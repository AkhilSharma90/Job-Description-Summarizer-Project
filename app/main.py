import streamlit as st
from summarizer import summarize_jd

# Set page title
st.set_page_config(page_title="Job Description Summarizer", page_icon="📜", layout="wide")

# Set title
st.title("Job Description Summarizer", anchor=False)
st.header("Summarize Job Description with AI", anchor=False)

with st.form("my_form"):
    # Input JD (pasted by user)
    jd = st.text_area("Paste the job description here", value="")

    def submit_form():
        st.write(summarize_jd(jd))   

    submit = st.form_submit_button(label="Summarize", on_click=submit_form)




