import streamlit as st

def reset_button():
    """Reset button with preserved dark mode"""
    if st.session_state.get('messages', []):
        if st.button("Reset Chat", key="reset_button"):
            # Reset chat-specific states
            st.session_state.update({
                'messages': [],
                'show_suggestions': True,
                'clicked_questions': [],
            })
            st.rerun()