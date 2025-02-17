# flow.py
import requests
import json
import streamlit as st
import time
import logging

def run_flow(message: str) -> dict:
    """Run the Langflow with proper response parsing using secrets"""
    start_time = time.time()
    try:
        api_url = f"{st.secrets.langflow.base_api_url}/lf/{st.secrets.langflow.langflow_id}/api/v1/run/{st.secrets.langflow.endpoint}"
        
        payload = {
            "input_value": message,
            "output_type": "chat",
            "input_type": "chat",
        }
        
        headers = {
            "Authorization": f"Bearer {st.secrets.langflow.application_token}",
            "Content-Type": "application/json"
        }

        # Add retry mechanism for hibernation recovery
        max_retries = 3
        retry_delay = 2  # seconds
        
        for attempt in range(max_retries):
            try:
                response = requests.post(api_url, json=payload, headers=headers)
                response.raise_for_status()
                result = response.json()
                break
            except requests.exceptions.RequestException as e:
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    continue
                raise e
        
        if (result and 'outputs' in result and 
            len(result['outputs']) > 0 and 
            'outputs' in result['outputs'][0] and 
            len(result['outputs'][0]['outputs']) > 0 and 
            'results' in result['outputs'][0]['outputs'][0] and 
            'message' in result['outputs'][0]['outputs'][0]['results'] and 
            'text' in result['outputs'][0]['outputs'][0]['results']['message']):
            
            message_text = result['outputs'][0]['outputs'][0]['results']['message']['text']
            logging.info(f"Request completed in {time.time() - start_time:.2f} seconds")
            return {"result": message_text}
        else:
            return {"result": "I apologize, but I couldn't process the response properly. Please try again."}

    except requests.exceptions.RequestException as e:
        # Log the error for monitoring
        logging.error(f"Request failed after {time.time() - start_time:.2f} seconds: {str(e)}")
        return {"result": "I encountered a connection error. Please try again later."}
    except json.JSONDecodeError:
        return {"result": "I received an invalid response format. Please try again."}
    except Exception:
        return {"result": "An unexpected error occurred. Please try again later."}