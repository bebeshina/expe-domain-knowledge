basic_template = """<instructon>A partir du texte où tous les mots sont sémantiquement liés, 
                attribue un poids d'association à chaque paire de mots du texte en fonction 
                de leur position. Tous les mots doivent être liés. Le poids total du graphe est 1.0</instruction>
                <context>{texte}</context>
                <format>'mot_1, mot_2, poids dans l'intervalle [0;1]"""

qualif_template = """<instructon>Pour la paire de noeuds donnée, estime la probabilité pour A partir du texte où tous les mots sont sémantiquement liés,
                attribue un poids d'association à chaque paire de mots du texte en fonction
                de leur position. Tous les mots doivent être liés. Le poids total du graphe est 1.0</instruction>
                <context>{texte}</context>
                <format>'mot_1, mot_2, poids \in [0;1]'"""


rels_selection_template = """<instruction>Il est demandé de lister le type et le poids de la relation le {source} et le {cible}. 
        Donne le poids pour chaque type de relation dans relations. 
        <relations>
        <relation type="r_isa" relation_detail="'cible' est le générique du 'source'" poids_minimum=0.0 poids_maximum=1.0/>
        <relation type="r_carac" relation_detail="'cible' est un adjectif et une caractéristique du 'source''" poids_minimum=0.0 poids_maximum=1.0/>
        <relation type="r_has_part" relation_detail="'cible' désigne un constituant du 'source'" poids_minimum=0.0 poids_maximum=1.0/>
        <relation type="r_object_mater" relation_detail="'cible' est la matière qui constitue 'source''" poids_minimum=0.0 poids_maximum=1.0/>
        <relation type="r_color" relation_detail="'cible' est une couleur du 'source'" poids_minimum=0.0 poids_maximum=1.0/>
        <relation type="r_patient" relation_detail="'cible' est le patient de l'action 'source', 'source' désigne une action ou un processus" poids_minimum=0.0 poids_maximum=1.0/>
        </relations>

        <context>
            source: {source}
            cible: {cible}
            text: {text}
        </context> 
"""