import streamlit as st

# Main configuration settings
# Add your config settings here

# Language management system
from config.languages import get_translations

# Page titles
st.title(get_translations()['title'])

# Language selection
language = st.selectbox(get_translations()['language_select_label'], options=["English", "Polish", "Russian"])
st.session_state.language = language

# Main navigation
pages = ["Specificity", "Accuracy", "Precision", "Linearity", "Detectability", "Measurability", "Robustness"]
selected_page = st.sidebar.selectbox("Select Page", pages)

# Page routing
if selected_page == "Specificity":
    import pages.specificity
elif selected_page == "Accuracy":
    import pages.accuracy
elif selected_page == "Precision":
    import pages.precision
elif selected_page == "Linearity":
    import pages.linearity
elif selected_page == "Detectability":
    import pages.detectability
elif selected_page == "Measurability":
    import pages.measurability
else:
    import pages.robustness
