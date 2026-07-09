import streamlit as st
import joblib
import pandas as pd
import io
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Load saved model and preprocessing objects
model = joblib.load("model.pkl")
oe = joblib.load("oe.pkl")
le = joblib.load("le.pkl")
fs = joblib.load("fs.pkl")

# Page settings
st.set_page_config(
    page_title="Breast Cancer Recurrence Prediction",
    page_icon="🩺",
    layout="wide"
)

# Enhanced CSS Styling for Professional Medical Dashboard
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        min-height: 100vh;
    }
    
    /* Main container background */
    .main {
        background: transparent;
    }
    
    /* Main title */
    h1 {
        color: #1a3a52;
        text-align: center;
        font-weight: 700;
        font-size: 2.8rem;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    
    /* Sub headings */
    h2 {
        color: #2c5282;
        font-weight: 600;
        font-size: 1.8rem;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        color: #2d3748;
        font-weight: 600;
        font-size: 1.3rem;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e3a8a 0%, #1a365d 100%);
        border-right: 3px solid #1e40af;
    }
    
    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: #e2e8f0;
    }
    
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #f0f9ff;
        font-weight: 700;
    }
    
    section[data-testid="stSidebar"] .css-1d391kg {
        color: #cbd5e1;
    }
    
    /* Info boxes in sidebar */
    section[data-testid="stSidebar"] [data-testid="stAlert"] {
        background-color: rgba(59, 130, 246, 0.15);
        border: 2px solid #3b82f6;
        border-radius: 10px;
        color: #f0f9ff;
    }
    
    /* Sidebar dividers */
    section[data-testid="stSidebar"] hr {
        border-color: #3b82f6;
        opacity: 0.3;
    }
    
    /* Metric cards - Medical Dashboard Style */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 2px solid #e2e8f0;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 20px rgba(15, 23, 42, 0.08), 0 1px 3px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    div[data-testid="stMetric"]:hover {
        box-shadow: 0 8px 30px rgba(15, 23, 42, 0.12);
        border-color: #cbd5e1;
        transform: translateY(-2px);
    }
    
    div[data-testid="stMetric"] > div:first-child {
        color: #475569;
        font-weight: 600;
        font-size: 0.95rem;
    }
    
    div[data-testid="stMetric"] > div:nth-child(2) {
        color: #1e3a8a;
        font-weight: 700;
        font-size: 1.8rem;
    }
    
    /* Predict button - Attractive and prominent */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        border-radius: 12px;
        height: 55px;
        padding: 12px 30px;
        font-size: 18px;
        font-weight: 700;
        letter-spacing: 0.5px;
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
        transition: all 0.3s ease;
        width: 100%;
        text-transform: uppercase;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        box-shadow: 0 10px 30px rgba(59, 130, 246, 0.5);
        transform: translateY(-2px);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Info/Alert boxes */
    div[data-testid="stAlert"] {
        border-radius: 12px;
        border-left: 5px solid #3b82f6;
        background-color: rgba(219, 234, 254, 0.5);
        color: #1e3a8a;
        font-weight: 500;
    }
    
    /* Success alert */
    .stAlert > div:has-text(✅) {
        background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
        border-left-color: #22c55e;
        color: #165e4e;
    }
    
    /* Error alert */
    .stAlert > div:has-text(⚠️) {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border-left-color: #ef4444;
        color: #7f1d1d;
    }
    
    /* Cards/Containers */
    .stContainer {
        background: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }
    
    /* Tables */
    table {
        border-radius: 10px;
        border-collapse: collapse;
    }
    
    table thead {
        background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
        color: white;
        font-weight: 600;
    }
    
    table tbody tr {
        border-bottom: 1px solid #e2e8f0;
        transition: background-color 0.2s ease;
    }
    
    table tbody tr:hover {
        background-color: #f0f9ff;
    }
    
    table td {
        padding: 12px 15px;
        color: #334155;
    }
    
    /* Input fields */
    .stSelectbox label,
    .stNumberInput label {
        color: #334155;
        font-weight: 600;
        font-size: 0.95rem;
    }
    
    /* Progress bar */
    .stProgress > div > div {
        background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
        border-radius: 10px;
    }
    
    /* Divider */
    hr {
        border-color: #cbd5e1;
        margin: 2rem 0;
    }
    
    /* Caption */
    .stCaption {
        color: #64748b;
        font-weight: 500;
    }
    
    /* Column spacing */
    .element-container {
        margin-bottom: 1rem;
    }
    
    /* Form labels */
    label {
        color: #1e293b !important;
    }
    
</style>
""", unsafe_allow_html=True)

# Banner
image = Image.open("banner.webp")
st.image(image, use_container_width=True)

# Sidebar
with st.sidebar:
    st.markdown("---")
    st.markdown("## 🩺 System Information")
    st.markdown("""
    **Project Type:** MCA Project
    
    **Algorithm:** Logistic Regression
    
    **Model Accuracy:** 74.74%
    
    **Framework:** Streamlit + Scikit-learn
    
    **Developed by:** Shaista Anjum
    """)
    st.markdown("---")
    st.info("📋 Fill all patient clinical details in the form and click **Predict** to get the recurrence prediction.")
    st.markdown("---")
    st.markdown("### 📊 About This System")
    st.markdown("""
    This ML-powered application predicts the likelihood of breast cancer recurrence based on clinical parameters.
    """)

# Main Dashboard
st.title("🎗️ Breast Cancer Recurrence Prediction")
st.markdown("### 🩺 AI-Powered Clinical Decision Support System")

# Dashboard Summary Section
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="🎯 Accuracy", value="74.74%")

with col2:
    st.metric(label="🤖 Algorithm", value="Logistic Regression")

with col3:
    st.metric(label="📋 Features", value="9")

with col4:
    st.metric(label="💻 Framework", value="Streamlit")

st.markdown("---")

# Information Box
st.info("""
### 📖 How to Use
This application predicts breast cancer recurrence based on clinical features. 
Enter patient details in the form below and click **Predict** to receive an AI-based prediction with confidence scores.
""")

# Patient Input Form
st.markdown("### 👨‍⚕️ Patient Clinical Details")

# Input fields in two columns for better organization
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Personal Information")
    age = st.selectbox(
        "👤 Age Group",
        ["20-29", "30-39", "40-49", "50-59", "60-69", "70-79"],
        key="age"
    )
    
    menopause = st.selectbox(
        "🩺 Menopause Status",
        ["lt40", "ge40", "premeno"],
        format_func=lambda x: {"lt40": "Less than 40", "ge40": "Greater than 40", "premeno": "Premenopausal"}[x],
        key="menopause"
    )
    
    tumor_size = st.selectbox(
        "📏 Tumor Size (mm)",
        ["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59"],
        key="tumor_size"
    )
    
    inv_nodes = st.selectbox(
        "🔬 Involved Nodes",
        ["0-2", "3-5", "6-8", "9-11", "12-14", "15-17", "18-20", "21-23", "24-26", "27-29", "30-32", "33-35", "36-39"],
        key="inv_nodes"
    )
    
    node_caps = st.selectbox(
        "💊 Node Caps",
        ["yes", "no"],
        format_func=lambda x: "Yes" if x == "yes" else "No",
        key="node_caps"
    )

with col2:
    st.markdown("#### Tumor Characteristics")
    deg_malig = st.selectbox(
        "⚠️ Degree of Malignancy",
        ["1", "2", "3"],
        format_func=lambda x: f"Grade {x}",
        key="deg_malig"
    )
    
    breast = st.selectbox(
        "🏥 Affected Breast",
        ["left", "right"],
        format_func=lambda x: "Left Breast" if x == "left" else "Right Breast",
        key="breast"
    )
    
    breast_quad = st.selectbox(
        "📍 Breast Quadrant",
        ["left_up", "left_low", "right_up", "right_low", "central"],
        format_func=lambda x: {
            "left_up": "Left Upper",
            "left_low": "Left Lower",
            "right_up": "Right Upper",
            "right_low": "Right Lower",
            "central": "Central"
        }[x],
        key="breast_quad"
    )
    
    irradiat = st.selectbox(
        "☢️ Radiation Therapy",
        ["yes", "no"],
        format_func=lambda x: "Yes" if x == "yes" else "No",
        key="irradiat"
    )

st.markdown("---")

# Predict Button - Prominent and Centered
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    predict_button = st.button("🔮 PREDICT RECURRENCE", key="predict1", use_container_width=True)

st.markdown("---")

# Prediction Logic
if predict_button:
    # Prepare data for prediction
    new_data = [[
        f"'{age}'",
        f"'{menopause}'",
        f"'{tumor_size}'",
        f"'{inv_nodes}'",
        f"'{node_caps}'",
        f"'{deg_malig}'",
        f"'{breast}'",
        f"'{breast_quad}'",
        f"'{irradiat}'"
    ]]
    
    # Transform and predict
    new_data_enc = oe.transform(new_data)
    new_data_fs = fs.transform(new_data_enc)
    
    prediction = model.predict(new_data_fs)
    probability = model.predict_proba(new_data_fs)
    result = le.inverse_transform(prediction)
    
    # Prediction Results Section
    st.markdown("### 📊 Prediction Results")
    
    # Result Alert
    if result[0] == "no-recurrence-events":
        st.success("✅ **NEGATIVE** - No Recurrence Expected", icon="✅")
        confidence_score = probability[0][0] * 100
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%); 
                    padding: 20px; border-radius: 12px; border-left: 5px solid #22c55e;'>
            <h3 style='color: #165e4e; margin: 0;'>Confidence Score</h3>
            <p style='color: #065f46; font-size: 1.5rem; font-weight: 700; margin: 10px 0 0 0;'>{confidence_score:.2f}%</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("⚠️ **POSITIVE** - Recurrence Risk Detected", icon="⚠️")
        confidence_score = probability[0][1] * 100
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%); 
                    padding: 20px; border-radius: 12px; border-left: 5px solid #ef4444;'>
            <h3 style='color: #7f1d1d; margin: 0;'>Confidence Score</h3>
            <p style='color: #991b1b; font-size: 1.5rem; font-weight: 700; margin: 10px 0 0 0;'>{confidence_score:.2f}%</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Charts Section - Side by Side
    st.markdown("### 📈 Prediction Analysis")
    
    chart_col1, chart_col2 = st.columns(2)
    
    # Pie Chart
    with chart_col1:
        st.markdown("#### Probability Distribution")
        st.markdown("""
        <div style="
        background:white;
        padding:20px;
        border-radius:15px;
        box-shadow:0px 4px 12px rgba(0,0,0,0.12);
        margin-bottom:15px;
        ">
        """, unsafe_allow_html=True)
        labels = ["No Recurrence", "Recurrence"]
        sizes = [probability[0][0], probability[0][1]]
        colors = ['#FBCFE8', '#DB2777']
        
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors,
               textprops={'fontsize': 12, 'weight': 'bold'})
        ax.axis("equal")
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Bar Chart
    with chart_col2:
        st.markdown("#### Confidence Comparison")
        st.markdown("""
        <div style="
        background:white;
        padding:20px;
        border-radius:15px;
        box-shadow:0px 4px 12px rgba(0,0,0,0.12);
        margin-bottom:15px;
        ">
        """, unsafe_allow_html=True)
        chart_data = pd.DataFrame({
            "Prediction": ["No Recurrence", "Recurrence"],
            "Probability": [
                probability[0][0] * 100,
                probability[0][1] * 100
            ]
        })
        
        fig, ax = plt.subplots(figsize=(8, 6))
        bars = ax.bar(chart_data["Prediction"], chart_data["Probability"], 
                     color=['#FBCFE8', '#DB2777'], width=0.6, edgecolor='black', linewidth=1.5)
        ax.set_ylabel("Probability (%)", fontweight='bold', fontsize=12)
        ax.set_ylim(0, 100)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}%', ha='center', va='bottom', fontweight='bold', fontsize=11)
        
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Patient Summary and Download Report - Side by Side
    st.markdown("### 📋 Report & Summary")
    
    report_col1, report_col2 = st.columns(2)
    
    # Patient Summary Table
    with report_col1:
        st.markdown("#### Patient Summary")
        summary = pd.DataFrame({
            "Feature": [
                "Age",
                "Menopause",
                "Tumor Size",
                "Inv Nodes",
                "Node Caps",
                "Degree",
                "Breast",
                "Breast Quadrant",
                "Irradiat"
            ],
            "Value": [
                age,
                menopause,
                tumor_size,
                inv_nodes,
                node_caps,
                deg_malig,
                breast,
                breast_quad,
                irradiat
            ]
        })
        st.table(summary)
    
    # Download Report
    with report_col2:
        st.markdown("#### Export Report")
        
        report = pd.DataFrame({
            "Feature": [
                "Age",
                "Menopause",
                "Tumor Size",
                "Inv Nodes",
                "Node Caps",
                "Degree",
                "Breast",
                "Breast Quadrant",
                "Irradiat",
                "Prediction",
                "Confidence"
            ],
            "Value": [
                age,
                menopause,
                tumor_size,
                inv_nodes,
                node_caps,
                deg_malig,
                breast,
                breast_quad,
                irradiat,
                result[0],
                f"{confidence_score:.2f}%"
            ]
        })
        
        csv = report.to_csv(index=False).encode("utf-8")
        
        st.markdown("**Download the patient report in CSV format**")
        st.download_button(
            label="📥 Download Report (CSV)",
            data=csv,
            file_name="Breast_Cancer_Report.csv",
            mime="text/csv",
            use_container_width=True
        )
        
        st.markdown("---")
        st.info("""
        **📌 Report Notes:**
        - This report contains patient clinical data and AI prediction
        - Confidence score indicates prediction reliability
        - Always consult medical professionals for final diagnosis
        """)

st.markdown("---")
st.markdown("---")
st.caption("© 2026 Breast Cancer Recurrence Prediction System | MCA Project by Shaista Anjum")
