import streamlit as st
import openai
from streamlit_chat import message


openai.api_key = st.secrets["OPENAI_API_KEY"]


def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    new_message = completions.choices[0].text
    return new_message


def gen_image(image_prompt):
    image_response = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size="1024x1024"
    )
    image_url = image_response['data'][0]['url']
    rendered = st.image(image_url, caption='Here is your Image')
    return rendered


st.title("chatBot : I'm a RazzBot using Streamlit and openAI")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input("You: ", "Hello, how are you?", key="input")
    return input_text


user_input = get_text()

if 'draw' in user_input.split() or 'picture' in user_input.split() or 'graph' in user_input.split():
    output = gen_image(user_input)
else:
    output = generate_response(user_input)
    # store the output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')


