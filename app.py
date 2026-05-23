import streamlit as st
from groq import Groq
client=Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("🚀 The Career Architect")
st.markdown("**Stop guessing**. Tell us your background, and our AI will engineer a **ruthless**, step-by-step roadmap for your future.")
st.divider()

interests = st.text_input("What are your core interests? (e.g., AI, hardware, finance)")
studies = st.text_input("What are you currently studying?")

    
values = st.selectbox("What do you value most?", ["High Salary", "Work-Life Balance", "Entrepreneurship", "Social Impact"])
risk_tolerance = st.selectbox("Risk Tolerance?", ["Low - Secure jobs only", "Medium - Calculated risks", "High - Startup/Founder mentality"])
year = st.selectbox("What is your current academic stage?", ["12th Pass / Drop Year", "1st Year College", "2nd Year College ", "3rd Year College", "Final Year - Placements soon", "Recently Graduated"])  
if st.button("Generate My Roadmap"):
    if interests and studies:
        with st.spinner("Building your roadmap...."):
            prompt=f""" You are an elite career guidance expert for indian engineering students.
            Student_Profile: 
            Interests = {interests}, Currently_studying = {studies}, Value = {values}, Risk_tolerance = {risk_tolerance}, Year of study = {year}
            Based on this profile, directly give career guidance. Do not repeat the profile back but go thorugh each point in the profile
            Give_them:
            1. Top three career paths that suit them
            2. Why each path fits their profile
            3. Skills needed for each path
            4. Specific next steps to start this week
            After that generate a table with those 4 points as colums and the fill them with the guidance points
            Be specific and practical. No generic advice """
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown(response.choices[0].message.content)
else:
    st.error("Please fill in your interests and studies first. ")