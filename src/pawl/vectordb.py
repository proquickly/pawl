# pip install chromadb
import chromadb
import pprint
from chromadb.config import Settings

RELOAD_DB = True

chroma_client = chromadb.PersistentClient(path="data/chroma.db",
                                          settings=Settings(
                                              anonymized_telemetry=False
                                          )
                                          )
collection = chroma_client.get_or_create_collection(name="chess")


def query_source_data():
    chess_moves = [
        "rook moves horizontally or vertically",
        "pawn moves one square forward",
        "knight moves two squares horizontally and one vertically",
        "knight moves two squares vertically and one horizontally",
        "bishop moves diagonally",
    ]
    return chess_moves


def load_data(results: list):
    collection.upsert(
        documents=results,
        ids=[f"id{num}" for num in range(1, len(results) + 1)]
    )


def run_query(query: str):
    results = collection.query(
        query_texts=[query],
        n_results=3
    )
    return results


def main():
    if RELOAD_DB:
        results = query_source_data()
        load_data(results)
    questions = [
        "which pieces move diagonally",
    ]
    for question in questions:
        findings = run_query(question)
        print(question)
        pprint.pprint(findings)
        print("-" * len(question), "\n")


if __name__ == "__main__":
    main()
