import json
import pickle

# Load website data
with open(
    "data/website_data.json",
    "r",
    encoding="utf-8"
) as f:

    documents = json.load(f)

chunks = []

chunk_size = 500

for doc in documents:

    content = doc["content"]

    for i in range(
        0,
        len(content),
        chunk_size
    ):

        chunk = content[
            i:i+chunk_size
        ]

        chunks.append(
            {
                "url": doc["url"],
                "title": doc["title"],
                "content": chunk
            }
        )

print(
    f"Total Chunks: {len(chunks)}"
)

with open(
    "vectorstore/chunks.pkl",
    "wb"
) as f:

    pickle.dump(
        chunks,
        f
    )

print("Chunks Saved")