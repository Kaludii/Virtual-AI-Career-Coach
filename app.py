import json
import streamlit as st
import requests
import io
import textwrap
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, portrait

# Define OpenAI API endpoint
API_URL = "https://api.openai.com/v1/chat/completions"

# Define OpenAI model ID
MODEL_ID = "gpt-3.5-turbo"

# Define function to generate chat completion
def generate_completion(api_key, message):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    data = {
        "model": MODEL_ID,
        "messages": [{"role": "user", "content": message}],
        "temperature": 0.7,
        "max_tokens": 300
    }
    response = requests.post(API_URL, headers=headers, data=json.dumps(data)).json()
    if "choices" in response:
        return response["choices"][0]["message"]["content"].strip()
        # total_tokens = response["usage"]["total_tokens"]
    else:
        raise ValueError("Invalid response from OpenAI API")

# Define function to generate PDF
def generate_pdf(name, skills, experience, option, education, industry, salary_expectations, response):
    buffer = io.BytesIO()

    # Create the PDF
    p = canvas.Canvas(buffer, pagesize=portrait(letter), bottomup=1)
    p.setFontSize(12)
    # Add title to the PDF
    p.drawString(250, 750, "Virtual AI Career Coach")
    # Write the user's selected options and the response to the PDF
    p.drawString(100, 720, f"Name: {name}")
    p.drawString(100, 690, f"Skills: {skills}")
    p.drawString(100, 660, f"Years of experience: {experience}")
    p.drawString(100, 630, f"What brings you here?: {option}")
    p.drawString(100, 600, f"Highest level of education: {education}")
    p.drawString(100, 570, f"Industry: {industry}")
    p.drawString(100, 540, f"Salary expectations: {salary_expectations}")

    # Split the response into multiple lines
    lines = textwrap.wrap(response, width=80)
    y = 480
    for line in lines:
        p.drawString(100, y, line)
        y -= 20

    # Save the PDF
    p.showPage()
    p.save()

    # Set the buffer's position to the beginning
    buffer.seek(0)

    return buffer




# Define Streamlit app
def app():
    st.set_page_config(page_title="Virtual AI Career Coach")
    st.title("Virtual AI Career Coach")
    st.write("Welcome to the Virtual AI Career Coach app! Here, you can get personalized career advice based on your skills, experience, career goals, etc. using the ChatGPT API. You are then able to download the responses and selections as a PDF to keep it with you.")

    api_key = st.text_input("OpenAI API key", type="password")
    if api_key == "":
        st.warning("Please enter your OpenAI API key to continue.")
    else:
        name = st.text_input("Name:")
        skills = st.text_input("Current Skills (comma-separated):")       
        # Add education input field
        education = st.text_input("Highest level of education (e.g. Bachelor's, Master's, Doctoral):")
        option = st.selectbox("What brings you here?", ["Job Search", "Career Advancement", "New Career Field"])
        # Add industry input field
        industry = st.text_input("Industry (e.g. healthcare, technology, finance):")
        # Add salary expectations input field
        salary_expectations = st.text_input("Salary expectations:")
        experience = st.slider("Years of experience:", min_value=0, max_value=50, value=0)
        submit_button = st.button("Submit")

        if submit_button:
            # Generate the response
            if option == "New Career Field":
                prompt = f"You are a professional career coach. My name is {name}. I have {experience} years of experience in {skills}, and my highest level of education is {education}. I am interested in exploring new job fields in {industry} with a salary expectation of {salary_expectations}. What advice for new jobs can you give me in less than 250 words?"
            elif option == "Job Search":
                prompt = f"You are a professional career coach. My name is {name}. I have {experience} years of experience in {skills}, and my highest level of education is {education}. I am Job searching in {industry} with a salary expectation of {salary_expectations}. What advice can you give me in less than 250 words?"
            elif option == "Career Advancement":
                prompt = f"You are a professional career coach. My name is {name}. I have {experience} years of experience in {skills}, and my highest level of education is {education}. I am looking for a career advancement in {industry} with a salary expectation of {salary_expectations}. What advice can you give me in less than 250 words?"

            response = generate_completion(api_key, prompt)
            st.write(response)
            # Add a button to download the user's selected options and the response as a PDF
            pdf_bytes = generate_pdf(name, skills, experience, option, education, industry, salary_expectations, response)
            st.download_button(label="Download as PDF", data=pdf_bytes, file_name="career_advice.pdf", mime="application/pdf",)


# Run the Streamlit app
if __name__ == "__main__":
    app()
