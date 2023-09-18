import streamlit as st
import pandas as pd
import datetime
import openai

# Set your OpenAI GPT-3 API key
openai.api_key = "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"

# Function to generate a coherent sentence using OpenAI GPT-3
def generate_sentence(mood_score, mood_feeling, reason):
    prompt = f"My mood today is {mood_score}/10. I feel {mood_feeling} because {reason}."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,  # Adjust the max tokens as needed
        n = 1,
        stop=None,
        temperature=0.7  # Adjust temperature for creativity
    )
    return response.choices[0].text.strip()

# Create or load a DataFrame to store mood journal data
if 'mood_data' not in st.session_state:
    st.session_state.mood_data = pd.DataFrame(columns=['Date', 'Mood Score', 'Mood Feeling', 'Reason'])

# Sidebar for different parts of the app
st.sidebar.title("Virtual Mood Journal")
selected_page = st.sidebar.radio("Select a Page", ["Mood Journal", "Export Data"])

if selected_page == "Mood Journal":
    st.title("Virtual Mood Journal")

    # Get user input for mood journal
    date = st.date_input("Date", datetime.date.today())
    mood_score = st.slider("Rate Your Mood (0-10)", 0, 10, 5)
    mood_feeling = st.selectbox("Select a Mood/Feeling", [
        "Happy", "Sad", "Angry", "Excited", "Relaxed",
        "Stressed", "Confident", "Anxious", "Grateful", "Surprised"
    ])
    reason = st.text_area("Why do you feel this way?")
    
    if st.button("Record Entry"):
        if date and mood_score and mood_feeling and reason:
            sentence = generate_sentence(mood_score, mood_feeling, reason)
            st.write(f"Recorded Entry: {sentence}")
            st.session_state.mood_data = st.session_state.mood_data.append({
                'Date': date,
                'Mood Score': mood_score,
                'Mood Feeling': mood_feeling,
                'Reason': reason
            }, ignore_index=True)
            st.success("Entry Recorded Successfully!")

elif selected_page == "Export Data":
    st.title("Export Mood Journal Data")
    if not st.session_state.mood_data.empty:
        export_button = st.button("Export Data as CSV")
        if export_button:
            csv_file = st.session_state.mood_data.to_csv(index=False)
            st.download_button(
                "Click to Download",
                csv_file,
                key="export_data_csv",
                help="Export your mood journal data as a CSV file."
            )
    else:
        st.warning("No data to export. Record some entries first.")
