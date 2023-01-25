import streamlit as st
from chatgpt import Conversation

col1, col2 = st.columns([0.4, 2])

with col1:

    # Add a logo to the sidebar
    st.image("logo.png", width=150)

with col2:

    # Set the title
    st.title("ChatGPT Magic using Streamlit")


with st.form("gpt_form"):

    # Create a text input for the first field
    input1 = st.text_input("Enter whatever you like:")

    # Create a text input for the second field
    input2 = st.text_input("What else do you want?, still thinking?")

    # submitting the form here.
    submitted = st.form_submit_button("Submit 🤖")

if submitted:
    # st.write("slider", slider_val, "checkbox", checkbox_val)

    conversation = Conversation()
    st.write(
        conversation.chat(input1)
    )
    st.write(conversation.chat(input2))

    # The AI will forget it was speaking Portuguese
    conversation.reset()
    st.stop()