import streamlit as st

def sidebar():
    with st.sidebar: 
        st.markdown("## About Ahmed Shehata")
        st.markdown("""
        - 💼 **Profession**: Senior Implementation Consultant
        - 📫 **Contact**: ismailahmedsh@gmail.com 
        """)
        
        # Portfolio button
        st.link_button("🌐 Portfolio", "https://ismailahmedsh.github.io/portofolio/index.html")
        st.markdown("---")
        st.markdown("## About the Project")
        st.markdown("""
        - 🤖 **AI Chatbot**: This chatbot is designed to answer questions about Ahmed Shehata.
        - 🛠️ **Technology Stack**:
            - **Langflow Architecture**:
                - Multiple Agent System
                - Vector Database using AstraDB for knowledge storage
                - OpenAI Embeddings for text vectorization
                - Custom Knowledge Base for domain-specific responses
            - **Cloud Infrastructure**:
                - Google Cloud Platform (GCP)
                - Google Sheets API for registration data
            - **Frontend**:
                - Streamlit for web interface
                - Custom Python components
                - Responsive UI/UX design
            - **Backend Integration**:
                - RESTful API endpoints
                - Custom error handling
                - Secure credentials management
        - 🎯 **Purpose**: A sophisticated chatbot application featuring multi-agent AI interactions, user registration, and personalized responses based on a custom knowledge base.
        """)
        # Add social badges with icons
        st.markdown("---")
        st.markdown("**🌍 Connect With Me**")
        cols = st.columns(3)
        with cols[0]:
            st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ahmedismailshehata)")
        with cols[1]:
            st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ismailahmedsh)")
        with cols[2]:
            st.markdown("""
                <div style="text-align: center;">
                    <a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fahmedshehata.streamlit.app&count_bg=%2300F3FF&title_bg=%23DD0909&icon=ionic.svg&icon_color=%23010101&title=Views&edge_flat=false"/></a>
                </div>
                """, unsafe_allow_html=True)