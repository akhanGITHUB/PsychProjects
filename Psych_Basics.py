import streamlit as st

# Define a dictionary with mental health conditions and their descriptions
mental_health_conditions = {
    "Mood Disorders": {
        "Major Depressive Disorder": "A mood disorder characterized by persistent and deep feelings of sadness and a loss of interest or pleasure in daily activities. People with MDD may also experience changes in sleep and appetite, low energy, difficulty concentrating, and even thoughts of death or suicide. MDD is treatable through therapy, medication, or a combination of both, and seeking help from a mental health professional is crucial for effective management and recovery.",
        "Bipolar Disorder": "A mood disorder characterized by extreme mood swings, including periods of intense happiness and high energy (mania) and periods of deep sadness and low energy (depression). During manic episodes, individuals may feel overly confident and engage in risky behaviors, while depressive episodes involve persistent sadness and loss of interest. Management options often include mood-stabilizing medications and psychotherapy, which can help individuals balance their moods and lead more stable lives.",
        "Seasonal Affective Disorder": "A mood disorder that typically occurs seasonally, most commonly during the fall and winter months when there's less natural sunlight. People with SAD experience symptoms like persistent sadness, low energy, and changes in sleep and appetite. Light therapy, psychotherapy, and lifestyle adjustments, such as spending more time outdoors or using lightboxes, can help alleviate symptoms and improve mood during the darker months.",
        "Persistent Depressive Disorder (Dysthymia)": "A long-lasting form of depression where individuals experience chronic, low-level depressive symptoms for two years or more. These symptoms include persistent feelings of sadness, low energy, changes in appetite or sleep, and a general sense of hopelessness. Treatment options often include psychotherapy and sometimes medication, which can help manage symptoms and improve overall well-being over time.",
    },
    "Anxiety Disorders": {
        "Generalized Anxiety Disorder": "An anxiety disorder characterized by excessive and persistent worry about various aspects of life, like health, work, or relationships, even when there's no clear reason for concern. People with GAD often experience physical symptoms like restlessness, muscle tension, and difficulty concentrating. Effective management options include therapy, such as cognitive-behavioral therapy (CBT), and antidepressant medication, which can help individuals learn to cope with their worries and reduce anxiety.",
        "Social Anxiety Disorder": "Also known as Social Phobia, it is a common anxiety disorder marked by intense fear and avoidance of social situations due to a deep-seated fear of judgment or embarrassment by others. People with this disorder often feel extremely self-conscious and may worry about being scrutinized or humiliated in social settings. Effective treatment options include therapy, particularly cognitive-behavioral therapy (CBT), and in some cases, medication, which can help individuals build confidence and ease their social fears over time.",
        "Panic Disorder": "An anxiety disorder characterized by recurring and unexpected panic attacks, which are sudden and intense surges of fear or discomfort. These attacks often come out of the blue and may be accompanied by physical symptoms like a racing heart, shortness of breath, trembling, and sweating. Treatment options typically include therapy, such as cognitive-behavioral therapy (CBT), and antidepressant medication, which can help individuals learn to manage and reduce the frequency and intensity of panic attacks.",
        
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
    sub_category = st.sidebar.selectbox("Choose a mental health condition", list(mental_health_conditions.keys()))

    # Display disorders in a dropdown list on the main page
    selected_disorder = st.selectbox(f"Choose one from below", list(mental_health_conditions[sub_category].keys()))
    disorder_description = mental_health_conditions[sub_category][selected_disorder]
    st.write(f"**{selected_disorder}**: {disorder_description}")

elif selected_category == "Psychiatry Medications":
    medication_category = st.sidebar.selectbox("Choose category of medication", list(psychiatry_medications.keys()))

    # Display medications in a dropdown list on the main page
    selected_medication = st.selectbox(f"Choose a medication", list(psychiatry_medications[medication_category].keys()))
    medication_description = psychiatry_medications[medication_category][selected_medication]
    st.write(f"**{selected_medication}**: {medication_description}")
