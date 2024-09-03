import streamlit as st
import requests

st.title("RephraseFluxKI")

# Input text field
input_text = st.text_area("Enter text to paraphrase:")

# Paraphrase button
if st.button("Paraphrase"):
    if input_text:
        try:
            response = requests.post("http://localhost:8000/paraphrase/", json={"text": input_text})
            if response.status_code == 200:
                paraphrased_text = response.json().get("paraphrased_text", "No paraphrased text returned.")
                st.write("Here is your paraphrased text:")
                st.write(paraphrased_text)
            else:
                st.write("Error:", response.json().get("detail", "An error occurred"))
        except Exception as e:
            st.write(f"Error occurred: {e}")
    else:
        st.write("Please enter some text.")
