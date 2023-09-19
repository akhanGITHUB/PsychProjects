import streamlit as st
import pandas as pd
import datetime

# Create a dataframe to store mood journal data
df = pd.DataFrame(columns=['Date', 'Mood', 'Feeling', 'Explanation'])

# Define a function to add entries to the mood journal
def add_entry(date, mood, feeling, explanation):
    global df
    df = df.append({'Date': date, 'Mood': mood, 'Feeling': feeling, 'Explanation': explanation}, ignore_index=True)

# Define the Streamlit app layout
st.title('Virtual Mood Journal')

# Mood Journal Entry
st.header('Mood Journal Entry')
today = datetime.date.today()
date = st.date_input('Date', today)
mood = st.slider('Rate Your Mood (0-10)', 0, 10, 5)
feelings = st.selectbox('Select Feeling', [
    'Happy', 'Sad', 'Angry', 'Excited', 'Calm', 'Anxious', 'Grateful', 'Stressed',
    'Confident', 'Relaxed', 'Lonely', 'Energetic', 'Content', 'Overwhelmed', 'Optimistic'
])
explanation = st.text_area('Why do you feel that way?', '')

if st.button('Add Entry'):
    add_entry(date, mood, feelings, explanation)
    st.success('Entry Added!')

# Export Data
st.header('Export Data')
if st.button('Export Data as CSV'):
    if not df.empty:
        df.to_csv('mood_journal.csv', index=False)
        st.success('Data Exported to mood_journal.csv')
    else:
        st.warning('No data to export.')

# Mood Tracking
st.header('Mood Tracking')
st.subheader('Visualize Mood Over Time')
if not df.empty:
    mood_chart = st.line_chart(df.set_index('Date')['Mood'])
else:
    st.info('Start tracking your mood to see the visualization.')

# Mood Journal Entries
st.header('Your Mood Journal Entries')
if not df.empty:
    st.dataframe(df)
else:
    st.info('No entries yet. Add your mood journal entries above.')
