import streamlit as st

# Title and Description
st.title("Risk Assessment Tool")
st.write("This tool calculates the severity, probability, and combined risk score based on your inputs.")

# User Inputs: Scale (A), Scope (B), Irremediability (C), Likelihood (D)
scale = st.selectbox("Select Scale (A):", ["High", "Medium", "Low"])
scope = st.selectbox("Select Scope (B):", ["High", "Medium", "Low"])
irremediability = st.selectbox("Select Irremediability (C):", ["High", "Medium", "Low"])
likelihood = st.selectbox("Select Likelihood (D):", ["High", "Medium", "Low"])

# Mapping for High, Medium, Low to numerical values
score_map = {
    "High": 1,
    "Medium": 0.7,
    "Low": 0.3
}

# Severity Formula Calculation (based on Scale, Scope, Irremediability)
severity = (
    (score_map[scale] * 0.3) + 
    (score_map[scope] * 0.2) + 
    (score_map[irremediability] * 0.2)
)

# Probability Formula Calculation (based on Likelihood)
probability = score_map[likelihood] * 0.3

# Combined Score Calculation (Severity + Probability)
combined_score = severity + probability

# Displaying the Results
st.subheader("Results")
st.write(f"**Severity Score:** {severity:.2f}")
st.write(f"**Probability Score:** {probability:.2f}")
st.write(f"**Combined Risk Score (Severity + Probability):** {combined_score:.2f}")
