# import ollama

# ollam_ver = ollama.list()

# while(True):
#     user_input = input("Enter your topic: ")
#     res = ollama.chat(
#         model="llama3.2",
#         messages = [
#             {"role": "user", "content": user_input}
#         ]
#     )
#     print(res["message"]["content"])


import streamlit as st
import replicate
import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-flash")

# App title
st.set_page_config(
    page_title="Koduesi AI",
    layout="centered",
    initial_sidebar_state="collapsed",
    page_icon="👨‍💻",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)

# Replicate Credentials
with st.sidebar:
    st.title('💬 Asisteni yt i kodimit\n [**Koduesi Ai**](/)')
    st.markdown("""
        <ul type="none">
            <li><a href="https://i-code.al">i-code.al</a></li>
            <li><a href="https://i-code.al/academy">Akademia</a></li>
            <li><a href="https://i-code.al/news">News</a></li>
        </ul>
    """, unsafe_allow_html=True)

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Si mund t'ju ndihmoj sot?"}]


# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Si mund t'ju ndihmoj sot?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)


# User-provided prompt
if prompt := st.chat_input("Enter something: "):
    st.session_state.messages.append({"role": "user", "content": prompt, "avatar": "🐱‍👤"})
    with st.chat_message("user", avatar="user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Kuduesi AI po mendohet..."):
            response = model.generate_content(prompt)._result.candidates[0].content.parts[0]
            placeholder = st.empty()
            full_response = ''
            for item in response.text:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response, "avatar": "💡"}
    st.session_state.messages.append(message)
######
######
