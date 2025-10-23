isa_template = """<instruction>Il est demandé d'énumérer les génériques des mots à partir de la liste et du texte fournis 
                <constraints>
                <constraint>Le terme générique est un nom</constraint>
                <constraint>Le terme spécifique est un nom</constraint>
                <constraint>Aucun commentaire n'est autorisé. Uniquement la liste au format JSON.</constraint>
                <constraint>Aucune note n'est autorisée. Uniquement la liste au format JSON. </constraint>
                <constraint>Aucune remarque n'est autorisée. Uniquement la liste au format JSON. </constraint>
                <constraint>Le terme source est différent du terme cible c'est à dire <code>source.casefold() != cible.casefold()</code></constraint>
                <constraint>Le terme cible (l'hyperonyme) peut être absent du texte et de la liste  ou présent dans le texte ou dans la liste</constraint>
                <constraint>len(cible) > 0</constraint>
                <constraint>len(source) > 0</constraint>
                <constraint>[] est retourné si il n'y a pas de relation de type r_isa trouvée</constraint>
                </constraints> 
                </instruction>
                
                <context>
                Texte : {text}
                Liste des mots : {list}
                </context>
                
                <code_block format="json" type=list[dict(keys=['hyponyme', 'hyperonyme'])]>
                // Your JSON here
                </code_block>
                 """


has_part_template = """<instruction>Il faut donner des parties, constituants, éléments de l'objet 
                à partir du texte et de la liste fournis.
                <constraints>
                <constraint>Le terme source est un nom</constraint>
                <constraint>Le terme cible est un nom</constraint>
                <constraint>Le terme source est différent du terme cible</constraint>
                <constraint>Le terme cible peut être absent du contexte </constraint>
                <constraint>len(terme source) > 0</constraint>
                <constraint>len(terme cible) > 0</constraint>
                </constraints> 
                </instruction>

                <context>
                Texte : {text}
                Liste des mots : {list}
                </context>

                <code_block format="json">
                // Your JSON here
                </code_block>
                 """


mater_template = """<instruction>A partir des mots du texte et de la liste, il faut donner la ou les matière(s) 
                ou substance(s) pouvant composer l'objet.
                <constraints>
                <constraint>Le terme source est un nom</constraint>
                <constraint>Le terme cible est un nom qui désigne une matière ou une substance</constraint>
                <constraint>Le terme source est différent du terme cible</constraint>
                <constraint>Le terme cible peut être absent du contexte </constraint>
                <constraint>len(terme source) > 0</constraint>
                <constraint>len(terme cible) > 0</constraint>
                </constraints> 
                </instruction>

                <context>
                Texte : {text}
                Liste des mots : {list}
                </context>

                <code_block format="json">
                // Your JSON here
                </code_block>
                 """


carac_template = """<instruction>Il est demandé d'en énumérer les caractéristiques (adjectifs) typiques des noms 
                présents dans la liste et dans le texte fournis. 
                
                <constraints>
                <constraint>Le terme source est un nom (NOUN, NPROP)</constraint>
                <constraint>Le terme cible ne peut être qu'un adjectif (ADJ)</constraint>
                <constraint>Le terme source est différent du terme cible</constraint>
                <constraint>Le terme cible peut être absent du contexte </constraint>
                <constraint> 0 < len(terme source)</constraint>
                <constraint>0 < len(terme cible)</constraint>
                </constraints> 
                </instruction>

                <context>
                Texte : {text}
                Liste des mots : {list}
                </context>
                
                <code_block format="json">
                // Your JSON here
                </code_block>
                 """


color_template = """<instruction>Il est demandé d'en énumérer les couleurs des noms 
                présents dans la liste et dans le texte fournis. 
                
                <constraints>
                <constraint>Le terme source est un nom (NOUN, NPROP)</constraint>
                <constraint>Le terme cible est une couleur.</constraint>
                <constraint>Le terme source est différent du terme cible</constraint>
                <constraint>Le terme cible peut être absent du contexte </constraint>
                <constraint> 0 < len(terme source)</constraint>
                <constraint>0 < len(terme cible)</constraint>
                </constraints> 
                </instruction>

                <context>
                Texte : {text}
                Liste des mots : {list}
                </context>
                
                <code_block format="json">
                // Your JSON here
                </code_block>
                 """


process_template = """<instruction>A partir des mots du texte et de la liste, il faut donner le ou les processus ou les événemnets
                dont l'objet est le patient.
                <constraints>
                <constraint>Le terme source est un nom</constraint>
                <constraint>Le terme cible est un verbe</constraint>
                <constraint>Le terme source est différent du terme cible</constraint>
                <constraint>Le terme cible peut être absent du contexte </constraint>
                <constraint>len(terme source) > 0</constraint>
                <constraint>len(terme cible) > 0</constraint>
                </constraints> 
                </instruction>

                <context>
                Texte : {text}
                Liste des mots : {list}
                </context>

                <code_block format="json">
                // Your JSON here
                </code_block>
                 """


lieu_template = """<instruction>A partir d'un terme du domaine automobile présent dans le texte et dans la liste, il est demandé d'énumérer les LIEUX 
                typiques où peut se trouver le terme/objet en question. </instruction>

                <constraints>
                <constraint>Le terme source est un nom</constraint>
                <constraint>Le terme cible est un nom</constraint>
                <constraint>Le terme source est différent du terme cible</constraint>
                <constraint>Le terme cible peut être absent du contexte </constraint>
                <constraint>len(terme source) > 0</constraint>
                <constraint>len(terme cible) > 0</constraint>
                </constraints>
                 
                <context>
                Texte : {text}
                Liste des mots : {list}
                </context>
                
                <code_block format="json">
                // Your JSON here
                </code_block>
                 """


syn_template = """<instruction>A partir des mots du texte et de la liste, il est demandé d'énumérer les synonymes 
                ou quasi-synonymes.

                <constraints>
                <constraint>Le terme source est différent du terme cible</constraint>
                <constraint>Le terme cible peut être absent du contexte </constraint>
                <constraint>len(terme source) > 0</constraint>
                <constraint>len(terme cible) > 0</constraint>
                </constraints> 
                </instruction>

                <context>
                Texte : {text}
                Liste des mots : {list}
                </context>

                <code_block format="json">
                // Your JSON here
                </code_block>
                 """


# ----------------------- for later use -------------------------------


instr_template = """<instruction>A partir de la liste des relations, donner l'instrument avec lequel on fait l'action.  </instruction>

                <constraints>
                <constraint>Le terme source est un nom</constraint>
                <constraint>Le terme cible est un nom</constraint>
                <constraint>Le terme source est différent du terme cible</constraint>
                <constraint>Le terme cible peut être absent du contexte </constraint>
                <constraint>len(terme source) > 0</constraint>
                <constraint>len(terme cible) > 0</constraint>
                </constraints>

                <context>
                Relations : {list}
                </context>

                <code_block format="json">
                // Your JSON here
                </code_block>
                 """


# ---------------------------------------------------------------------


verification_isa="""<instruction> Retourne 0 si l'affirmation est vraie et 1 si elle est fausse.</instruction>
                  <context>{text}</context>"""