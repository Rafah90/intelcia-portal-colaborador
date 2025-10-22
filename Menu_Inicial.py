import streamlit as st

st.set_page_config(
    page_title="Menu Inicial",
    page_icon="📋",
    layout="centered",  # deixa de ser "wide"
    initial_sidebar_state="expanded"
)

# TÍTULO
st.markdown("<h1>Portal do Colaborador</h1>",unsafe_allow_html=True)

st.markdown("Portal para compartilhamento de informações e solicitações diversas.",unsafe_allow_html=True)

st.markdown("""
### Aqui você pode:

- 📰 **NOTÍCIAS:** Compartilhamento de comunicados de procedimentos e reminders.  


Nos próximos dias novas funcionalidades serão disponibilizadas
""")


