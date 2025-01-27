import requests

def handle_langflow_error(error):
    if isinstance(error, requests.exceptions.ConnectionError):
        return "I'm having trouble connecting to my knowledge base. Please try again in a moment."
    elif isinstance(error, requests.exceptions.Timeout):
        return "The response took too long. Please try again."
    elif isinstance(error, requests.exceptions.RequestException):
        return "There was an issue processing your request. Please try again."
    elif isinstance(error, KeyError):
        return "I received an unexpected response format. Please try again."
    else:
        return f"An unexpected error occurred: {str(error)}"