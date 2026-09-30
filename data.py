import chromadb

# client=chromadb.Client()
client= chromadb.PersistentClient(path="./datafolder")

collection= client.get_collection("my_collection")

print(collection.get())