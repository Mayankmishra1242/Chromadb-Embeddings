import chromadb
# client = chromadb.Client()

client=chromadb.PersistentClient(path="./datafolder")

collection = client.get_or_create_collection(
    name="my_collection"
)

print(collection.name)

# Add documents with embeddings
collection.add(
    ids=["id1", "id2","id3","id4"],
    documents=["Python is used for AI and machine learning.",
        "Java is popular for enterprise applications.",
        "Cooking books teach different recipes.",
        "Data science involves analyzing data."],
)

result=collection.query(
    query_texts=[" about artificial intelligence"],
    n_results=2
)

print(result)