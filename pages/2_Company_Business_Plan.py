import streamlit as st

st.set_page_config(page_title="Company Business Plan", layout="wide")

# (Optionnel) style léger cohérent avec Neat
C_FONCE = "#41072A"
C_WHITE = "#FFFFFF"
st.markdown(
    f"""
    <style>
      .stApp {{ background-color: {C_WHITE}; }}
      h1, h2, h3, h4 {{ color: {C_FONCE}; }}
    </style>
    """,
    unsafe_allow_html=True,
)

profile = st.session_state.get("profile")
if not profile:
    st.warning("Please select a profile first.")
    st.switch_page("pages/0_Home.py")

st.title("Company Business Plan")
st.caption("Coming soon — we’ll define the business assumptions and a robust BP model later.")

st.info(
    "This page is intentionally empty for now.\n\n"
    "Next steps (later): company selection → assumptions → projections → export."
)

