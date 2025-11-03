basic_template = """<instructon>A partir du texte où tous les mots sont sémantiquement liés, 
                attribue un poids d'association à chaque paire de mots du texte en fonction 
                de leur position. Tous les mots doivent être liés. Le poids total du graphe est 1.0</instruction>
                <context>{texte}</context>
                <format>'mot_1, mot_2, poids dans l'intervalle [0;1]"""
#
basic_token_template = """<instructon>Attribue un poids d'association aux tokens fournis compte tenu du contexte fourni.</instruction>
                        <instructon>Retourne uniquement les association entre les tokens fournis.</instruction>
                        <instructon>N'extraie pas de mots autres que les mots fournis du texte fourni.</instruction>
                        <instructon>node_1 == source, node_2 == cible</instruction>
                        <tokens>{source}, {cible}</tokens>
                        <context>{texte}</context>
                        <format>node_1, node_2, poids d'association dans l'intervalle [0;100]</format>"""

qualif_template = """<instructon>Pour la paire de noeuds donnée, estime la probabilité pour A partir du texte où tous les mots sont sémantiquement liés,
                attribue un poids d'association à chaque paire de mots du texte en fonction
                de leur position. Tous les mots doivent être liés. Le poids total du graphe est 1.0</instruction>
                <context>{texte}</context>
                <format>'mot_1, mot_2, poids in [0;1]'"""


rels_selection_template = """<instruction>Il est demandé de lister le type et le poids de la relation le terme {source}
        et le terme {cible}. Donne le poids entre -100.0 (la relation n'existe pas ou elle est fausse) et 100.0 
        pour chaque type de relation dans relations. Ne répète pas la consigne. Retourne uniquement les réponses 
        sous forme de relations. </instruction>
        <relations>
        <relation 
            type="r_isa" 
            relation_detail="le terme cible est le générique du terme source, les deux termes doivent être des noms 
            dans le texte fourni. Si le terme source et/ou le terme cible n'est pas un nom, le poids de 
            la relation r_isa est négatif." 
            examples="chien r_isa animal, table r_isa meuble" 
            poids_minimum=-100.0 
            poids_maximum=100.0/>
        <relation 
            type="r_carac" 
            relation_detail="le terme cible de la relation r_carac doit être un adjectif et une caractéristique du 
            terme source, le terme source doit être un nom dans le texte fourni. Si le terme cible n'est pas un 
            adjectif, le poids de la relation r_carac est négatif, il ne peut pas être positif. Si le terme 
            cible est un adjectif ou un participe qui peut désigner une caractéristique typique de 
            l'objet désigné par le terme source, la relation est positive." 
            examples="soupe r_carac liquide, train r_carac rapide, design r_carac personnalisable, chaise r_carac blanche" 
            poids_minimum=-100.0 
            poids_maximum=100.0/>
        <relation 
            type="r_has_part" relation_detail="le terme cible désigne un constituant l'objet ou une partie de 
            l'objet désigné par terme source. Si le terme source et/ou le terme cible n'est pas un nom dans 
            le texte fourni, le poids de la relation r_has_part est négatif car dans ce cas la relation est fausse."
            examples="maison r_has_part fenêtre, garçon r_has_part bras, document r_has_part page"
            poids_minimum=-100.0 
            poids_maximum=100.0/>
        <relation 
            type="r_object_mater" 
            relation_detail="terme cible désigne la matière qui constitue l'objet que désigne le terme source, 
            les deux termes doivent être des noms dans le texte fourni. Si le terme source et/ou le terme cible 
            n'est pas un nom, le poids de la relation r_object_mater est négatif car la relation est fausse." 
            examples="pain r_object_mater farine, clé r_object_mater métal, habillage r_object_mater cuir"
            poids_minimum=-100.0 
            poids_maximum=100.0/>
        <relation 
            type="r_color" 
            relation_detail="le terme cible doit désigner une couleur de l'objet désigné par le terme source. Si le 
            terme cible ne désigne pas une couleur et n'est pas un nom ni une locution nominale, le poids de la relation 
            r_color est négatif." 
            examples="ciel r_color gris", épine r_color vert, drap r_color blanc, table r_color noir" 
            poids_minimum=-100.0 
            poids_maximum=100.0/>
        <relation 
            type="r_patient" 
            relation_detail="le terme cible désigne le patient de l'action désignée par le terme source, le terme 
            source doit désigner une action ou un processus. Si le terme source n'est pas un verbe ni un nom verbal, 
            le poids de la relation r_patient est négatif." 
            examples = "manger r_patient pomme, écrire r_patient lettre, acheter r_patient voiture, extinction r_patient feu"
            poids_minimum=-100.0 
            poids_maximum=100.0/>
        <relation 
            type="r_lieu" 
            relation_detail="le terme cible désigne le lieu ou peut se trouver le terme source, le terme cible 
            doit être un lieu, en endroit dans le texte fourni. Le terme source et le terme cible doivent être 
            des noms. Si le terme source et/ou le terme cible n'est pas un nom, le poids de la relation r_lieu est 
            négatif." 
            examples="lit r_lieu chambre, bâteau r_lieu mer, voiture r_lieu route"
            poids_minimum=-100.0 
            poids_maximum=100.0/>
        </relations>

        <context>
            source: {source}
            cible: {cible}
            text: {text}
        </context> 
"""

relation_check = """Est-ce que l'affirmation est vraie? Réponds 0 si elle est vraie et 1 si elle est fausse. 
                    Ne donne aucun commentaire."""

isa_augmentation_template = """<instruction>Quel est le générique de {term} (automobile). 
                            Ne donne pas d'explication ni commentaire.</instruction>
                            <examples>chien r_isa animal, table r_isa meuble</examples> 
                            <format>{term} r_isa ta_réponse</format>"""

carac_augmentation_template = """<instruction>Quelles sont les caractéristiques typiques de {term} (automobile). 
                            Ne donne pas d'explication ni commentaire. </instruction>
                            <examples>soupe r_carac liquide, train r_carac rapide, design r_carac personnalisable, 
                            chaise r_carac blanche</examples> 
                            <format>{term} r_carac ta_réponse</format>
                            """

has_part_augmentation_template = """<instruction>Quelles sont les parties de {term} (automobile). 
                            Ne donne pas d'explication ni commentaire.</instruction> 
                            <examples>ciel maison r_has_part fenêtre, garçon r_has_part bras, 
                            document r_has_part page</examples> 
                            <format>{term} r_has_part ta_réponse</format>"""

object_mater_augmentation_template = """<instruction>Quelle est la matière de {term} (automobile). 
                            Ne donne pas d'explication ni commentaire.</instruction>
                            <examples>pain r_object_mater farine, clé r_object_mater métal, habillage r_object_mater cuir</examples>
                            <format>{term} r_object_mater ta_réponse</format>
                            """

color_augmentation_template = """<instruction>Quelle est la couleur de {term} (automobile). 
                            Ne donne pas d'explication ni commentaire.</instruction>
                            <examples>ciel r_color gris, drap r_color blanc, table r_color noir </examples> 
                            <format>{term} r_color ta_réponse</format>
                            """

lieu_augmentation_template = """<instruction>Quel est le lieu typique de {term} (en rapport avec l'automobile). 
                            Ne donne pas d'explication ni commentaire.</instruction>
                            <examples>"lit r_lieu chambre, bâteau r_lieu mer, voiture r_lieu route</examples>
                            <format>{term} r_lieu ta_réponse</format>"""