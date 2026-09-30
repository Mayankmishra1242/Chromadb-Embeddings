# ChromaDB Embeddings

A small project that stores text in **ChromaDB** (a vector database), searches it by **meaning** using embeddings, and saves the data on disk so it is **persistent**.

## Project Structure

```
Chromadb-Embeddings/
├── app.py             # Creates the collection, adds documents, runs a search
├── data.py            # Reads back the saved data
├── requirements.txt   # chromadb, sentence-transformers
├── datafolder/        # Created automatically, ChromaDB saves data here
└── .gitignore
```

## Installation

```bash
pip install -r requirements.txt
```

`requirements.txt` contains:

```
chromadb
sentence-transformers
```

## How to Run

```bash
python app.py     # stores the documents and runs the search
python data.py    # reads back what was stored
```

Run `app.py` first, because `data.py` needs the collection that `app.py` creates. Run both from the same folder.

---

## 1. Embeddings

Computers work with numbers, not words. An **embedding** turns a piece of text into a list of numbers (a vector) that represents its **meaning**.

Texts with similar meaning get vectors that are close to each other. This lets us search by meaning instead of exact keywords.

In this project, the query is *"about artificial intelligence"*. It has no words in common with *"Python is used for AI and machine learning."*, but the meaning is close, so that document is returned.

## 2. sentence-transformers

`sentence-transformers` is a library of pre-trained models that convert sentences into embeddings. It is listed in `requirements.txt` because ChromaDB uses an embedding model to convert your documents and your query text into vectors.

In this project you only pass plain text to ChromaDB. The embeddings are created for you when you call `add()` and `query()`.

## 3. ChromaDB

ChromaDB is a vector database. It stores documents together with their embeddings and can find the documents most similar to a query.

| Term | Meaning |
|------|---------|
| Client | The connection to ChromaDB |
| Collection | A group of documents (like a table) |
| Document | The text you store |
| ID | A unique name for each document |

## 4. CRUD Operations Used

### Create: add documents

```python
collection.add(
    ids=["id1", "id2","id3","id4"],
    documents=["Python is used for AI and machine learning.",
    "Java is popular for enterprise applications.",
    "Cooking books teach different recipes.",
    "Data science involves analyzing data."],
)
```

- `ids` are unique names for each document.
- `documents` are the texts to store.
- The embeddings are generated automatically.

### Read: search by meaning

```python
result=collection.query(
    query_texts=[" about artificial intelligence"],
    n_results=2
)
print(result)
```

- `query_texts` is the text to search for.
- `n_results=2` returns the 2 closest documents.
- The most relevant results here are the Python/AI sentence and the data science sentence.

### Read: get everything stored

```python
print(collection.get())
```

This is in `data.py`. It returns all the stored data without doing a similarity search.

## 5. Persistence

```python
client=chromadb.PersistentClient(path="./datafolder")
```

`PersistentClient` saves the data in the `./datafolder` folder on disk, so it is still there after the program ends.

The in-memory version, `chromadb.Client()`, is commented out in the code. It does not save data, so everything is lost when the program stops.

Both `app.py` and `data.py` use the same `./datafolder` path. That is why `data.py` can read what `app.py` stored.

- `get_or_create_collection(name="my_collection")` in `app.py` opens the collection or creates it if it doesn't exist.
- `get_collection("my_collection")` in `data.py` only opens an existing collection, so `app.py` must be run first.

---

## Code

### app.py

```python
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
```

### data.py

```python
import chromadb

# client=chromadb.Client()

client= chromadb.PersistentClient(path="./datafolder")

collection= client.get_collection("my_collection")

print(collection.get())
```
