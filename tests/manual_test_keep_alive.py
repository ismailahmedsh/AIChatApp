import sys
import os

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

import time
import logging
from utils.keep_alive import keep_alive_manager

# Configure logging to see the output
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def test_keep_alive():
    try:
        print("Starting keep-alive service...")
        keep_alive_manager.start()
        
        # Run for 5 minutes
        print("Service will run for 5 minutes. Check the logs for ping activities.")
        print("Press Ctrl+C to stop earlier.")
        
        time.sleep(300)  # 5 minutes
        
    except KeyboardInterrupt:
        print("\nTest interrupted by user.")
    finally:
        print("Stopping keep-alive service...")
        keep_alive_manager.stop()
        print("Test completed.")

if __name__ == "__main__":
    test_keep_alive() 