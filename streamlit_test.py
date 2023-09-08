import streamlit as st
import pandas as pd
import plotly.express as px

# Create a DataFrame to store daily feelings
feelings_data = pd.DataFrame(columns=["Date", "Feeling"])

# Define the Streamlit app
st.title("Daily Feelings Tracker")

# Input form to enter feelings
with st.form("Feeling Input"):
    date = st.date_input("Date", pd.to_datetime("today"))
    feeling = st.slider("Feeling (1 - 10)", 1, 10, 5)
    submit_button = st.form_submit_button("Submit")

# When the form is submitted, add the data to the DataFrame
if submit_button:
    feelings_data = feelings_data.append({"Date": date, "Feeling": feeling}, ignore_index=True)
    st.success("Feeling added successfully!")

# Display a table of recorded feelings
st.subheader("Recorded Feelings")
st.write(feelings_data)

# Visualize feelings over time using a line chart
if not feelings_data.empty:
    fig = px.line(feelings_data, x="Date", y="Feeling", title="Feeling Over Time")
    st.plotly_chart(fig)
else:
    st.warning("No feelings recorded yet.")


# Medication data
medications = {
    "Medication 1": {
        "Description": "Description of Medication 1",
        "Usage": "How Medication 1 is used",
        "Side Effects": "Common side effects of Medication 1",
    },
    "Medication 2": {
        "Description": "Description of Medication 2",
        "Usage": "How Medication 2 is used",
        "Side Effects": "Common side effects of Medication 2",
    },
    "Medication 3": {
        "Description": "Description of Medication 3",
        "Usage": "How Medication 3 is used",
        "Side Effects": "Common side effects of Medication 3",
    },
}

# Define the Streamlit app
st.title("Depression Medications Summary")

# Select a medication from the dropdown
selected_medication = st.selectbox("Select a Medication", list(medications.keys()))

# Display medication information
st.subheader(f"**{selected_medication}**")
st.write(f"**Description:** {medications[selected_medication]['Description']}")
st.write(f"**Usage:** {medications[selected_medication]['Usage']}")
st.write(f"**Common Side Effects:** {medications[selected_medication]['Side Effects']}")

# Add some additional information or resources
st.markdown("### Additional Information and Resources")
st.write("Here you can add more information, links, or resources related to depression medications.")

# Disclaimer
st.markdown("### Disclaimer")
st.write("This information is for educational purposes only. Please consult a healthcare professional for personalized advice on depression medications.")




#openAI key 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