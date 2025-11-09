import os
from typing import List
import networkx as nx
from click import Tuple
from rdflib import Graph, RDFS, SKOS
from definitions import ONTOLOGY_DIR
import matplotlib.pyplot as plt


def plot_graph(G: nx.Graph):
    fig = plt.figure("", figsize=(10, 8))
    axgrid = fig.add_gridspec(4, 4)
    ax0 = fig.add_subplot(axgrid[0:3, :])
    pos = nx.multipartite_layout(G)
    nx.draw_networkx(G, ax=ax0, pos=pos, node_size=20)
    ax0.set_title("Ontology View")
    ax0.set_axis_off()
    plt.show()


def run_nx_graph(nodes, edges):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    # plot_graph(G)


def get_label_approximate_graph(g:Graph):
    nodes = set()
    edges = []
    blank_nodes = 0
    labeled_nodes = 0
    for subj, pred, obj in g:
        node_label = g.value(subject=subj, predicate=RDFS.label)
        parent =  g.value(subject=subj, predicate=RDFS.subClassOf)
        parent_label = g.value(subject=parent, predicate=RDFS.label)
        if parent_label:
            print(f"{node_label}, {parent_label}")
            nodes.add(node_label)
            edges.append((node_label, parent_label))
            labeled_nodes += 1
        else:
            blank_nodes += 1
    print("blank nodes %s" % blank_nodes, f"rate {blank_nodes/(blank_nodes + labeled_nodes)}")
    return edges


def get_definition_approximate_graph(g: Graph) -> List[Tuple]:
    edge_list = []
    for subj, pred, obj in g:
        n = str(subj).split("/")[-1]
        node_label = g.value(subject=subj, predicate=RDFS.label)
        node_definition =  g.value(subject=subj, predicate=SKOS.definition)
        parent =  g.value(subject=subj, predicate=RDFS.subClassOf)
        parent_label = g.value(subject=parent, predicate=RDFS.label)
        parent_definition = g.value(subject=parent, predicate=SKOS.definition)
        if parent_label:
            edge_list.extend([(node_label, node_definition),
                             (parent_label, parent_definition),
                              (node_definition, parent_definition)])
    return edge_list



def translate_definitions():
    print("LLM or seq2seq translation process")


def propose_labels():
    print("Based on definitions propose labels")


def serialize(g: Graph, destination):
    g.serialize(destination=destination, format="json-ld")


def run():
    for ontology in os.listdir(f"{ONTOLOGY_DIR}"):
        graph = Graph()
        g = graph.parse(source=f"{ONTOLOGY_DIR}/{ontology}")
        labels = get_label_approximate_graph(g)
        definitions = get_definition_approximate_graph(g)