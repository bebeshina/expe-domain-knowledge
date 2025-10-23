import ollama

from src import relation_extraction
from resources import aco_schemas


# using llm assign local weights to the arcs of the graph
# browse with ants caring probabilty of this semantic relation, type and update weights


# dans un texte relatif à un domaine d'activité, on peut supposer que tous les mots sont liés

template = """<instructon>A partir du texte où tous les mots sont sémantiquement liés, 
                attribue un poids d'association à chaque paire de mots du texte en fonction 
                de leur position. Tous les mots doivent être liés. Le poids total du graphe est 1.0</instruction>
                <context>{texte}</context>
                <format>'mot_1, mot_2, poids dans l'intervalle [0;1]"""


# qualif_template = """<instructon>Pour la paire de noeuds donnée, estime la probabilité pour A partir du texte où tous les mots sont sémantiquement liés,
#                 attribue un poids d'association à chaque paire de mots du texte en fonction
#                 de leur position. Tous les mots doivent être liés. Le poids total du graphe est 1.0</instruction>
#                 <context>{texte}</context>
#                 <format>'mot_1, mot_2, poids \in [0;1]'"""


isa = """<instruction>Il est demandé de donner le poids de la relation de type r_isa entre le {terme_1} et le {terme_2}. 
        La cible de la relation r_isa est le générique de sa source. Le poids doit être dans l'intervalle [0;1] 
"""

def init_aco_graph(texte):
    prompt = template.format(texte=texte)
    response = ollama.generate(model=relation_extraction.model,
                               prompt=prompt,
                               format=aco_schemas.Links.model_json_schema())
    links = aco_schemas.Links.model_validate_json(response.response)
    return links


def run_isa(terme_1, terme_2):
    prompt = isa.format(terme_1=terme_1, terme_2=terme_2)
    response = ollama.generate(model=relation_extraction.model,
                               prompt=prompt,
                               format=aco_schemas.Isa.model_json_schema())
    rel = aco_schemas.Isa.model_validate_json(response.response)
    return rel


def test():
    texte = ("myAudi vous fournit à tout  moment les informations essentielles telles que les niveaux de carburant "
             "et d’huile, les kilomètres parcourus,  le statut des portières, les éventuels avertissements "
             "et les rendez-vous atelier.")
    links = init_aco_graph(texte)
    for link in links.links:
        print(link)
        print(run_isa(link.node_1, link.node_2))




# def isa():



# def run_iteration(arcs: list):
#     for arc in arcs:
        #  relation probability is evaluated for each type/arc
        # initial pheromone vanishes (calcul avec modulo??)
        # everything if normalized
        # the initial distance of the ontology labels is infinity
        # then , with each move the isa ant tries to reach the label directly
        # the ant can 'see' the ontology labels when they are at the distance = 2
        # or at some point we are ready to summarize and compare with the definition vector
        # ants are used to capture the definition(s) we actually need to access




test()






