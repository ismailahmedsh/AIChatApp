# **AI Chat App**

Welcome to the **AI Chat App**, a sophisticated chatbot platform powered by Streamlit, designed to showcase the profile of Ahmed Shehata and interact dynamically with users.

---

## **Features**
- **Dynamic Registration Form**: Collects user details like name, email, job role, and purpose of interaction.
- **Quick Suggestions**: Predefined questions for easy exploration of Ahmed Shehata's profile and achievements.
- **Customizable Chat Interface**: Users can ask free-form questions to learn more.
- **Google Sheets Integration**: Saves user interactions and registration data for analytics and follow-ups.
- **Streamlit-Powered UI**: Ensures a sleek, responsive, and user-friendly interface.

---

## **Technology Stack**
### **Langflow Architecture**
- Multiple Agent System.
- Vector Database using **AstraDB** for knowledge storage.
- **OpenAI Embeddings** for text vectorization.
- Custom Knowledge Base for domain-specific responses.

### **Cloud Infrastructure**
- **Google Cloud Platform (GCP)** for hosting and API integrations.
- **Google Sheets API** for managing and storing registration data.

### **Frontend**
- **Streamlit** for building the interactive web interface.
- Custom Python components for modular and reusable design.
- Responsive UI/UX design for a seamless user experience.

### **Backend Integration**
- RESTful API endpoints for handling user interactions and data storage.
- Custom error handling for better debugging and stability.
- Secure credentials management using service accounts and environment variables.

---

## **Purpose**
A sophisticated chatbot application featuring:
- Multi-agent AI interactions.
- User registration and analytics.
- Personalized responses based on a custom knowledge base.

---

## **Architecture Overview**
The app is modularized into reusable components, ensuring maintainability and scalability. Here's the breakdown:

### **1. Core Files**
- **`app.py`**:  
   The main entry point of the application. Handles the integration of all components and the overall user flow.
- **`flow.py`**:  
   Manages external API requests and utility logic for handling interactions outside the app.

---

### **2. Components** (Located in `components/`)
Each file represents a specific UI or logic component:
- **`registration_form.py`**:  
   Handles the dynamic user registration form, validates inputs, and integrates with Google Sheets for saving user data.  
- **`quick_suggestions.py`**:  
   Displays predefined questions for easy interaction, utilizing Streamlit's button components.  
- **`sidebar.py`**:  
   Contains logic for displaying a customizable sidebar for additional app controls.  
- **`reset.py`**:  
   Adds functionality to reset session state and start fresh.  
- **`user_input.py`**:  
   Manages free-text user input and processes it for chat interaction.  
- **`message_display.py`**:  
   Handles the display of user and bot messages in a conversational format.

---

### **3. Utilities** (Located in `utils/`)
Contains helper scripts for handling backend logic and integrations:
- **`google_sheets.py`**:  
   Integrates with Google Sheets API using `google-auth` and `google-api-python-client` to append and retrieve data.  
   - `append_to_sheet(data)`: Saves user registration details or interactions to Google Sheets.

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/aichatapp.git
cd aichatapp
