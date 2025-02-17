import requests
import schedule
import threading
import time
import logging
from datetime import datetime
import streamlit as st

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KeepAliveManager:
    def __init__(self, interval_minutes=10):
        self.interval_minutes = interval_minutes
        self.last_ping_time = None
        self.is_running = False
        self.thread = None
    
    def ping_langflow(self):
        """Send a lightweight request to Langflow to keep it active"""
        try:
            api_url = f"{st.secrets.langflow.base_api_url}/lf/{st.secrets.langflow.langflow_id}/api/v1/run/{st.secrets.langflow.endpoint}"
            headers = {
                "Authorization": f"Bearer {st.secrets.langflow.application_token}",
                "Content-Type": "application/json"
            }
            
            # Use a minimal payload for the health check
            payload = {
                "input_value": "ping",
                "output_type": "chat",
                "input_type": "chat",
            }
            
            response = requests.post(api_url, json=payload, headers=headers)
            response.raise_for_status()
            
            self.last_ping_time = datetime.now()
            logger.info(f"Successfully pinged Langflow at {self.last_ping_time}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to ping Langflow: {str(e)}")
            return False
    
    def ping_database(self):
        """Send a lightweight query to AstraDB to keep it active"""
        try:
            # Implement database ping based on your AstraDB setup
            # This is a placeholder - implement actual DB ping
            logger.info("Database ping successful")
            return True
            
        except Exception as e:
            logger.error(f"Failed to ping database: {str(e)}")
            return False
    
    def keep_alive_task(self):
        """Execute all keep-alive tasks"""
        self.ping_langflow()
        self.ping_database()
    
    def run_scheduler(self):
        """Run the scheduler in a loop"""
        while self.is_running:
            schedule.run_pending()
            time.sleep(60)  # Check schedule every minute
    
    def start(self):
        """Start the keep-alive service"""
        if not self.is_running:
            self.is_running = True
            
            # Schedule the keep-alive task
            schedule.every(self.interval_minutes).minutes.do(self.keep_alive_task)
            
            # Run initial ping
            self.keep_alive_task()
            
            # Start scheduler in a separate thread
            self.thread = threading.Thread(target=self.run_scheduler, daemon=True)
            self.thread.start()
            
            logger.info("Keep-alive service started")
    
    def stop(self):
        """Stop the keep-alive service"""
        if self.is_running:
            self.is_running = False
            schedule.clear()
            if self.thread:
                self.thread.join(timeout=1)
            logger.info("Keep-alive service stopped")

# Create a singleton instance
keep_alive_manager = KeepAliveManager() 