import streamlit as st
import pandas as pd
import openai
from dotenv import load_dotenv
import os
import json

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

def music_prompt(df_summary, prompt):
    return f"Let's dive into music insights: {df_summary}. Your music query: {prompt}"

def chat_about_music(df_summary, prompt):
    prompt_text = music_prompt(df_summary, prompt)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt_text},
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message['content'].strip()

def summarize_music_data(df):
    summary_stats = df.describe(include='all').to_string()
    sample_rows = df.sample(min(5, len(df))).to_string()
    summary = f"Music Data Summary:\n{summary_stats}\n\nSample Rows:\n{sample_rows}"
    return summary

def check_keywords(prompt):
    keywords = ['song', 'music', 'industry', 'artist', 'album', 'genre', 'track', 'beat', 'melody', 'lyric', 'band', 'instrument', 'concert', 'performance']
    return any(keyword in prompt.lower() for keyword in keywords)

def load_conversation_history():
    if os.path.exists("conversation_history.json"):
        with open("conversation_history.json", "r") as file:
            return json.load(file)
    else:
        return []

def save_conversation_history(conversation_history):
    with open("conversation_history.json", "w") as file:
        json.dump(conversation_history, file)

st.set_page_config(layout='wide')

st.title("Explore Music Insights and Chat with OpenAI")

num_files = st.number_input("Number of Music Files to Upload", min_value=1, step=1)
uploaded_files = st.file_uploader("Upload your Music Files (CSV)", type=['csv'], accept_multiple_files=True, key="file_uploader")

# Load conversation history
conversation_history = load_conversation_history()

if uploaded_files and len(uploaded_files) >= num_files:
    for idx, file in enumerate(uploaded_files[:num_files], start=1):
        st.subheader(f"Music File {idx}")

        chunk_size = 100000  # Adjust based on your system's memory capacity
        for df_chunk in pd.read_csv(file, chunksize=chunk_size, encoding='latin1'):
            st.dataframe(df_chunk, use_container_width=True)

            input_text = st.text_area(f"Enter your music query for File {idx}")

            if input_text is not None:
                if check_keywords(input_text):
                    if st.button(f"Chat about Music File {idx}"):
                        st.info(f"Your Music Query for File {idx}: " + input_text)
                        df_summary = summarize_music_data(df_chunk)
                        result = chat_about_music(df_summary, input_text)
                        st.success(f"Response about Music File {idx}: {result}")

                        # Update conversation history
                        conversation_history.insert(0, {'role': 'user', 'content': input_text})
                        conversation_history.insert(0, {'role': 'system', 'content': result})
                        save_conversation_history(conversation_history)
                else:
                    st.warning("Out of Scope: Please ask a query related to songs, music, or the music industry.")

# Display conversation history
st.subheader("Conversation History")
for message in conversation_history:
    if message['role'] == 'user':
        st.text(f"You: {message['content']}")
    elif message['role'] == 'system':
        st.text(f"System: {message['content']}")

# Add a button to clear conversation history
if st.button("Clear Conversation History"):
    conversation_history.clear()
    save_conversation_history(conversation_history)
