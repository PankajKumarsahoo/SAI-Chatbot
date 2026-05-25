# import streamlit as st
# from chatbot import ask_bot
# # --------------------------
# # Page Config
# # --------------------------

# st.set_page_config(
#     page_title="SAIntellect Chatbot",
#     page_icon="🤖",
#     layout="wide"
# )

# # --------------------------
# # Title
# # --------------------------

# st.title("🤖 SAIntellect Website Chatbot")

# st.markdown(
#     """
#     Ask anything about:

#     - Company Information
#     - Services
#     - Products
#     - Contact Details
#     - AI Solutions
#     - Training Programs
#     """
# )

# # --------------------------
# # Chat History
# # --------------------------

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for message in st.session_state.messages:

#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # --------------------------
# # Voice Input
# # --------------------------

# st.subheader("🎤 Voice Input")

# audio = mic_recorder(
#     start_prompt="🎙 Start Recording",
#     stop_prompt="⏹ Stop Recording",
#     key="recorder"
# )

# voice_query = None

# if audio:

#     voice_query = transcribe_audio(
#         audio["bytes"]
#     )

#     st.success(
#         f"You said: {voice_query}"
#     )

# # --------------------------
# # Text Input
# # --------------------------

# text_query = st.chat_input(
#     "Ask a question..."
# )

# # --------------------------
# # Final Query
# # --------------------------

# query = voice_query if voice_query else text_query

# # --------------------------
# # Process Query
# # --------------------------

# if query:

#     st.session_state.messages.append(
#         {
#             "role": "user",
#             "content": query
#         }
#     )

#     with st.chat_message("user"):
#         st.markdown(query)

#     with st.chat_message("assistant"):

#         with st.spinner(
#             "Searching website..."
#         ):

#             answer = ask_bot(query)

#             st.markdown(answer)

#             # Audio Output
#             audio_file = text_to_audio(
#                 answer
#             )

#             st.audio(audio_file)

#     st.session_state.messages.append(
#         {
#             "role": "assistant",
#             "content": answer
#         }
#     )

#_________________________________________________
import streamlit as st
from chatbot import ask_bot

# --------------------------
# Page Config
# --------------------------

st.set_page_config(
    page_title="SAIntellect Chatbot",
    page_icon="🤖",
    layout="wide"
)

# --------------------------
# Title
# --------------------------

st.title("🤖 SAIntellect Website Chatbot")

st.markdown(
    """
    Ask anything about:

    - Company Information
    - Services
    - Products
    - Contact Details
    - AI Solutions
    - Training Programs
    """
)

# --------------------------
# Chat History
# --------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------
# Text Input
# --------------------------

query = st.chat_input(
    "Ask a question..."
)

# --------------------------
# Process Query
# --------------------------

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):

        with st.spinner(
            "Searching website..."
        ):

            answer = ask_bot(query)

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )