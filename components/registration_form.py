# components/registration_form.py
import streamlit as st
import re
from utils.google_sheets import append_to_sheet

def is_valid_email(email):
    """Validate email format using regex"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def show_loading_message():
    """Display a loading message with spinner"""
    with st.spinner('Saving your registration...'):
        st.empty()

def registration_form():
    """Display registration form and handle submission"""
    if 'is_registered' not in st.session_state:
        st.session_state.is_registered = False
    
    if not st.session_state.is_registered:
        st.markdown("""
            <h2 style='text-align: center;'>Welcome to Echo of Ahmed</h2>
            <p style='text-align: center;'>Fill out the form below to start exploring Shehata's brain</p>
        """, unsafe_allow_html=True)
        
        with st.form("registration_form"):
            # Required fields
            name = st.text_input("Full Name*", key="name")
            email = st.text_input("Email*", key="email")
            
            # Optional fields
            company = st.text_input("Company (Optional)", key="company")
            role = st.text_input("Job Role (Optional)", key="role")
            interests = st.multiselect(
                "Purpose of Visit (Optional)",
                ["Professional Networking", "Recruitment", "Learning", "Other"],
                key="interests"
            )
            
            submitted = st.form_submit_button("Submit")
            
            if submitted:
                # Validation
                if not name.strip():
                    st.error("Please enter your name")
                    return
                
                if not email.strip():
                    st.error("Please enter your email")
                    return
                
                if not is_valid_email(email):
                    st.error("Please enter a valid email address")
                    return
                
                # Prepare user data
                user_data = {
                    "name": name,
                    "email": email,
                    "company": company,
                    "role": role,
                    "interests": interests,
                }
                
                # Show loading message
                show_loading_message()
                
                # Save to Google Sheets
                success, message = append_to_sheet(user_data)
                
                if success:
                    # Store user information in session state
                    st.session_state.user_info = user_data
                    st.session_state.is_registered = True
                    st.rerun()
                else:
                    st.error(message)

def customize_chat_based_on_registration():
    """Customize chat experience based on registration info"""
    if hasattr(st.session_state, 'user_info'):
        user_info = st.session_state.user_info
        
        # Add a personalized welcome message
        if not st.session_state.get('welcomed', False):
            welcome_message = f"Welcome {user_info['name']}! "
            if user_info['interests']:
                welcome_message += f"I see you're interested in {', '.join(user_info['interests'])}. "
            welcome_message += "How can I help you today?"
            
            st.session_state.messages.append({
                "role": "bot",
                "content": welcome_message
            })
            st.session_state.welcomed = True