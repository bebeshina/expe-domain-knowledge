model_template = """<instruction>A partir du nom de modèle, il est demandé d'énumérer ses caractéristiques.</instruction>

                <context>
                {text}
                </context>

                <code_block format="json">
                // Your JSON here
                </code_block>
                 """