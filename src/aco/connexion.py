import ollama

from resources.aco_schemas import Relations, Relation
from resources.aco_templates import rels_selection_template, basic_template, basic_token_template, \
    isa_augmentation_template, carac_augmentation_template, has_part_augmentation_template, \
    object_mater_augmentation_template, color_augmentation_template, lieu_augmentation_template
from src import relation_extraction
from resources import aco_schemas

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


def init_aco_graph(texte):
    prompt = basic_template.format(texte=texte)
    response = ollama.generate(model="llama3.2",
                               prompt=prompt,
                               format=aco_schemas.Links.model_json_schema())
    links = aco_schemas.Links.model_validate_json(response.response)
    return links


# def check_relation():
#
#

def qualify_associations(links, text) -> list:
    rels = []
    for link in links:
        prompt = rels_selection_template.format(source=link.node_1, cible=link.node_2, text=text)
        response = ollama.generate(model="llama3.2",
                                   prompt=prompt,
                                   format=aco_schemas.Relations.model_json_schema())
        resp = aco_schemas.Relations.model_validate_json(response.response)
        rels_out = [r for r in resp.relations if r.source == link.node_1 and r.target == link.node_2]
        for rel_out in rels_out:
            print(f"{rel_out.source}, {rel_out.target}, {rel_out.relation_type}, {rel_out.poids}")
        rels.extend(rels_out)
        prompt = rels_selection_template.format(source=link.node_2, cible=link.node_1, text=text)
        response = ollama.generate(model="llama3.2",
                                   prompt=prompt,
                                   format=aco_schemas.Relations.model_json_schema())
        resp = aco_schemas.Relations.model_validate_json(response.response)
        rels_in = [r for r in resp.relations if r.source == link.node_2 and r.target == link.node_1]
        for rel_in in rels_in:
            print(f"{rel_in.source}, {rel_in.target}, {rel_in.relation_type}, {rel_in.poids}")
        rels.extend(rels_in)
    return rels



def normalize_graph(relations: list) -> list:
    srt = sorted([r.poids for r in relations])
    max_w = srt[-1]
    min_w = srt[0]
    updated = []

    for relation in relations:
        # min_max_scaled_w = (relation.poids-min_w)/(max_w - min_w)
        min_max_scaled_w = relation.poids/max_w
        updated_relation = aco_schemas.Relation(source=relation.source,
                                                target=relation.target,
                                                poids=min_max_scaled_w,
                                                relation_type=relation.relation_type)
        print(relation.poids, ">>", updated_relation.poids)
        updated.append(updated_relation)
    # res = Relations(updated)
    # res.__set_relation_list__(updated)
    return updated


def run_relations(source, cible, text):
    prompt = rels_selection_template.format(source=source, cible=cible, text=text)
    response = ollama.generate(model="llama3.2",
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
    # rels.extend(links.links)
    print(rels)
    for r in rels:
        if type(r) == Relation:
            print(r.source, r.relation_type, r.target, r.poids)
    updated = normalize_graph(rels)
    return rels
"""
Intérieur Sportline Pédalier look aluminium Jantes en alliage 20’’ Vega noires  
        Volant 3 branches sport en_cuir  multifonctions chauffant avec  palettes, détection des mains 
        Confort et agrément  - Direction dynamique progressive
        Palettes au_volant pour sélection du freinage régénératif Ligne et design
        Badge Sportline sur le hayon de coffre - Ciel de pavillon_noir - Coques de rétroviseurs extérieurs noir glossy
        Design intérieur Sportline : sellerie tissu suédine noir perforé,  matériau synthétique noir et surpiqûres grises et noires
"""


def augment_relations(relations:list):
    result = []
    templates = {
        "r_carac": carac_augmentation_template,
        "r_isa": isa_augmentation_template,
        "r_has_part": has_part_augmentation_template,
        "r_object_mater": object_mater_augmentation_template,
        "r_color": color_augmentation_template,
        "r_lieu": lieu_augmentation_template
    }
    sources = set(r.source for r in relations if r.poids > 0)
    for term in sources:
        for r, t in templates.items():
            content = t.format(term=term)
            response = ollama.chat(model="llama3.2",
                                   messages=[
                                           {"role": "user",
                                            "content": content}],
                                   format=Relations.model_json_schema()
                                   )
            rels = Relations.model_validate_json(response['message']['content'])
            result.extend([f"{rel.source}, {rel.relation_type}, {rel.target}" for rel in rels.relations])
            print(term, r, response['message']['content'])
    return result


def test_whole_process():
    text = """
            Habillage tissu gris  sur planche de bord. Jantes en alliage 19”."""
    valid_toks = ['tissu', 'gris', 'contreporte', 'habillage', 'jante', 'alliage', 'planche de bord']
    links = init_with_valid_pairs(text, valid_toks)
    rels = qualify_associations(links, text)
    augmented = augment_relations(rels)
    print(links)
    print(rels)
    print(augmented)
    for l in links:
        print(l.node_1, "association", l.node_2, l.weight)
    for r in rels:
        print(r.source, r.relation_type, r.target, r.poids)
    for a in augmented:
        print(a, "50")



    # ontology_layer =

test_whole_process()





