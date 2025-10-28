import ollama

from resources.aco_templates import rels_selection_template, basic_template
from src import relation_extraction
from resources import aco_schemas






def init_aco_graph(texte):
    prompt = basic_template.format(texte=texte)
    response = ollama.generate(model=relation_extraction.model,
                               prompt=prompt,
                               format=aco_schemas.Links.model_json_schema())
    links = aco_schemas.Links.model_validate_json(response.response)
    return links


def normalize_graph(relations: list) -> list:
    srt = sorted([r.poids for r in relations])
    max = srt[-1]
    min = srt[0]
    for relation in relations:
        w = relation.get("poids")/(max-min)


def run_relations(source, cible, text):
    prompt = rels_selection_template.format(source=source, cible=cible, text=text)
    response = ollama.generate(model=relation_extraction.model,
                               prompt=prompt,
                               format=aco_schemas.Relations.model_json_schema())
    rel = aco_schemas.Relations.model_validate_json(response.response)
    return rel


def test(texte):
    links = init_aco_graph(texte)
    rels = []
    for link in links.links:
        rels.extend(run_relations(link.node_1, link.node_2, texte).relations)
        rels.extend(run_relations(link.node_2, link.node_1, texte).relations)
    rels.extend(links.links)
    print(rels)
    for r in rels:
        print(r.source, r.relation_type, r.target, r.poids)
    return rels





txt = """D\u00e9couvrez le dernier chef-d\u2019\u0153uvre de design et de dynamisme Audi!"""
test(txt)






