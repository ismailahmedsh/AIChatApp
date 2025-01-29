# components/quick_suggestions.py
import streamlit as st
from utils.flow import run_flow
from utils.error_handler import handle_langflow_error

def display_quick_suggestions():
    """Quick suggestions that disappear immediately on click"""
    if not st.session_state.get("show_suggestions", True):
        return

    # Store questions in session state to maintain consistency
    if 'quick_questions' not in st.session_state:
        st.session_state.quick_questions = [
            "What's the story behind his education journey?",
            "Can you share details about his professional experience?",
            "What are some of his unique interests?"
        ]

    # Header remains visible after suggestions disappear
    st.markdown("""
        <h4 style='text-align: left; margin-left: 1rem; margin-bottom: 0.5rem;'>
            Quick Suggestions
        </h4>
    """, unsafe_allow_html=True)

    # Create a single container for buttons
    button_container = st.container()

    with button_container:
        cols = st.columns(3) if not st.session_state.get('is_mobile') else [st.container()]
        
        for idx, question in enumerate(st.session_state.quick_questions):
            target_col = cols[idx % 3] if not st.session_state.get('is_mobile') else cols[0]
            
            with target_col:
                if st.button(
                    question,
                    key=f"qs_{question}",  # Unique key using question text
                    use_container_width=True
                ):
                    # Immediately update state and prevent re-render
                    st.session_state.show_suggestions = False
                    st.session_state.pending_question = question
                    st.rerun()

def process_pending_question():
    """Handle question processing after buttons disappear"""
    if 'pending_question' not in st.session_state:
        return

    question = st.session_state.pending_question
    del st.session_state.pending_question  # Prevent reprocessing

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    # Process with loading state
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

    # Force immediate UI update
    st.rerun()