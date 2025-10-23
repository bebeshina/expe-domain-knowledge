from typing import Sequence

import ollama
from rdflib import Graph
from src.relation_extraction import loader
from definitions import ONTOLOGY_DIR


def get_ontology_context():
    vectorstore = Qdrant.from_documents(
        splits,
        flag_embeddings,
        collection_name="ontologies",
        location=":memory:",
        # path="./data/qdrant",
        # Run Qdrant as a service for production use:
        # url="http://localhost:6333",
        # prefer_grpc=True,
    )

def test(text):
    g = Graph()
    ontology = g.parse(f"{ONTOLOGY_DIR}/VehicleSignals.rdf")
    print(ontology.all_nodes())
    # prompt = "Express connections with the ontology schema if any. Otherwise, return 'None'"
    # print("text>>>", text)
    # response = ollama.generate(model='llama3.2',
    #                            prompt=prompt,
    #                            context=Sequence(type=is_instance_of, input_value=ontology, input_type_Graph),
    #                            # Sequence [type=is_instance_of, input_value=<Graph identifier=Na07d7d... 'rdflib.graph.Graph'>)>, input_type=Graph]
    #                            )
    # print("response>>", response["response"])
    # output = response["response"]
    return ""
    # return output


def run():
    df = loader.get_texts()[:20]
    df["isa"] = df["text"].apply(test)
    # print(df["isa"])


run()


