import pandas as pd
import loader, nodes, isa, has_part, matter, carac, manner, locution
from definitions import INPUT_DIR, OUTPUT_DIR
from src.relation_extraction.nodes import prepare_nodes





def run_extraction_from_stubs():
    # nodes.prepare_nodes()
    df = pd.read_csv(f"{OUTPUT_DIR}/data_with_nodes.csv", sep=';')
    print(df.info)
    test = df.sample(100)

    # test["locution"] = test.apply(lambda x: locution.get_locution(x["stub"], x["nouns"]), axis=1)

    test["locution"] = test["nouns"].apply(locution.get_locution_list)
    # test["isa"] = test.apply(lambda x : isa.get_isa_with_nodes(x["stub"], x["nouns"]), axis=1)
    # test["carac"] = test["stub"].apply(carac.get_carac)
    # test["carac"] = test.apply(lambda x : carac.get_carac(x["stub"], x["nouns"]), axis=1)


run_extraction_from_stubs()

# <examples>
# <example>terme_source = 'huile' relation_type='r_locution' terme_cible='huile d'olive'</exemple>
# <example>terme_source = 'itinéraire' relation_type='r_locution' terme_cible='itinéraire optimisé'</exemple>
# </examples>