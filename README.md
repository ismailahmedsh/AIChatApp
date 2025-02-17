# AI Chat App - Your Personal AI Assistant

Hey there! 👋 Welcome to my AI Chat App project. I built this to create a smart, interactive way for people to learn about my professional background and experience. It's not just your average chatbot - it's powered by some really cool tech that makes it feel more like talking to a knowledgeable colleague than a robot.

## What Makes This Special?

### Smart Conversations with Multi-Agent AI
I've implemented a multi-agent system using Langflow that makes the chat experience much more natural and context-aware. Here's how it works:

- **FAQ Agent**: Handles common questions about my background, skills, and experience
- **Context-Aware Agent**: Maintains conversation flow and remembers previous interactions
- **Knowledge Base Agent**: Taps into my detailed professional history stored in a vector database

### Technical Deep Dive

#### The Brain Behind the Bot
- **Langflow Architecture**: I've set up a custom flow that connects multiple AI agents, each specialized in different aspects of conversation
- **Vector Database (AstraDB)**:
  - Stores and indexes all my professional information
  - Uses OpenAI embeddings to convert text into vector representations
  - Enables semantic search for more accurate responses
  - Maintains persistent connections with keep-alive mechanisms

#### Cloud Infrastructure
- **Google Cloud Platform (GCP)**:
  - Hosts the application with auto-scaling capabilities
  - Manages API integrations securely
  - Handles user data and analytics
- **Google Sheets Integration**:
  - Tracks user interactions and feedback
  - Stores registration data for follow-ups
  - Enables easy data analysis and reporting

#### Frontend Magic
I chose Streamlit for the frontend because it lets me create a clean, professional interface without sacrificing functionality:

- **Dynamic Registration**: Smooth user onboarding process
- **Responsive Design**: Works great on both desktop and mobile
- **Real-time Updates**: Instant message responses and status updates
- **Custom Components**: Modular design for easy maintenance

#### Behind the Scenes

```
User Query → FAQ Agent → Vector DB Lookup → Context Processing → Response Generation
```

The system uses:
- OpenAI embeddings for semantic understanding
- AstraDB for knowledge storage and retrieval
- Custom error handling and retry mechanisms
- Keep-alive services to prevent connection timeouts

## Getting Started

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/ai-chat-app.git
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up your environment variables**
```bash
# Create a .env file with your credentials
LANGFLOW_API_KEY=your_key
ASTRA_DB_TOKEN=your_token
GCP_CREDENTIALS=your_credentials
```

4. **Run the app**
```bash
streamlit run app.py
```

## What's Next?

I'm constantly improving the app with features like:
- Enhanced context awareness
- More sophisticated multi-agent interactions
- Improved response accuracy and speed
- Additional analytics and insights

## Connect With Me

Got questions or suggestions? Feel free to reach out:
- 📧 Email: ismailahmedsh@gmail.com
- 💼 LinkedIn: [Ahmed Shehata](https://www.linkedin.com/in/ahmedismailshehata)
- 🌐 Portfolio: [View Portfolio](https://ismailahmedsh.github.io/portofolio/index.html)

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
