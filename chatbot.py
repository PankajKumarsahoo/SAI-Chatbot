# import faiss
# import pickle
# import os
# import google.generativeai as genai

# from dotenv import load_dotenv
# from sentence_transformers import SentenceTransformer

# # ------------------------
# # Load API Key
# # ------------------------

# load_dotenv()

# genai.configure(
#     api_key=os.getenv("AIzaSyD95-T_dnmJ3PK_iu2O6_NytsDKTqvLtGg")
# )

# # ------------------------
# # Gemini Model
# # ------------------------

# model = genai.GenerativeModel(
#     "gemini-3.1-flash-lite"
# )

# # ------------------------
# # Embedding Model
# # ------------------------

# embedding_model = SentenceTransformer(
#     "all-MiniLM-L6-v2"
# )

# # ------------------------
# # Load FAISS Index
# # ------------------------

# index = faiss.read_index(
#     "vectorstore/faiss_index.bin"
# )

# with open(
#     "vectorstore/documents.pkl",
#     "rb"
# ) as f:

#     documents = pickle.load(f)

# # ------------------------
# # Chat Function
# # ------------------------

# def ask_bot(query):

#     try:

#         # Create query embedding
#         query_embedding = embedding_model.encode(
#             [query]
#         ).astype("float32")

#         # Search FAISS
#         distances, indices = index.search(
#             query_embedding,
#             10
#             )

#         # Build context
#         context = ""

#         for idx in indices[0]:

#             context += f"""
# Source URL:
# {documents[idx]['url']}

# Page Title:
# {documents[idx]['title']}

# Content:
# {documents[idx]['content']}

# ----------------------------------
# """

#         # Prompt
#         prompt = f"""
# You are an AI assistant for SAIntellect Solutions.

# Answer ONLY using the website information provided below.

# User Question:
# {query}

# Website Information:
# {context}
#  Instructions:

# 1. Answer ONLY the user's question.

# 2. Use only the website information.

# 3. If information is unavailable,
#    say exactly:
#    "I could not find that information on the website."

# 4. Do not provide unrelated services,
#    products or contact information.

# 5. Mention only source URLs
#    directly used in the answer.

# 6. Keep answers concise and professional.

# 7. If the user asks about careers,
#    search only career-related information.

# 8. If the user asks about training,
#    focus only on training information.

# 9. Never invent information.
# """

#         # Gemini Response
#         response = model.generate_content(
#             prompt
#         )

#         return response.text

#     except Exception as e:

#         return f"""
# Error:

# {str(e)}

# Possible Reasons:
# - Gemini quota exceeded
# - Invalid API key
# - Internet connection issue

# FAISS retrieval is working correctly.
# """


###---------------------------------------------------------------------------

import faiss
import pickle
import os
import google.generativeai as genai

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

# =====================================
# Load API Key
# =====================================
# load_dotenv()

# genai.configure(
#     api_key=os.getenv("GOOGLE_API_KEY")
# )

# =====================================
# Load API Key
# =====================================

import streamlit as st

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    api_key = st.secrets["GOOGLE_API_KEY"]

genai.configure(
    api_key=api_key
)
# =====================================
# Gemini Model
# =====================================

model = genai.GenerativeModel(
    "gemini-3.1-flash-lite"
)

# =====================================
# Embedding Model
# =====================================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# =====================================
# Load FAISS Index
# =====================================

index = faiss.read_index(
    "vectorstore/faiss_index.bin"
)

with open(
    "vectorstore/documents.pkl",
    "rb"
) as f:

    documents = pickle.load(f)

# =====================================
# Chat Function
# =====================================

def ask_bot(query):

    try:

        # =====================================
        # Greetings / Simple Responses
        # =====================================

        query_lower = query.lower().strip()

        if query_lower in [
            "thanks",
            "thank you",
            "ok",
            "okay",
            "good",
            "bye",
            "thankyou"
        ]:
            return (
                "You're welcome! 😊\n\n"
                "Let me know if you need any information "
                "about SAIntellect Solutions."
            )

        # =====================================
        # Create Query Embedding
        # =====================================

        query_embedding = embedding_model.encode(
            [query]
        ).astype("float32")

        # =====================================
        # Search FAISS
        # =====================================

        distances, indices = index.search(
            query_embedding,
            15
        )

        # =====================================
        # Build Context
        # =====================================

        context = ""

        source_urls = set()

        for idx in indices[0]:

            source_urls.add(
                documents[idx]["url"]
            )

            context += f"""
Source URL:
{documents[idx]['url']}

Page Title:
{documents[idx]['title']}

Content:
{documents[idx]['content']}

----------------------------------
"""

        # =====================================
        # Prompt
        # =====================================

        prompt = f"""
You are an AI assistant for SAIntellect Solutions.

Answer ONLY using the website information provided below.

User Question:
{query}

Website Information:
{context}

Instructions:

1. Answer ONLY the user's question.

2. Use only the website information.

3. If information is unavailable,
   say exactly:

   "I could not find that information on the website."

4. Do NOT provide unrelated services,
   products or contact information.

5. Keep answers concise,
   professional and accurate.

6. If the user asks about:
   - Services → explain services
   - Products → explain products
   - Careers → explain careers
   - Training → explain training
   - Contact → provide contact details

7. Never invent information.

8. Mention source URLs only if relevant.

9. Do not repeat the same information.

10. Answer in bullet points whenever possible.
"""

        # =====================================
        # Gemini Response
        # =====================================

        response = model.generate_content(
            prompt
        )

        answer = response.text

        # =====================================
        # Add Source URLs
        # =====================================

        # if source_urls:

        #     answer += "\n\n### Sources:\n"

        #     for url in sorted(source_urls):

        #         answer += f"- {url}\n"

        return answer

    except Exception as e:

        return f"""
❌ Error

{str(e)}

Possible Reasons:

• Gemini quota exceeded

• Invalid API key

• Internet connection issue

• Gemini service unavailable

FAISS retrieval is working correctly.
"""