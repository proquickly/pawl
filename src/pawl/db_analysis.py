import chromadb
import pprint

print = pprint.pprint

chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(name="my_collection")

collection.upsert(
    documents=[
        "read a guide to touring vineyards in france",
        "watch a tv show about portugal",
        "visit alaska"
    ],
    ids=["id1", "id2", "id3"]
)

results = collection.query(
    query_texts=["see grapes harvested"],
    n_results=2
)

print(results)
