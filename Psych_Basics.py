import streamlit as st

# Create a function to display information for Mental Health Conditions
def display_mental_health_conditions():
    st.title("Mental Health Conditions")
    
    # Display buttons to choose between Mood Disorders and Personality Disorders
    if st.button("Mood Disorders"):
        display_mood_disorders()
    if st.button("Personality Disorders"):
        display_personality_disorders()

# Create a function to display information for Mood Disorders
def display_mood_disorders():
    st.title("Mood Disorders")
    
    # Define the list of common mood disorders
    mood_disorders = ["Depression", "Anxiety", "Bipolar Disorder", "Dysthymia", "Cyclothymic Disorder"]
    
    # Create a dropdown to select a mood disorder
    selected_mood_disorder = st.selectbox("Select a Mood Disorder", mood_disorders)
    
    # Use ChatGPT to generate an explanation for the selected mood disorder
    if selected_mood_disorder == "Depression":
        explanation = "Depression is a mood disorder characterized by persistent feelings of sadness, hopelessness, and a lack of interest or pleasure in daily activities."
    elif selected_mood_disorder == "Anxiety":
        explanation = "Anxiety is a condition where a person experiences excessive worry, fear, or nervousness. It can lead to physical symptoms like rapid heartbeat and sweating."
    # Add more mood disorders and explanations here
    
    st.write(explanation)

# Create a function to display information for Personality Disorders
def display_personality_disorders():
    st.title("Personality Disorders")
    
    # Define the list of common personality disorders
    personality_disorders = ["Borderline Personality Disorder", "Narcissistic Personality Disorder", "Antisocial Personality Disorder", "Obsessive-Compulsive Personality Disorder", "Avoidant Personality Disorder"]
    
    # Create a dropdown to select a personality disorder
    selected_personality_disorder = st.selectbox("Select a Personality Disorder", personality_disorders)
    
    # Use ChatGPT to generate an explanation for the selected personality disorder
    if selected_personality_disorder == "Borderline Personality Disorder":
        explanation = "Borderline Personality Disorder is a condition characterized by unstable relationships, self-image, and emotions. People with this disorder may have intense mood swings and difficulty regulating their emotions."
    elif selected_personality_disorder == "Narcissistic Personality Disorder":
        explanation = "Narcissistic Personality Disorder involves a pattern of grandiosity, a need for admiration, and a lack of empathy for others. Individuals with this disorder often have an inflated sense of self-importance."
    # Add more personality disorders and explanations here
    
    st.write(explanation)

# Create the main Streamlit app
def main():
    st.title("Mental Health Information App")
    
    # Create navigation options
    option = st.sidebar.selectbox("Select an Option", ["Home", "Mental Health Conditions", "Psychiatry Medications"])
    
    if option == "Home":
        st.write("Welcome to the Mental Health Information App. Use the sidebar to explore different topics.")
    elif option == "Mental Health Conditions":
        display_mental_health_conditions()
    elif option == "Psychiatry Medications":
        display_psychiatry_medications()

if __name__ == "__main__":
    main()
