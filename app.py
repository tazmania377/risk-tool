import streamlit as st


# Title
st.markdown('<h1 style="color: #2E5A88;">Risk Calculator Tool</h1>', unsafe_allow_html=True)

# Add methodology on the side in the sidebar
st.sidebar.markdown("""
### Methodology
This tool calculates risk scores based on the following criteria:

**Point 1**: We have used a matrix to assess suppliers, countries, and risks. Based on these, we have:
- **High Risk**: Score 1.0
- **Medium Risk**: Score 0.7
- **Low Risk**: Score 0.3

**Point 2**: We also assign specific weights to each criterion:
- **Severity Criteria (0.7)**:
    - Scale (0.3)
    - Scope (0.2)
    - Irremediability (0.2)
- **Probability Criteria (0.3)**:
    - Likelihood of Risk (0.3)

**Point 3**: Formulas:
- **Severity Score**: 
    - (Scale× Weight of Seriousness) + 
    - (Scope × Weight of Stakeholders) + 
    - (Irremediability × Weight of Irreversibility)
- **Probability Score**:
    - Likelihood of Risk × Weight of Likelihood
- **Combined Score**:
    - Severity Score + Probability Score
""")

# Custom Selectbox with pastel colors using HTML
st.markdown("""
    <style>
        .stSelectbox select {
            background-color: #FFDDDD;  /* Pastel red for High */
            color: #FF5733;
        }
        .stSelectbox:nth-child(2) select {
            background-color: #FFD9A1;  /* Pastel orange for Medium */
            color: #FF8C00;
        }
        .stSelectbox:nth-child(3) select {
            background-color: #D4F8E3;  /* Pastel green for Low */
            color: #32CD32;
        }
    </style>
""", unsafe_allow_html=True)

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

# Colorful display for Risk Classification based on Combined Score
if combined_score >= 0.7:
    risk_classification = "High Risk"
    risk_color = "#FFDDDD"  # Pastel red
elif combined_score >= 0.4:
    risk_classification = "Medium Risk"
    risk_color = "#FFD9A1"  # Pastel orange
else:
    risk_classification = "Low Risk"
    risk_color = "#D4F8E3"  # Pastel green

# Display Severity Score in a box with some space
st.markdown(f"""
    <div style="background-color: #F5F5F5; padding: 10px; border-radius: 10px;">
        <h3 style="font-weight: bold;">Severity Score: {severity:.2f}</h3>
    </div>
""", unsafe_allow_html=True)

# Adding some space
st.write("\n")

# Display Probability Score in a box with some space
st.markdown(f"""
    <div style="background-color: #F5F5F5; padding: 10px; border-radius: 10px;">
        <h3 style="font-weight: bold;">Probability Score: {probability:.2f}</h3>
    </div>
""", unsafe_allow_html=True)

# Adding some space
st.write("\n")

# Display Combined Risk Score in a box, with dynamic color based on risk
st.markdown(f"""
    <div style="background-color: {risk_color}; padding: 10px; border-radius: 10px;">
        <h3 style="font-weight: bold;">Combined Risk Score: {combined_score:.2f} ({risk_classification})</h3>
    </div>
""", unsafe_allow_html=True)

# Adding some space
st.write("\n")


