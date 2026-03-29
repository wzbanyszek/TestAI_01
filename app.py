import streamlit as st
from config.languages import get_translations, load_dictionary

# Page configuration
st.set_page_config(
    page_title="Analytical Method Validation",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'language' not in st.session_state:
    st.session_state.language = "English"

if 'page' not in st.session_state:
    st.session_state.page = "Specificity"

# Sidebar - Language Selection
st.sidebar.markdown("---")
st.sidebar.markdown("### 🌍 Language Settings")
language = st.sidebar.selectbox(
    get_translations(st.session_state.language).get('language_label', 'Select Language'),
    options=["English", "Polish", "Russian"],
    index=["English", "Polish", "Russian"].index(st.session_state.language)
)
st.session_state.language = language

# Sidebar - Navigation
st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 Navigation")
pages = {
    "Specificity": "pages.specificity",
    "Accuracy": "pages.accuracy", 
    "Precision": "pages.precision",
    "Linearity": "pages.linearity",
    "Detectability": "pages.detectability",
    "Measurability": "pages.measurability",
    "Robustness": "pages.robustness"
}

selected_page = st.sidebar.radio(
    get_translations(st.session_state.language).get('nav_title', 'Navigation'),
    list(pages.keys())
)
st.session_state.page = selected_page

# Get translations
translations = get_translations(st.session_state.language)

# Main title
st.title(translations.get('title', 'Analytical Method Validation'))

# Page routing with dynamic imports
page_module_name = pages.get(selected_page)
if page_module_name:
    try:
        # Import the corresponding page module
        if selected_page == "Specificity":
            from pages import specificity
            specificity.render_specificity()
        elif selected_page == "Accuracy":
            from pages import accuracy
            accuracy.render_accuracy()
        elif selected_page == "Precision":
            from pages import precision
            precision.render_precision()
        elif selected_page == "Linearity":
            from pages import linearity
            linearity.render_linearity()
        elif selected_page == "Detectability":
            from pages import detectability
            detectability.render_detectability()
        elif selected_page == "Measurability":
            from pages import measurability
            measurability.render_measurability()
        elif selected_page == "Robustness":
            from pages import robustness
            robustness.render_robustness()
    except Exception as e:
        st.error(f"Error loading page: {str(e)}")
        st.info("Make sure all page modules are properly created.")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("### 📱 Application Info")
st.sidebar.info("🔬 Analytical Method Validation Application v1.0")
