import re
from typing import List
import pandas as pd
import networkx as nx
from matplotlib import pyplot as plt

from definitions import OUTPUT_DIR
from resources.aco_schemas import Link


def plot_whole_graph(G: nx.Graph):
    fig = plt.figure("", figsize=(10, 8))
    axgrid = fig.add_gridspec(4, 4)
    ax0 = fig.add_subplot(axgrid[0:3, :])
    nx.draw_networkx(G, ax=ax0,  node_size=20)
    # nx.draw_networkx_edges(G_connected, pos, ax=ax0, alpha=0.4)
    ax0.set_title("Plain graph view")
    ax0.set_axis_off()
    plt.show()


def splits(text: str):
    link_list = []
    qdict = {"ch": "chevaux",
             "g/km": "grammes par kilomètre",
             "kWh": "kilowatt heure",
             "kW": "kilowatt",
             "kg": "kilogramme",
             "g": "grammes",
             "m": "mètre",
             "A": "ampère",
             "TTC": "toutes taxes comprises",
             "HT": "hors taxes",
             "EURO": "euro",
             "€": "euro",
             "km/h": "kilomètre heure",
             "ch à tr/m": "chevaux à tour minute",
             "l/100 km": "litre à 100 kilomètres",
             "[Nn]m à tr/mn": "newton mètre à tour minute",
             "V": "volt"
             }
    for k, v in qdict.items():
        if m := re.search("(?P<q>\d+\s?\d+\s?)(?P<e>%s)[\s.,!?/|\n]" % k, text):
            link_list.extend([Link(node_1=m.group("q"), node_2=m.group("e"), weight=50),
                             Link(node_1=k, node_2=v, weight=50)])
            print(link_list)
    return set(link_list)


def splits_to_graph(lst: List[str]):
    edge_set = set()
    node_set = set()
    G = nx.Graph()

    qdict = {"ch": "chevaux",
             "g/km": "grammes par kilomètre",
             "kWh": "kilowatt heure",
             "kW": "kilowatt",
             "kg": "kilogramme",
             "g": "grammes",
             "m": "mètre",
             "A": "ampère",
             "TTC": "toutes taxes comprises",
             "HT": "hors taxes",
             "EURO": "euro",
             "€": "euro",
             "km/h": "kilomètre heure",
             "ch à tr/m": "chevaux à tour minute",
             "l/100 km": "litre à 100 kilomètres",
             "[Nn]m à tr/mn": "newton mètre à tour minute",
             "V": "volt"
             }

    for text in lst:
        for k, v in qdict.items():
            if m := re.search("(?P<q>\d+\s?\d+\s?)(?P<e>%s)[\s.,!?/|\n]" % k, text):
                node_set.add(m.group("q"))
                node_set.add(m.group("e"))
                node_set.add(v)
                edge_set.add((k, v))
                edge_set.add((m.group("q"), m.group("e")))
                edge_set.add((m.group("q"), v))
    G.add_nodes_from(node_set)
    G.add_edges_from(edge_set)
    plot_whole_graph(G)
    # plot_connected_components(G)
    return G


def test():
    df = pd.read_csv(f"{OUTPUT_DIR}/data_mwt_loc_nodes.csv", sep=";")[:200]
    ls = df["updated_text"].tolist()
    g = splits_to_graph(ls)


test()