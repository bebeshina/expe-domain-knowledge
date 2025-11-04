"""
Load documents into the vectorstore
"""
from typing import List
from uuid import uuid4

import langchain_chroma
import langchain_core.documents
from humanfriendly.prompts import prompt_for_input
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from definitions import ONTOLOGY_DIR, VECTORSTORE_DIR
from src.ontology_parsing import langchain_rdf_parser


embeddings = OllamaEmbeddings(model="llama3.2")


def load_into_chroma(docs: List[langchain_core.documents.Document]):
    from langchain_chroma import Chroma
    uuids = [str(uuid4()) for _ in range(len(docs))]
    vector_store = Chroma(
        collection_name="example_collection",
        embedding_function=embeddings,
        persist_directory="./chroma_langchain_db",
    )

    vector_store.add_documents(documents=docs, ids=uuids)
    retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 1, "fetch_k": 5})
    return retriever



def run():
    vectordb = Chroma(persist_directory=f"{VECTORSTORE_DIR}", embedding_function=embeddings)
    # related_ontology_data = vectordb.similarity_search_with_vectors("Advanced Driver Assist System")
    test = vectordb.similarity_search_with_vectors("active parking assistance system")
    print(test)


run()