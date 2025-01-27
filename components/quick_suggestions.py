# components/quick_suggestions.py
import streamlit as st
from utils.flow import run_flow
from utils.error_handler import handle_langflow_error

def get_screen_width():
    """Estimate if we're on mobile based on a temporary element"""
    temp_col = st.columns(3)
    with temp_col[0]:
        temp_button = st.empty()
    try:
        width = temp_button._element.width
    except:
        width = 1000  # Default to desktop view
    temp_button.empty()
    return width

def display_quick_suggestions():
    """Quick suggestions with Langflow integration and loading state"""
    if not st.session_state.get("show_suggestions", True):
        return

    # Left-aligned header with matching style
    st.markdown("""
        <h4 style='text-align: left; margin-left: 1rem; margin-bottom: 0.5rem;'>
            Quick Suggestions
        </h4>
    """, unsafe_allow_html=True)
    
    # Create a placeholder for the loading indicator
    loading_placeholder = st.empty()
    
    quick_questions = [
        "What's the story behind his education journey?",
        "Can you share details about his professional experience?",
        "What impressive achievements has he accomplished?",
        "What are some of his unique interests?",
        "What hobbies keep him inspired and energized?"
    ]

    # Check if we're on mobile
    is_mobile = get_screen_width() < 768
    
    if is_mobile:
        # Mobile layout - single column, shorter list
        mobile_questions = quick_questions[:3]  # Only show first 3 questions on mobile
        for question in mobile_questions:
            if st.button(question, key=f"suggestion_{question}", use_container_width=True):
                handle_question_click(question, loading_placeholder)
    else:
        # Desktop layout - three columns
        col1, col2, col3 = st.columns([1, 1, 1], gap="small")
        button_states = []
        
        for idx, question in enumerate(quick_questions):
            with [col1, col2, col3][idx % 3]:
                button_clicked = st.button(question, key=f"suggestion_{question}", use_container_width=True)
                button_states.append((question, button_clicked))
        
        for question, clicked in button_states:
            if clicked:
                handle_question_click(question, loading_placeholder)

def handle_question_click(question, loading_placeholder):
    """Handle when a suggestion is clicked"""
    if question not in st.session_state.clicked_questions:
        st.session_state.clicked_questions.append(question)
        
        st.session_state.messages.append({
            "role": "user", 
            "content": question
        })
        
        with loading_placeholder:
            with st.status("🤖 Echo is thinking...", expanded=True) as status:
                try:
                    response = run_flow(question)
                    bot_response = response.get('result', 'I apologize, but I encountered an issue processing your request.')
                    status.update(label="✅ Response ready!", state="complete")
                    st.session_state.messages.append({
                        "role": "bot",
                        "content": bot_response
                    })
                except Exception as e:
                    status.update(label="❌ Error occurred", state="error")
                    error_msg = handle_langflow_error(e)
                    st.session_state.messages.append({
                        "role": "bot",
                        "content": error_msg
                    })
        
        st.session_state.show_suggestions = False
        st.rerun()