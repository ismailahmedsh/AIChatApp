# utils/google_sheets.py
import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import streamlit as st
from datetime import datetime

def get_sheet_id():
    """Get sheet ID from secrets with fallback options"""
    try:
        # Try root level first
        if "sheet_id" in st.secrets:
            return st.secrets["sheet_id"]
        # Try inside gcp_service_account
        elif "gcp_service_account" in st.secrets and "sheet_id" in st.secrets.gcp_service_account:
            return st.secrets.gcp_service_account["sheet_id"]
        else:
            raise ValueError("sheet_id not found in secrets")
    except Exception as e:
        raise ValueError(f"Failed to get sheet_id: {str(e)}")

def create_google_sheets_connection():
    """Create a connection to Google Sheets API"""
    try:
        credentials = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=[
                "https://www.googleapis.com/auth/spreadsheets",
            ],
        )
        
        service = build('sheets', 'v4', credentials=credentials)
        return service
    except Exception as e:
        raise e

def append_to_sheet(user_data):
    """Append user registration data to Google Sheet"""
    try:
        service = create_google_sheets_connection()
        SHEET_ID = get_sheet_id()
        
        # Prepare the data
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row_data = [
            timestamp,
            user_data["name"],
            user_data["email"],
            user_data.get("company", ""),
            user_data.get("role", ""),
            ", ".join(user_data.get("interests", []))
        ]

        request = service.spreadsheets().values().append(
            spreadsheetId=SHEET_ID,
            range='Sheet1!A:G',
            valueInputOption='USER_ENTERED',
            insertDataOption='INSERT_ROWS',
            body={
                'values': [row_data]
            }
        )
        
        request.execute()
        return True, "Registration data saved successfully!"
        
    except ValueError as ve:
        error_msg = f"Configuration error: {str(ve)}"
        st.error(error_msg)
        return False, error_msg
    except Exception as e:
        error_msg = f"Error saving registration data: {str(e)}"
        st.error(error_msg)
        return False, error_msg