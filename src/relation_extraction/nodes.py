import os
import pandas as pd
import fr_core_news_sm
import loader
from typing import List, Tuple
from definitions import INPUT_DIR, OUTPUT_DIR


def keep_only_nodes(lst: List[Tuple]) -> List[Tuple]:
    res = [(tup[0], tup[2], tup[1]) for tup in lst if tup[1] in ["NOUN", "PROPN", "ADJ", "ADV"] and len(tup[0]) > 2]
    return res


def keep_only_nouns(lst: List[Tuple]) -> List[str]:
    res = [set(tup[2] for tup in lst if tup[1] in ["NOUN", "PROPN"] and len(tup[0]) > 2)]
    return res


def prepare_nodes() -> pd.DataFrame:
    nlp = fr_core_news_sm.load()

    dfs = [loader.get_stubs(f"{INPUT_DIR}/{d}/") for d in os.listdir(f"{INPUT_DIR}")]
    frames = []
    while dfs:
        df = dfs.pop()
        df["pos_tagged_words"] = df["stub"].apply(lambda x: [(w.text, w.pos_, w.lemma_) for w in nlp(x)])
        df["nodes"] = df["pos_tagged_words"].apply(keep_only_nodes)
        df["nouns"] = df["pos_tagged_words"].apply(keep_only_nouns)
        df["ready"] = df["nodes"].apply(lambda x: 1 if len(x) > 2 else 0)
        res = df[df["ready"] == 1]
        print(res.head(5))
        frames.append(res)
    data = pd.concat(frames)
    print(len(data))
    data.to_csv(f"{OUTPUT_DIR}/data_with_nodes.csv", sep=";", index=False)
    return data


