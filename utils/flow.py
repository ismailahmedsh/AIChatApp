# flow.py
import requests
import json
import streamlit as st

def run_flow(message: str) -> dict:
    """Run the Langflow with proper response parsing using secrets"""
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

        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        
        if (result and 'outputs' in result and 
            len(result['outputs']) > 0 and 
            'outputs' in result['outputs'][0] and 
            len(result['outputs'][0]['outputs']) > 0 and 
            'results' in result['outputs'][0]['outputs'][0] and 
            'message' in result['outputs'][0]['outputs'][0]['results'] and 
            'text' in result['outputs'][0]['outputs'][0]['results']['message']):
            
            message_text = result['outputs'][0]['outputs'][0]['results']['message']['text']
            return {"result": message_text}
        else:
            return {"result": "I apologize, but I couldn't process the response properly. Please try again."}

    except requests.exceptions.RequestException as e:
        return {"result": "I encountered a connection error. Please try again later."}
    except json.JSONDecodeError:
        return {"result": "I received an invalid response format. Please try again."}
    except Exception:
        return {"result": "An unexpected error occurred. Please try again later."}