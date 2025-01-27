# app.py
import streamlit as st
from components.quick_suggestions import display_quick_suggestions
from components.sidebar import sidebar
from components.reset import reset_button
from components.user_input import user_input_process
from components.message_display import message_display
from components.registration_form import registration_form, customize_chat_based_on_registration

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.update({
        'messages': [],
        'show_suggestions': True,
        'clicked_questions': [],
        'is_registered': False,
    })

# Set page configuration
st.set_page_config(page_title="Ahmed Shehata", layout="wide")

# Load CSS styles
def load_css(file_name):
    with open(file_name, "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_css("styles/styles.css")
load_css("styles/registration.css")

# Display registration form or chat interface
if not st.session_state.get('is_registered', False):
    registration_form()
else:
    # Set Icons
    st.markdown(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">',
        unsafe_allow_html=True
    )

    # Custom header with navigation icons
    st.markdown("""
        <div class="nav-container">
            <div class="nav-title">
                <h1>Echo of Ahmed Shehata</h1>
                <h4>An AI That Knows Me Best</h4>
            </div>
            <div class="nav-icons">
                <a href="https://www.linkedin.com/in/ahmedismailshehata" target="_blank">
                    <i class="fab fa-linkedin"></i>
                </a>
                <a href="https://www.instagram.com/ahmed_issh/#" target="_blank">
                    <i class="fab fa-instagram"></i>
                </a>
                <a href="https://github.com/ismailahmedsh" target="_blank">
                    <i class="fab fa-github"></i>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Sidebar
    sidebar()

    # Customize chat based on registration info
    customize_chat_based_on_registration()

    # Display components
    message_display()
    display_quick_suggestions()
    user_input_process()
    reset_button()