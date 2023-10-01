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
    "Trauma & Stress-related Disorders": {
        "Post-Traumatic Stress Disorder (PTSD)": "A mental health condition that can develop after exposure to a traumatic event, such as abuse, accidents, or violence. Individuals with PTSD may experience distressing symptoms, including flashbacks, nightmares, and severe anxiety related to the trauma. Treatment often involves therapy, particularly trauma-focused therapies like cognitive behavioral therapy (CBT) and eye movement desensitization and reprocessing (EMDR), as well as antidepressant medication to alleviate symptoms and help individuals regain control over their lives.",
    },
}

# Define a dictionary with psychiatry medications and their descriptions
psychiatry_medications = {
    "Antidepressants": {
        "Fluoxetine (Prozac)": "Prozac is an antidepressant medication that falls into the category of selective serotonin reuptake inhibitors (SSRIs). It works by increasing the levels of serotonin in the brain, which is a chemical that helps regulate mood. Doctors often prescribe Prozac to treat conditions like depression, anxiety disorders, and obsessive-compulsive disorder (OCD), helping people feel better and manage their emotions more effectively.",
        "Escitalopram (Lexapro)": "Lexapro is an antidepressant belonging to the selective serotonin reuptake inhibitor (SSRI) category. It functions by adjusting the levels of serotonin in the brain, a chemical that plays a crucial role in regulating mood. Lexapro is commonly prescribed by healthcare professionals to help individuals with conditions such as depression and generalized anxiety disorder (GAD), assisting them in feeling better and reducing the impact of their emotional symptoms.",
        "Paroxetine (Paxil)": "Paxil is an antidepressant medication that belongs to the class of selective serotonin reuptake inhibitors (SSRIs). It works by increasing the levels of serotonin in the brain, which helps regulate mood. Doctors commonly prescribe Paxil to treat conditions such as depression, generalized anxiety disorder (GAD), social anxiety disorder (SAD), and post-traumatic stress disorder (PTSD), aiming to alleviate symptoms and improve overall mental well-being.",
        "Sertraline (Zoloft)": "Zoloft is a type of antidepressant known as a selective serotonin reuptake inhibitor (SSRI). It operates by elevating the levels of serotonin, a brain chemical that influences mood. Doctors frequently recommend Zoloft to manage conditions such as depression, anxiety disorders, and post-traumatic stress disorder (PTSD), aiming to improve emotional well-being and provide relief from distressing symptoms.",
        "Citalopram (Celexa)": "Celexa is an antidepressant medication classified as a selective serotonin reuptake inhibitor (SSRI). It functions by increasing the levels of serotonin in the brain, a neurotransmitter that influences mood. Medical professionals often prescribe Celexa to manage conditions like depression and anxiety disorders, assisting individuals in feeling better and reducing the impact of their emotional symptoms.",  
        "Duloxetine (Cymbalta)": "Cymbalta is an antidepressant medication classified as a serotonin-norepinephrine reuptake inhibitor (SNRI). It works by affecting the levels of both serotonin and norepinephrine in the brain, which play essential roles in regulating mood and pain perception. Doctors commonly prescribe Cymbalta to treat conditions such as depression, generalized anxiety disorder (GAD), fibromyalgia, and chronic pain disorders, helping individuals improve their mood and manage physical discomfort.",
        "Venlaxafine (Effexor)": "Effexor is an antidepressant categorized as a serotonin-norepinephrine reuptake inhibitor (SNRI). It works by increasing the levels of both serotonin and norepinephrine in the brain, two chemicals that affect mood and emotions. Doctors often prescribe Effexor to treat conditions like depression, generalized anxiety disorder (GAD), and social anxiety disorder (SAD), aiming to improve mood and alleviate symptoms of anxiety, providing individuals with a better overall sense of well-being.",
        "Bupropion (Wellbutrin)": "Wellbutrin is an atypical antidepressant that works by influencing the levels of certain neurotransmitters, particularly dopamine and norepinephrine, in the brain. It's often prescribed to manage conditions like depression and seasonal affective disorder (SAD). Unlike many other antidepressants, Wellbutrin does not primarily target serotonin. It can help improve mood and increase energy levels, making it a valuable option for individuals experiencing these symptoms.",
        "Mirtazapine (Remeron)": "Remeron is an antidepressant medication that belongs to the class of atypical antidepressants. It works by affecting various neurotransmitters in the brain, including serotonin and norepinephrine. Remeron is often prescribed to treat conditions like depression and is known for its tendency to increase appetite and promote weight gain, which can be helpful for individuals with weight loss or poor appetite due to depression or other conditions. It aims to improve mood and overall well-being.",
        "Trazadone (Desyrel)": "Desyrel is an antidepressant medication that primarily affects serotonin levels in the brain, aiding in mood regulation. Additionally, Desyrel acts as both a serotonin reuptake inhibitor (like many other antidepressants) and an antagonist at the histamine H1 receptor. This histamine-blocking activity can cause drowsiness, which is why Desyrel is sometimes prescribed to manage insomnia. It helps improve mood and can promote better sleep, making it a versatile treatment option for some individuals.",
    },
    "Antipsychotics": {
        "Haloperidol (Haldol)":
        "Risperidone (Risperdal)": "An antipsychotic used to treat schizophrenia and bipolar disorder.",
        "Quetiapine (Seroquel)": "An antipsychotic used to treat schizophrenia, bipolar disorder, and major depressive disorder.",
        "Olanzapine (Zyprexa)":
        "Clozapine (Clozaril)":
        "Aripiprazole (Abilify)":
        "Ziprasadone (Geodon)":
    },
     "Mood-Stabilizers": {
        "Lithium (Lithobid)": "An antipsychotic used to treat schizophrenia and bipolar disorder.",
        "Carbamazepine (Tegretol)": "An antipsychotic used to treat schizophrenia, bipolar disorder, and major depressive disorder.",
        "Lamotrigine (Lamictal)": 
     },
}

# Define a dictionary with mental health professionals and their descriptions
mental_health_Professionals = {
    "Psychiatrists": "Psychiatrists are medical doctors who specialize in diagnosing and treating mental illnesses. They can prescribe medications and provide therapy.",
    "Psychologists": "Psychologists are trained to assess and diagnose mental health conditions. They provide therapy and counseling but cannot prescribe medications.",
    "LSW Counselors/Therapists": "Licensed Social Workers (LSWs) provide counseling and therapy to individuals and families. They can help with various mental health issues and life challenges.",
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

elif selected_category == "Mental Health Professionals":
    # Display mental health professionals in a dropdown list on the main page
    selected_professional = st.selectbox("Choose a Mental Health Professional", list(mental_health_team.keys()))
    professional_description = mental_health_team[selected_professional]
    st.write(f"**{selected_professional}**: {professional_description}")
 
