import unittest
import time
from unittest.mock import patch, MagicMock
from utils.keep_alive import KeepAliveManager

class TestKeepAliveManager(unittest.TestCase):
    def setUp(self):
        self.manager = KeepAliveManager(interval_minutes=1)  # Shorter interval for testing
    
    def tearDown(self):
        if self.manager.is_running:
            self.manager.stop()
    
    @patch('requests.get')
    def test_ping_langflow(self, mock_get):
        # Setup mock response
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        # Test successful ping
        result = self.manager.ping_langflow()
        self.assertTrue(result)
        mock_get.assert_called_once()
        
        # Test failed ping
        mock_get.side_effect = Exception("Connection error")
        result = self.manager.ping_langflow()
        self.assertFalse(result)
    
    def test_service_lifecycle(self):
        # Test service start
        self.manager.start()
        self.assertTrue(self.manager.is_running)
        self.assertIsNotNone(self.manager.thread)
        
        # Wait for a ping cycle
        time.sleep(2)
        
        # Test service stop
        self.manager.stop()
        self.assertFalse(self.manager.is_running)
    
    @patch('utils.keep_alive.KeepAliveManager.ping_langflow')
    @patch('utils.keep_alive.KeepAliveManager.ping_database')
    def test_keep_alive_task(self, mock_ping_db, mock_ping_langflow):
        # Setup mocks
        mock_ping_langflow.return_value = True
        mock_ping_db.return_value = True
        
        # Execute keep-alive task
        self.manager.keep_alive_task()
        
        # Verify both services were pinged
        mock_ping_langflow.assert_called_once()
        mock_ping_db.assert_called_once()

if __name__ == '__main__':
    unittest.main() 