import re

import pandas as pd
from definitions import OUTPUT_DIR
from src.relation_extraction.carac import get_carac
from src.relation_extraction.color import get_color
from src.relation_extraction.has_part import get_has_part
from src.relation_extraction.isa import get_isa
from src.relation_extraction.lieu import get_lieu
from src.relation_extraction.matter import get_mater
from src.relation_extraction.process import get_processus
from src.relation_extraction.syn import get_syn


def get_relations(stub, liste):
    stop_list = ["internal", "INTERNAL#", "Pour rappel", "Vorsprung", "Cheffe de Produit", "Chef de Produit", "Tarif", "édition", "documentation"]
    go = True
    for stop in stop_list:
        if stop in stub:
            go = False
    if go:
        print("text>>>", stub)
        print("liste>>>", liste)
        relations = []
        syn = get_syn(stub, liste)
        has_part = get_has_part(stub, liste)
        mater = get_mater(stub, liste)
        carac = get_carac(stub, liste)
        color = get_color(stub, liste)
        processus = get_processus(stub, liste)
        lieu = get_lieu(stub, liste)
        # isa is a meta relation?
        isa = get_isa(stub, liste)

        if syn:
            relations.extend(syn)
        if has_part:
            relations.extend(has_part)
        if mater:
            relations.extend(mater)
        if carac:
            relations.extend(carac)
        if color:
            relations.extend(color)
        if processus:
            relations.extend(processus)
        if lieu:
            relations.extend(lieu)
        if isa:
            relations.extend(isa)
        for r in relations:
            print(r)
        return relations
    else:
        return []


def group_by_model():
    df = pd.read_csv(f"{OUTPUT_DIR}/data_mwt_loc_nodes.csv", sep=";", encoding="utf8")
    print(len(set(df.model.values.tolist())), set(df.model.values.tolist()))
    for model in set(df.model.values.tolist()):
         if "Audi A1 Sportback allstreet" in model:
            sub = df[df["model"] == model]
            print(model, len(sub))
            sub["relations"] = sub.apply(lambda x: get_relations(x["stub"], x["considered_tokens"]), axis=1)
            for e in sub.relations.values.tolist():
                print(e)

stub = "myAudi vous fournit à tout  moment les informations essentielles telles que les niveaux de carburant et d’huile, les kilomètres parcourus,  le statut des portières, les éventuels avertissements et les rendez-vous atelier."
get_relations(stub, stub.split(" "))


# group_by_model()
                # système multiagent ACO
                # start beguinning of the phrase then move forward
                # each ant updates the graph thus new paths are constantly formed
                
                # express each model as a set of semantic relations (we dehydrate the text to get out of noisy
                # textual data, only keep the core information)
                # propose a metric to evaluate translation as a set of relations evaluator LLM:
                # LLM 1 : generates summary from available relations for each model
                # LLM 2: evaluates semantic similarity with the initial text and the coverage and the entropy evolution

                # build summary regarding each model
                # compare to agnostic summary from the web

                # first vectorstore
                # plug to the ontology world
                # second vectorstore
                # build a global graph for release : interoperability with the ontologies and car model conceptual representation (each car is a set of features/relations)
                # clean building process for release  : takes doc, yes/no for ontology, reltypes

