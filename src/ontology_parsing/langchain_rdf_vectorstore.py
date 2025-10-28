"""
Load documents into the vectorstore
"""
from typing import List
from uuid import uuid4
import langchain_core.documents
from langchain_ollama import OllamaEmbeddings
from definitions import ONTOLOGY_DIR
from src.ontology_parsing import langchain_rdf_parser


embeddings = OllamaEmbeddings(model="llama3.2")
#
# def load_into_qdrant():
#     from langchain_qdrant import QdrantVectorStore


def load_into_chroma(docs: List[langchain_core.documents.Document]):
    from langchain_chroma import Chroma
    vector_store = Chroma(
        collection_name="example_collection",
        embedding_function=embeddings,
        persist_directory="./chroma_langchain_db",
    )
    uuids = [str(uuid4()) for _ in range(len(docs))]
    vector_store.add_documents(documents=docs, ids=uuids)
    retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 1, "fetch_k": 5})
    return retriever



ds = langchain_rdf_parser.run(f"{ONTOLOGY_DIR}/VehicleParts.rdf")
r = load_into_chroma(ds)
print(r.invoke("Tell me about Advanced Driver Assist Systems attributes").pop())