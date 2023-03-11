
# Virtual AI Career Coach

This is a Streamlit app that uses the ChatGPT API from OpenAI to generate personalized career advice for the user based on their skills, experience, career goals, etc. The user is then able to download the response and their selections as a PDF.

# Web App
Click [Here](https://huggingface.co/spaces/Kaludi/Virtual-AI-Career-Coach_App "Here") To View This App Online!

![Image](https://github.com/Kaludii/OpenAI-Chatbot/blob/main/images/OpenAI-Chatbot.png?raw=true)

## Features

The Virtual AI Career Coach app has the following features:

-   **Personalized career advice:** The app uses the ChatGPT API from OpenAI to generate personalized career advice based on the user's skills, experience, education, career goals, industry, and salary expectations.
    
-   **PDF download:** The user can download the advice as a PDF for easy reference and sharing.
        
-   **Clear and user-friendly interface:** The app has a simple and intuitive interface that makes it easy for the user to input their information and receive advice.
    
-   **Customizable prompts:** The app allows the user to select from three different prompts depending on their career goals, and also allows them to customize the prompt if desired.

## Usage

To run the app, use the following command:

`streamlit run app.py` 

This will launch the app in your browser. You will need to enter your OpenAI API key in order to use the app. Once you have entered your API key, you can input your name, current skills, years of experience, education, career goals, industry, and salary expectations. Based on this input, the app will generate personalized career advice using the ChatGPT API.

You can then download the advice as a PDF by clicking the "Download as PDF" button.

## Requirements

-   Python 3.6 or higher
-   Streamlit
-   Requests
-   fpdf
-   reportlab

## Installation

1.  Clone the repository:

`git clone https://github.com/Kaludii/Virtual-AI-Career-Coach.git` 

2.  Install the required packages:
To run this app, you will need to install the following dependencies:

-   `streamlit`
-   `requests`
-   `fpdf`
-   `reportlab`

You can install them using pip:
`pip install streamlit requests fpdf reportlab` 

3.  Run the app:

`streamlit run app.py`
