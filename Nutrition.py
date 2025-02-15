import google.generativeai as genai
import streamlit as st

# Set up API key
API_KEY = "AIzaSyCEhbQkBn8knXe8b-GfmJuUYqeZ_fJRLqQ"
genai.configure(api_key=API_KEY)

# Function to get Gemini AI response
def get_nutrition_advice(query):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(query)
    return response.text

# Streamlit UI
st.title("🥗 Advanced Nutrition Advisor using Gemini AI")
st.write("Get personalized nutrition insights powered by AI.")


# User Input
user_input = st.text_area("Enter your nutrition-related question:")

if st.button("Get Advice"):
    if user_input:
        advice = get_nutrition_advice(user_input)
        st.subheader("🍎 AI-Powered Nutrition Advice")
        st.write(advice)
    else:
        st.warning("Please enter a query.")
