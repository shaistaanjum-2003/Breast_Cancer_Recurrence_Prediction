# 🎗️ Breast Cancer Recurrence Prediction System

## 📋 Project Overview

A professional medical dashboard built with Streamlit that uses Machine Learning (Logistic Regression) to predict the likelihood of breast cancer recurrence based on clinical patient data.

**Model Accuracy:** 74.74%

---

## 🎯 Key Features

✅ **AI-Powered Predictions** - Logistic Regression model for cancer recurrence prediction  
✅ **Professional Medical UI** - Clinical-grade dashboard with modern design  
✅ **Real-time Analysis** - Instant prediction with confidence scores  
✅ **Visual Analytics** - Probability distribution pie charts and bar charts  
✅ **Patient Reporting** - Downloadable CSV reports  
✅ **Responsive Design** - Works seamlessly on desktop and mobile  
✅ **Clinical Data Input** - 9 carefully selected clinical features  

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
streamlit run app.py
```

The application will open at: `http://localhost:8501`

---

## 📊 UI Improvements Made

### 1. **Professional Medical Dashboard Design**
- Gradient backgrounds with medical color schemes (blues and clinical whites)
- Modern typography with proper font weights and sizes
- Professional spacing and alignment throughout

### 2. **Enhanced Sidebar**
- Dark blue gradient background (medical theme)
- Organized project information
- Clear system details and instructions
- Better visual hierarchy

### 3. **Charts Side-by-Side Layout**
- Pie chart showing probability distribution
- Bar chart showing confidence comparison
- Both charts visible simultaneously for better analysis

### 4. **Patient Summary & Download Report**
- Patient summary table on the left
- Download report section on the right
- Better visual organization with proper spacing

### 5. **Attractive Predict Button**
- Large, prominent blue gradient button
- Smooth hover effects with shadow transitions
- Better visual feedback on interaction
- Centered positioning for emphasis

### 6. **Improved Form Layout**
- Personal Information section (left column)
- Tumor Characteristics section (right column)
- Better field labels with icons
- Improved selectbox options with helpful descriptions

### 7. **Advanced Styling**
- Card-based design with hover effects
- Improved metric display with shadows and transitions
- Better color contrast for accessibility
- Professional alert boxes with gradients
- Enhanced table styling with hover effects

### 8. **Result Display**
- Success/Error alerts with gradient backgrounds
- Prominent confidence score display
- Better visual separation of prediction results

---

## 📈 Clinical Features

The model uses 9 key clinical features for prediction:

1. **Age Group** - Patient age category
2. **Menopause Status** - Menopausal state
3. **Tumor Size** - Size range in millimeters
4. **Involved Nodes** - Number of involved lymph nodes
5. **Node Caps** - Presence of capsular involvement
6. **Degree of Malignancy** - Tumor grade (1-3)
7. **Affected Breast** - Left or right breast
8. **Breast Quadrant** - Location within breast
9. **Radiation Therapy** - Whether irradiation was given

---

## 🔧 Project Structure

```
Breast_Cancer_Recurrence_Prediction/
├── app.py                    # Main Streamlit application (ENHANCED)
├── app_original.py          # Original version (backup)
├── app_enhanced.py          # Enhanced version (copy)
├── model.pkl                # Trained Logistic Regression model
├── le.pkl                   # Label encoder
├── oe.pkl                   # Ordinal encoder
├── fs.pkl                   # Feature selector
├── banner.webp              # Header banner image
├── breast-cancer.csv        # Dataset
├── requirements.txt         # Python dependencies
├── README.md                # This file
└── FeatureSelectionandmodelevalutaion.ipynb  # Model development notebook
```

---

## 📝 How to Use

1. **Fill Patient Details**
   - Select appropriate values for all 9 clinical features
   - Use the two-column layout for organized input

2. **Get Prediction**
   - Click the prominent "🔮 PREDICT RECURRENCE" button
   - Instant AI-powered prediction with confidence score

3. **View Analysis**
   - See probability distribution (pie chart)
   - View confidence comparison (bar chart)
   - Review patient summary table

4. **Download Report**
   - Click "📥 Download Report (CSV)" button
   - Get CSV file with all patient data and prediction

---

## 🎨 Color Scheme

**Primary Colors:**
- Primary Blue: #1e3a8a (Dark blue - professional)
- Accent Blue: #3b82f6 (Bright blue - interactive)
- Success Green: #22c55e (Positive predictions)
- Danger Red: #ef4444 (Risk indicators)
- Neutral Gray: #64748b (Text and borders)

**Gradients:**
- Main Background: #f5f7fa to #c3cfe2
- Button: #3b82f6 to #2563eb
- Sidebar: #1e3a8a to #1a365d

---

## 🤖 Machine Learning Model

- **Algorithm:** Logistic Regression
- **Accuracy:** 74.74%
- **Features Used:** 9 (selected via feature selection)
- **Framework:** Scikit-learn

---

## ⚠️ Clinical Disclaimer

⚠️ **IMPORTANT:** This system is designed as a clinical decision support tool and should NOT be used as the sole basis for medical diagnosis or treatment decisions. Always consult with qualified medical professionals for proper diagnosis and treatment recommendations.

---

## 👩‍💻 Developer Information

**Project Type:** MCA Project  
**Developed by:** Shaista Anjum  
**Technology Stack:** Streamlit, Python, Scikit-learn, Pandas, Matplotlib

---

## 📄 Changelog - UI Improvements

### Version 2.0 (Enhanced)
- ✨ Professional medical dashboard design
- 📊 Side-by-side chart layout
- 🎨 Improved color scheme with gradients
- 🎯 Attractive predict button with animations
- 📋 Side-by-side patient summary and report download
- 🎪 Enhanced sidebar with better styling
- 🔤 Improved typography and spacing
- 💳 Better card designs with hover effects
- 📱 Responsive design improvements
- 🏥 Clinical UI elements and better visual hierarchy

### Version 1.0 (Original)
- Basic Streamlit interface
- Functional prediction system
- Simple styling

---

## 🐛 Troubleshooting

**Issue:** Model files not found
- **Solution:** Ensure all `.pkl` files are in the same directory as `app.py`

**Issue:** Banner image not loading
- **Solution:** Verify `banner.webp` is in the project directory

**Issue:** Slow predictions
- **Solution:** This is normal for first prediction. Streamlit caches the model after loading

**Issue:** Styling not appearing correctly
- **Solution:** Clear browser cache and refresh the page

---

## 📞 Support

For issues or questions about this project, please contact:
- **Developer:** Shaista Anjum
- **Project:** MCA Course Project

---

## 📜 License

This project is developed for educational purposes as part of the MCA curriculum.

---

## 🙏 Acknowledgments

- Dataset sourced from breast cancer research data
- Built with Streamlit for interactive web interface
- Scikit-learn for machine learning model
- Professional medical dashboard UI design patterns

---

**Last Updated:** July 2026  
**Version:** 2.0 (Enhanced UI)
