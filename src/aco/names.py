# Commercial name extractor and encoder
import ollama
from resources.extraction_templates import commercial_names_template


def extract_names(text):
    content = commercial_names_template.format(text=text)
    response = ollama.chat(model="llama3.2",
                           messages=[
                               {"role": "user",
                                "content": content}])
    response_text = response['message']['content']
    name_list = response_text.split(";")
    return name_list

NO_OF_CHARS = 256


def get_next_state(pat, M, state, x):
    if state < M and x == ord(pat[state]):
        return state+1
    return state


def encode_store_names(names: list):
    temp_dic = {}
    for e in names:
        M = len(e)
        TF = [[0 for i in range(NO_OF_CHARS)]
              for _ in range(M + 1)]

        for state in range(M + 1):
            for x in range(NO_OF_CHARS):
                z = get_next_state(e, M, state, x)
                TF[state][x] = z
        print(TF)
        temp_dic[TF] = e
    return temp_dic

# Coroutines, just like generators, are resumable functions but instead of generating values, they consume values on the fly.

txt = """
Tarifs Škoda Enyaq Coupé (TTC) Element Clever Plus Sportline 100% électrique Batterie 85 286 ch"""
ls = extract_names(txt)
encode_store_names(ls)
