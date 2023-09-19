import streamlit as st
import pandas as pd
import datetime
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the pretrained GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Function to generate a coherent sentence using GPT-2
def generate_sentence(mood_score, mood_feeling, reason):
    input_text = f"My mood today is {mood_score}/10. I feel {mood_feeling} because {reason}."
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate text
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50, top_p=0.95)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    
    return generated_text

# Create or load a DataFrame to store mood journal data
if 'mood_data' not in st.session_state:
    st.session_state.mood_data = pd.DataFrame(columns=['Date', 'Mood Score', 'Mood Feeling', 'Reason'])

# Sidebar for different parts of the app
st.sidebar.title("Virtual Mood Journal")
selected_page = st.sidebar.radio("Select a Page", ["Mood Journal", "Export Data"])

if selected_page == "Mood Journal":
    st.title("Mood Journal")

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
