# components/user_input.py
import streamlit as st
from utils.flow import run_flow

def user_input_process():
    """Handle user input with Langflow integration"""
    if user_input := st.chat_input("Type your message here..."):
        # Add user message to chat history
        st.session_state.messages.append({
            "role": "user", 
            "content": user_input
        })
        
        # Hide suggestions when user types a message
        st.session_state.show_suggestions = False
        
        # Show typing indicator
        with st.status("🤖 Echo is thinking...", expanded=True) as status:
            try:
                # Get response from Langflow
                response = run_flow(user_input)
                
                # Extract the actual response from Langflow's output
                bot_response = response.get('result', 'I apologize, but I encountered an issue processing your request.')
                
                # Mark the status as complete
                status.update(label="✅ Response ready!", state="complete")
                
                # Add bot response to chat history
                st.session_state.messages.append({
                    "role": "bot",
                    "content": bot_response
                })
                
            except Exception as e:
                # Handle any errors gracefully
                status.update(label="❌ Error occurred", state="error")
                error_message = f"I apologize, but I encountered an error: {str(e)}"
                st.session_state.messages.append({
                    "role": "bot",
                    "content": error_message
                })
        
        # Trigger rerun to update the chat interface
        st.rerun()