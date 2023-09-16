import streamlit as st

# Define a dictionary with mental health conditions and their descriptions
mental_health_conditions = {
    "Mood Disorders": {
        "Depression": "A mood disorder characterized by persistent sadness and loss of interest in activities.",
        "Bipolar Disorder": "A mood disorder characterized by extreme mood swings, including mania and depression.",
    },
    "Personality Disorders": {
        "Borderline Personality Disorder": "A personality disorder characterized by unstable moods, relationships, and self-image.",
        "Narcissistic Personality Disorder": "A personality disorder characterized by an inflated sense of self-importance and lack of empathy for others.",
    },
}

# Define a dictionary with psychiatry medications and their descriptions
psychiatry_medications = {
    "Antidepressants": {
        "SSRIs (e.g., Prozac)": "SSRIs are a type of antidepressant that helps increase serotonin levels in the brain.",
        "SNRIs (e.g., Effexor)": "SNRIs are similar to SSRIs and also increase norepinephrine levels.",
    },
    "Antipsychotics": {
        "Risperidone": "An antipsychotic used to treat schizophrenia and bipolar disorder.",
        "Quetiapine": "An antipsychotic used to treat schizophrenia, bipolar disorder, and major depressive disorder.",
    },
}

# Streamlit UI
st.title("Mental Health Information App")

# Sidebar navigation
selected_category = st.sidebar.selectbox("Choose a Category", ["Home", "Mental Health Conditions", "Psychiatry Medications"])

if selected_category == "Home":
    st.write("Welcome to the Mental Health Information App!")

elif selected_category == "Mental Health Conditions":
    sub_category = st.sidebar.selectbox("Choose a Sub-Category", list(mental_health_conditions.keys()))
    sub_sub_category = st.sidebar.selectbox("Choose a Disorder", list(mental_health_conditions[sub_category].keys()))
    disorder_description = mental_health_conditions[sub_category][sub_sub_category]
    st.write(f"**{sub_sub_category}**: {disorder_description}")

elif selected_category == "Psychiatry Medications":
    medication_category = st.sidebar.selectbox("Choose a Medication Category", list(psychiatry_medications.keys()))
    selected_medication = st.sidebar.selectbox("Choose a Medication", list(psychiatry_medications[medication_category].keys()))
    medication_description = psychiatry_medications[medication_category][selected_medication]
    st.write(f"**{selected_medication}**: {medication_description}")
