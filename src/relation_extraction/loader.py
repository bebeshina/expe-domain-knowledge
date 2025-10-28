import json
import os
import pandas as pd

from definitions import INPUT_DIR, RESOURCE_DIR, OUTPUT_DIR


def get_stubs(d=f"{INPUT_DIR}/audi/"):
    mapping = dict({line.split(" ; ")[0]: line.split(";")[1].replace("\n", "") for line in open(f"{RESOURCE_DIR}/models.csv").readlines()})
    dates = dict({line.split(" ; ")[0]: line.split(";")[1].replace("\n", "") for line in open(f"{RESOURCE_DIR}/dates.csv").readlines()})
    print(mapping)
    values = []
    for f in os.listdir(d):
        dct = json.load(open(d + f, "r"))
        for m in dct:
            model = mapping.get(m)
            print(m, model)
            date = dates.get(m)
            print(m, date)
            for p in dct.get(m):
                brand = p.get("brand")
                for s in p.get("sentences").values():
                    value = [s.strip(), model, date, brand]
                    values.append(value)
    df = pd.DataFrame(values, columns=["stub", "model", "date", "brand"])
    df.drop_duplicates(subset=["stub"], inplace=True)
    print(df.info())
    return df


def get_texts(d=f"{INPUT_DIR}/audi/"):
    mapping = dict({line.split(" ; ")[0]: line.split(";")[1].replace("\n", "") for line in open(f"{RESOURCE_DIR}/models.csv").readlines()})
    dates = dict({line.split(" ; ")[0]: line.split(";")[1].replace("\n", "") for line in open(f"{RESOURCE_DIR}/dates.csv").readlines()})
    print(mapping)
    values = []
    for f in os.listdir(d):
        dct = json.load(open(d + f, "r"))
        for m in dct:
            model = mapping.get(m)
            print(m, model)
            date = dates.get(m)
            print(m, date)
            for p in dct.get(m):
                brand = p.get("brand")
                text = " ".join([s.strip() for s in p.get("sentences").values()])
                value = [text, model, date, brand]
                values.append(value)
    df = pd.DataFrame(values, columns=["text", "model", "date", "brand"])
    df.drop_duplicates(subset=["text"], inplace=True)
    print(df.info())
    return df
