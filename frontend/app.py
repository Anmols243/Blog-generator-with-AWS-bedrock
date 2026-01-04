import streamlit as st
import requests
import json

API_URL = st.secrets["API_URL"] 
st.set_page_config(page_title="AI Blog Generator", layout="centered")


st.title("📝 AI Blog Generator")
st.write("Powered by Amazon Bedrock + AWS Lambda")

topic = st.text_input("Enter a blog topic")

if st.button("Generate Blog"):
    if not topic:
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Generating blog... ⏳"):
            response = requests.post(API_URL, json={"blog_topic":topic})

            if response.status_code == 200:
                try:
                    data = response.json()
                    st.success(data["message"])

                    st.subheader("📖 Blog Content")
                    st.write(data["blog"]) 

                except Exception as e:
                    st.error(f"Error parsing response: {e}")
            else:
                st.error(f"Error: {response.text}") 
