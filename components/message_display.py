import streamlit as st

def message_display():
    for message in st.session_state.get('messages', []):
        if message["role"] == "user":
            st.markdown(f"""
                <div class="chat-message user">
                    <div class="content">{message['content']}</div>
                    <div class="icon">
                        <svg viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M27.6488 48.6343C27.6093 48.6489 27.5698 48.6636 27.5304 48.6784L26.3003 49.1395C20.1048 51.4615 16 57.3836 16 64C16 66.2091 17.7909 68 20 68H60C62.2091 68 64 66.2091 64 64C64 57.3836 59.8952 51.4615 53.6997 49.1395L52.4696 48.6784C52.4302 48.6636 52.3907 48.6489 52.3512 48.6343L45.908 54.0897C42.4983 56.9767 37.5017 56.9767 34.092 54.0897L27.6488 48.6343Z" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" />
                            <path d="M27.0336 18.8434C33.4206 10.0086 46.5797 10.0086 52.9666 18.8434L59.5812 27.993C63.2552 33.0751 62.3965 40.1292 57.6105 44.1816L45.9081 54.0899C42.4985 56.9769 37.5018 56.9769 34.0922 54.0899L22.3898 44.1816C17.6038 40.1293 16.7451 33.0751 20.4191 27.9929L27.0336 18.8434Z" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" />
                            <path d="M18.2012 36.1945C24.0233 31.0925 31.6505 28 40.0001 28C48.3496 28 55.9769 31.0925 61.7989 36.1945" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" />
                            <path d="M26.4551 30.8893C26.5039 31.5085 26.5937 32.1275 26.7253 32.7424L26.949 33.7877C27.787 37.7041 30.3395 41.0372 33.902 42.8672C37.73 44.8335 42.2712 44.8335 46.0991 42.8672C49.6616 41.0372 52.2141 37.7041 53.0521 33.7877L53.2758 32.7424C53.4074 32.1275 53.4972 31.5084 53.546 30.8892" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" />
                            <path d="M40 56.2549V68.0001" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" />
                        </svg>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="chat-message bot">
                    <div class="icon">
                        <svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M20 30C20 28.8954 20.8954 28 22 28H58C59.1046 28 60 28.8954 60 30V66C60 67.1046 59.1046 68 58 68H22C20.8954 68 20 67.1046 20 66V30Z" stroke="#C2CCDE" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M28 44C28 41.7909 29.7909 40 32 40C34.2091 40 36 41.7909 36 44C36 46.2091 34.2091 48 32 48C29.7909 48 28 46.2091 28 44Z" stroke="#C2CCDE" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M44 44C44 41.7909 45.7909 40 48 40C50.2091 40 52 41.7909 52 44C52 46.2091 50.2091 48 48 48C45.7909 48 44 46.2091 44 44Z" stroke="#C2CCDE" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M50 68C51.1046 68 52 67.1046 52 66V60C52 58.8954 51.1046 58 50 58H30C28.8954 58 28 58.8954 28 60V66C28 67.1046 28.8954 68 30 68" stroke="#C2CCDE" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M20 40H14C12.8954 40 12 40.8954 12 42V54C12 55.1046 12.8954 56 14 56H20" stroke="#C2CCDE" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M60 56H66C67.1046 56 68 55.1046 68 54V42C68 40.8954 67.1046 40 66 40H60" stroke="#C2CCDE" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M40 28V20" stroke="#C2CCDE" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M36 16C36 13.7909 37.7909 12 40 12C42.2091 12 44 13.7909 44 16C44 18.2091 42.2091 20 40 20C37.7909 20 36 18.2091 36 16Z" stroke="#C2CCDE" stroke-linecap="round" stroke-linejoin="round" />
                        </svg>
                    </div>
                    <div class="content">{message['content']}</div>
                </div>
            """, unsafe_allow_html=True)