import streamlit as st

st.set_page_config(
    page_title="Menu Inicial",
    page_icon="📋",
    layout="centered",  # deixa de ser "wide"
    initial_sidebar_state="expanded"
)

# TÍTULO
st.markdown("<h1>Portal do Colaborador</h1>",unsafe_allow_html=True)

st.markdown("Portal para compartilhamento de comunicados, informações e solicitações diversas.",unsafe_allow_html=True)

st.markdown("""
### Aqui você pode:

- 📰 **COMUNICADOS:** Compartilhamento de informações, procedimentos e reminders.<br><br><br>

Nos próximos dias novas funcionalidades serão disponibilizadas
""", unsafe_allow_html=True)




