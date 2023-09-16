import streamlit as st

# Create a function to display information for Mental Health Conditions
def display_mental_health_conditions():
    st.title("Mental Health Conditions")
    
    # Define the list of mental health condition categories
    mental_health_condition_categories = ["Mood Disorders", "Personality Disorders"]
    
    # Create a dropdown to select a mental health condition category
    selected_category = st.selectbox("Select a Mental Health Condition Category", mental_health_condition_categories)
    
    if selected_category == "Mood Disorders":
        display_mood_disorders()
    elif selected_category == "Personality Disorders":
        display_personality_disorders()

# Create a function to display information for Mood Disorders
def display_mood_disorders():
    st.subheader("Mood Disorders")
    
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
    st.subheader("Personality Disorders")
    
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

# Create a function to display information for Psychiatry Medications
def display_psychiatry_medications():
    st.title("Psychiatry Medications")
    
    # Define the list of common psychiatry medication categories
    psychiatry_medications = ["Antidepressants", "Antipsychotics"]
    
    # Create a dropdown to select a psychiatry medication category
    selected_medication_category = st.selectbox("Select a Psychiatry Medication Category", psychiatry_medications)
    
    if selected_medication_category == "Antidepressants":
        display_antidepressants()
    elif selected_medication_category == "Antipsychotics":
        display_antipsychotics()

# Create a function to display information for Antidepressant Medications
def display_antidepressants():
    st.subheader("Antidepressant Medications")
    
    # Define the list of common antidepressant medications
    antidepressants = ["Prozac (Fluoxetine)", "Zoloft (Sertraline)", "Lexapro (Escitalopram)", "Paxil (Paroxetine)", "Celexa (Citalopram)"]
    
    # Create a dropdown to select an antidepressant medication
    selected_antidepressant = st.selectbox("Select an Antidepressant Medication", antidepressants)
    
    # Use ChatGPT to generate an explanation for the selected antidepressant
    if selected_antidepressant == "Prozac (Fluoxetine)":
        explanation = "Prozac is an antidepressant medication commonly used to treat depression, anxiety, and obsessive-compulsive disorder (OCD). It works by increasing serotonin levels in the brain."
    elif selected_antidepressant == "Zoloft (Sertraline)":
        explanation = "Zoloft is an antidepressant medication used to treat depression, panic disorder, and social anxiety disorder. It helps balance serotonin levels in the brain."
    # Add more antidepressants and explanations here
    
    st.write(explanation)

# Create a function to display information for Antipsychotic Medications
def display_antipsychotics():
    st.subheader("Antipsychotic Medications")
    
    # Define the list of common antipsychotic medications
    antipsychotics = ["Risperdal (Risperidone)", "Abilify (Aripiprazole)", "Zyprexa (Olanzapine)", "Seroquel (Quetiapine)", "Haldol (Haloperidol)"]
    
    # Create a dropdown to select an antipsychotic medication
    selected_antipsychotic = st.selectbox("Select an Antipsychotic Medication", antipsychotics)
    
    # Use ChatGPT to generate an explanation for the selected antipsychotic
    if selected_antipsychotic == "Risperdal (Risperidone)":
        explanation = "Risperdal is an antipsychotic medication used to treat schizophrenia and bipolar disorder. It helps regulate dopamine levels in the brain."
    elif selected_antipsychotic == "Abilify (Aripiprazole)":
        explanation = "Abilify is an antipsychotic medication used to treat schizophrenia and bipolar disorder. It works by modulating dopamine and serotonin levels."
    # Add more antipsychotics and explanations here
    
    st.write(explanation)

# Create the main Streamlit app
def main():
    st.title("Mental Health Information App")
    
    # Create navigation options in the sidebar
    option = st.sidebar.selectbox("Select an Option", ["Home", "Mental Health Conditions", "Psychiatry Medications"])
    
    if option == "Home":
        st.write("Welcome to the Mental Health Information App. Use the sidebar to explore different topics.")
    elif option == "Mental Health Conditions":
        display_mental_health_conditions()
    elif option == "Psychiatry Medications":
        display_psychiatry_medications()

if __name__ == "__main__":
    main()
