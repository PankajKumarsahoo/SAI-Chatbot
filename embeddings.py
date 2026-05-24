# import json
# import pickle
# import faiss
# import numpy as np

# from sentence_transformers import SentenceTransformer

# # -----------------------------
# # Load JSON
# # -----------------------------

# with open(
#     "data/website_data.json",
#     "r",
#     encoding="utf-8"
# ) as f:

#     documents = json.load(f)

# # -----------------------------
# # Create Text Chunks
# # -----------------------------

# texts = []

# for doc in documents:

#     text = f"""
#     URL: {doc['url']}

#     Title: {doc['title']}

#     Content:
#     {doc['content']}
#     """

#     texts.append(text)

# print(f"Total Documents: {len(texts)}")

# # -----------------------------
# # Load Embedding Model
# # -----------------------------

# model = SentenceTransformer(
#     "all-MiniLM-L6-v2"
# )

# # -----------------------------
# # Generate Embeddings
# # -----------------------------

# embeddings = model.encode(
#     texts,
#     show_progress_bar=True
# )

# embeddings = np.array(
#     embeddings
# ).astype("float32")

# print(
#     "Embedding Shape:",
#     embeddings.shape
# )

# # -----------------------------
# # Create FAISS Index
# # -----------------------------

# index = faiss.IndexFlatL2(
#     embeddings.shape[1]
# )

# index.add(
#     embeddings
# )

# # -----------------------------
# # Save FAISS
# # -----------------------------

# faiss.write_index(
#     index,
#     "vectorstore/faiss_index.bin"
# )

# # -----------------------------
# # Save Documents
# # -----------------------------

# with open(
#     "vectorstore/documents.pkl",
#     "wb"
# ) as f:

#     pickle.dump(
#         documents,
#         f
#     )

# print("\nFAISS Index Saved")
# print("Documents Saved")




#_______________________________________________________________________________


import pickle
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

# -----------------------------
# Load Chunks
# -----------------------------

with open(
    "vectorstore/chunks.pkl",
    "rb"
) as f:

    chunks = pickle.load(f)

texts = []

for chunk in chunks:

    texts.append(
        f"""
        URL: {chunk['url']}

        Title: {chunk['title']}

        Content:
        {chunk['content']}
        """
    )

print(
    f"Total Chunks: {len(texts)}"
)

# -----------------------------
# Embedding Model
# -----------------------------

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# -----------------------------
# Create Embeddings
# -----------------------------

embeddings = model.encode(
    texts,
    show_progress_bar=True
)

embeddings = np.array(
    embeddings
).astype("float32")

print(
    "Embedding Shape:",
    embeddings.shape
)

# -----------------------------
# Create FAISS
# -----------------------------

index = faiss.IndexFlatL2(
    embeddings.shape[1]
)

index.add(
    embeddings
)

# -----------------------------
# Save FAISS
# -----------------------------

faiss.write_index(
    index,
    "vectorstore/faiss_index.bin"
)

# -----------------------------
# Save Chunks
# -----------------------------

with open(
    "vectorstore/documents.pkl",
    "wb"
) as f:

    pickle.dump(
        chunks,
        f
    )

print(
    "\nFAISS Saved"
)

print(
    "Documents Saved"
)