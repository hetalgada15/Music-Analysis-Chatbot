# Music Analysis using CSV Chatbot

## Overview


Welcome! I've developed Music Chat CSV, a Streamlit app that merges OpenAI's GPT-3.5 Turbo for rich music insights. Users can upload CSV files for analysis and engage in conversational interactions, capturing the essence of music-related queries seamlessly.

## Objective

The main goal of this project was to build a chatbot application leveraging Large Language Models (LLMs) to process natural language queries about music. The specific objectives include:

- **Domain Selection:** Choose the domain of music to provide insights and information to users interested in various aspects of music, such as songs, artists, genres, and more.
  
- **Application Development:** Develop a user-friendly interface using Streamlit for users to input natural language queries related to music. Integrate OpenAI's GPT-3.5 Turbo model for generating relevant and context-aware responses.
  
- **Evaluation and Testing:** Thoroughly test the application with diverse music-related queries to assess its performance, accuracy, and usability.

## Features

- **User Interface:** A clean and intuitive interface powered by Streamlit, allowing users to input natural language queries.
  
- **LLM Integration:** Integration with OpenAI's GPT-3.5 Turbo model to process queries and generate informative responses.
  
- **Music Data Insights:** Display music data summary and sample rows for better context and understanding.
  
- **Conversation History:** Keep track of user-system interactions with a conversation history display.

## Technologies Used

- Python: Backend development and data manipulation.
  
- Streamlit: Frontend user interface development.
  
- Pandas: Data analysis and manipulation.
  
- OpenAI API: Integration for LLM-based responses.
  
- JSON: Conversation history storage format.

## Setup and Usage

1. **Clone the Repository:**

   ```bash
   https://github.com/hetalgada15/Music-Analysis-Chatbot.git
   cd ChatCSV-Streamlit-App


2. **Install Dependencies:**

   ```bash

   pip install -r requirements.txt

  
3. **Set Up OpenAI API Key:**

Create a .env file in the project root directory with your OpenAI API key:

OPENAI_API_KEY=your_api_key_here

4. **Run the Application:**
   ```bash
   streamlit run app.py

5.**Access the Application:**

Open your web browser and navigate to http://localhost:8501.

## Testing

1. Input natural language queries related to music into the text area.
2. Click the "Chat about Music" button to generate responses based on the queries.
3. Explore conversation history to review past interactions.

   
## Additional Resources
OpenAI API Documentation: Learn more about OpenAI's GPT-3.5 Turbo model.

## Streamlit Documentation: 
Explore Streamlit for building interactive web applications.

## Contributors
Hetal Gada: Project developer and main contributor.
