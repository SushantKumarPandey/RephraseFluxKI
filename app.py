import streamlit as st
from openai import OpenAI

st.title("A Poor Pirate's Chat")

query = st.text_area(label="Prompt:")

client = OpenAI(
    base_url="https://chat-large.llm.mylab.th-luebeck.dev/v1",
    api_key="-"
)

completion = client.chat.completions.create(
    model="tgi",
    messages=[
        {"role": "system", "content": "Du bist Klaus Störtebeker, ein deutscher Pirat. Fluche und antworte mit vielen 'Aye!' und 'Aaaargh!'." },
        {"role": "user", "content": f"{query}\nAntwort:"}
    ],
    stream=True,
    max_tokens=1024
)

# iterate and print stream
st.write("Response:")
for message in completion:
    if not message.choices[0].finish_reason:
        st.write(message.choices[0].delta.content, end='')