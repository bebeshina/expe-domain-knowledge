import ollama
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from resources import aco_schemas
from resources.aco_schemas import Links
from resources.aco_templates import basic_token_template


def init_with_valid_pairs(text, valid_tokens):
    temp = []
    for i in range(len(valid_tokens)-1):
        j= i+1
        while j < len(valid_tokens):
            source = valid_tokens[i]
            cible = valid_tokens[j]
            # texte=text,
            prompt = basic_token_template.format(texte=text, source=source, cible=cible)
            response = ollama.generate(model="llama3.2",
                                       prompt=prompt,
                                       format=aco_schemas.Link.model_json_schema())
            link = aco_schemas.Link.model_validate_json(response.response)
            if link.node_1 == source and link.node_2 == cible:
                print(f"{link.node_1}, {link.node_2}, {link.weight}")
                temp.append(link)
            j += 1
        i += 1
    return temp


def max_normalize_graph(links: list) -> list:
    srt = sorted([r.weight for r in links])
    max_w = srt[-1]
    updated = []
    for link in links:
        min_max_scaled_w = link.weight/max_w
        updated_link = aco_schemas.Link(node_1=link.node_1,
                                        node_2=link.node_2,
                                        weight=min_max_scaled_w)
        updated.append(updated_link)
    return updated


def plot_association_graph(links: list):
    # build a dataframe
    values = []
    for l in links:
        values.append([l.node_1, l.node_2, l.weight])
    df = pd.DataFrame(values, columns=["node_1", "node_2", "w"])
    print(df.info())
    pivot = df.pivot(columns="node_1", index="node_2", values="w")
    sns.heatmap(pivot, annot=True, fmt=".1f")
    plt.show()


def run():
    text = """Insert décoratif effet alu brossé sur planche de bord"""
    valid_toks = ['insert', 'décoratif', 'effet', 'alu', 'brossé', 'planche de bord']
    links = init_with_valid_pairs(text, valid_toks)
    normalized = max_normalize_graph(links)
    plot_association_graph(normalized)

run()
