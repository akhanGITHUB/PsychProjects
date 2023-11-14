import streamlit as st
import pandas as pd
import datetime
import random

# Define a class for session state management
clas SessionState:
    def __init__(self):
        self.df_mood = pd.DataFrame(columns=['Date', 'Mood', 'Feeling', 'Explanation'])
        self.df_cbt = pd.DataFrame(columns=['Negative Thought', 'Based on Facts', 'Evidence', 'Jumping to Conclusions', 'Positive Perspective', 'Advice'])

# Create a session state object to persist data across runs
state = SessionState()

# Define a function to add entries to the Mood Journal
def add_mood_entry(date, mood, feeling, explanation):
    new_mood_entry = pd.DataFrame({'Date': [date], 'Mood': [mood], 'Feeling': [feeling], 'Explanation': [explanation]})
    state.df_mood = pd.concat([state.df_mood, new_mood_entry], ignore_index=True)

# Define a function to add entries to the CBT Journal
def add_cbt_entry(negative_thought, based_on_facts, evidence, jumping_to_conclusions, positive_perspective, advice):
    new_cbt_entry = pd.DataFrame({'Negative Thought': [negative_thought],
                                  'Based on Facts': [based_on_facts],
                                  'Evidence': [evidence],
                                  'Jumping to Conclusions': [jumping_to_conclusions],
                                  'Positive Perspective': [positive_perspective],
                                  'Advice': [advice]})
    state.df_cbt = pd.concat([state.df_cbt, new_cbt_entry], ignore_index=True)

# Define the Streamlit app layout
st.set_page_config(layout="wide")
st.title('Virtual Journal')

# Create a sidebar with page selection
page = st.sidebar.selectbox("Select a Page", ["Mood Journal Entry", "Positive Affirmations", "CBT Journal"])

# Mood Journal Entry Page
if page == "Mood Journal Entry":
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
        add_mood_entry(date, mood, feelings, explanation)
        st.success('Entry Added!')

    # Export Mood Data
    st.header('Export Mood Data')
    if st.button('Export Mood Data as CSV'):
        if not state.df_mood.empty:
            state.df_mood.to_csv('mood_journal.csv', index=False)
            st.success('Data Exported to mood_journal.csv')
        else:
            st.warning('No mood data to export.')

    # Mood Tracking
    st.header('Mood Tracking')
    st.subheader('Visualize Mood Over Time')

    if not state.df_mood.empty:
        mood_chart = st.line_chart(state.df_mood.set_index('Date')['Mood'], use_container_width=True)
    else:
        st.info('Start tracking your mood to see the visualization.')

    # Mood Journal Entries
    st.header('Your Mood Journal Entries')
    if not state.df_mood.empty:
        st.dataframe(state.df_mood)
    else:
        st.info('No mood entries yet. Add your mood journal entries above.')

# Positive Affirmations Page
elif page == "Positive Affirmations":
    st.header('Positive Affirmations')

    # List of 50 positive affirmations
    positive_affirmations = [
        "I am worthy of love and respect.",
        "I believe in my abilities.",
        "I am capable of achieving my goals.",
        "I am in control of my thoughts and emotions.",
        "I am a magnet for success and abundance.",
        "I radiate confidence and self-assurance.",
        "I am grateful for all that I have.",
        "I am open to new opportunities.",
        "I trust myself and my intuition.",
        "I am surrounded by loving and supportive people.",
        "I attract positive energy into my life.",
        "I am resilient and can overcome any obstacle.",
        "I am constantly growing and evolving.",
        "I deserve happiness and fulfillment.",
        "I am at peace with my past.",
        "I forgive myself and others for any past mistakes.",
        "I am confident in my decision-making abilities.",
        "I am a source of inspiration to others.",
        "I am in tune with my inner wisdom.",
        "I am a strong and capable person.",
        "I embrace change and adapt easily.",
        "I am a valuable and unique individual.",
        "I am free from self-doubt and fear.",
        "I am in charge of my own happiness.",
        "I am grateful for the gift of life.",
        "I am open to giving and receiving love.",
        "I am a loving and compassionate person.",
        "I am surrounded by beauty and positivity.",
        "I attract positive and loving relationships.",
        "I am a source of positivity in the world.",
        "I am open to receiving abundance in all forms.",
        "I trust that the universe has a plan for me.",
        "I am aligned with my life's purpose.",
        "I am a beacon of light and hope.",
        "I am confident in my abilities to achieve my dreams.",
        "I am a creative and innovative thinker.",
        "I am resilient in the face of challenges.",
        "I am a powerful manifestor.",
        "I am worthy of all the good that comes my way.",
        "I am open to the abundance of the universe.",
        "I am a magnet for positive experiences.",
        "I am in perfect health and well-being.",
        "I am grateful for my body and all it does for me.",
        "I am at peace with my body.",
        "I am confident in my physical appearance.",
        "I am capable of achieving my fitness goals.",
        "I am disciplined in taking care of my body.",
        "I am in harmony with nature."
    ]

    if st.button('Generate a positive affirmation'):
        random_affirmation = random.choice(positive_affirmations)
        st.subheader('Random Positive Affirmation:')
        st.write(random_affirmation)

# CBT Journal Page
elif page == "CBT Journal":
    st.header('CBT Journal Entry')
    negative_thought = st.text_area('What is your negative thought?')
    based_on_facts = st.text_area('Is this thought based on facts?')
    evidence = st.text_area('What evidence do you have to support it?')
    jumping_to_conclusions = st.text_area('Am I jumping to conclusions?')
    positive_perspective = st.text_area('Is there a more positive perspective on this thought?')
    advice = st.text_area("What advice would you give a friend in the same situation?")

    if st.button('Add CBT Entry'):
        add_cbt_entry(negative_thought, based_on_facts, evidence, jumping_to_conclusions, positive_perspective, advice)
        st.success('CBT Entry Added!')

    # Export CBT Data
    st.header('Export CBT Data')
    if st.button('Export CBT Data as CSV'):
        if not state.df_cbt.empty:
            state.df_cbt.to_csv('cbt_journal.csv', index=False)
            st.success('CBT Data Exported to cbt_journal.csv')
        else:
            st.warning('No CBT data to export.')

    # CBT Journal Entries
    st.header('Your CBT Journal Entries')
    if not state.df_cbt.empty:
        st.dataframe(state.df_cbt)
    else:
        st.info('No CBT entries yet. Add your CBT journal entries above.')
