import streamlit as st
import requests

# Streamlit UI
st.set_page_config(page_title="AI Resume & Cover Letter Generator", layout="centered")
st.title("📄 AI Resume & Cover Letter Generator")
st.markdown("Generate a professional resume and cover letter with the power of AI!")

# Inputs
job_title = st.text_input("Job Title", placeholder="e.g., Data Analyst")
company_name = st.text_input("Company Name", placeholder="e.g., Google")
your_name = st.text_input("Your Name")
your_experience = st.text_area("Your Experience", placeholder="Summarize your background...")
skills = st.text_area("Skills", placeholder="e.g., Python, Data Analysis, SQL")

# Add your OpenRouter API key here securely
OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]

if st.button("Generate Resume & Cover Letter"):
    if not all([job_title, company_name, your_name, your_experience, skills]):
        st.warning("⚠️ Please fill in all the fields.")
    else:
        with st.spinner("Generating with OpenRouter..."):

            # Prompt
            prompt = f"""
            Write a professional resume summary and a cover letter for the following:

            Name: {your_name}
            Job Title: {job_title}
            Company: {company_name}
            Experience: {your_experience}
            Skills: {skills}

            First output the resume summary in markdown format.
            Then output the cover letter in markdown format.
            """

            # API Call
            try:
                url = "https://openrouter.ai/api/v1/chat/completions"
                headers = {
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json"
                }
                data = {
                    "model": "openai/gpt-3.5-turbo",  # You can change to "mistralai/mistral-7b-instruct", etc.
                    "messages": [
                        {"role": "system", "content": "You are a professional career coach and resume expert."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 1000
                }

                response = requests.post(url, headers=headers, json=data)
                response.raise_for_status()
                result = response.json()["choices"][0]["message"]["content"]
                st.markdown(result)

            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")





