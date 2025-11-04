# Commercial name extractor and encoder
import ollama
from resources.extraction_templates import commercial_names_template
from cryptography.fernet import Fernet


def extract_names(text):
    content = commercial_names_template.format(text=text)
    response = ollama.chat(model="llama3.2",
                           messages=[
                               {"role": "user",
                                "content": content}])
    response_text = response['message']['content']
    name_list = response_text.split(";")
    return name_list


key = Fernet.generate_key()
cipher_suite = Fernet(key)
encrypted = dict()
hash_dict = dict()


def encrypt_names(spl: list, text: str):
    # data masking strategy
    byte_text = text.encode(encoding="utf-8")
    for e in spl:
        byte_e = e.encode(encoding="utf-8")
        if byte_e not in encrypted.keys():
            cipher_text = cipher_suite.encrypt(byte_e)
            encrypted[byte_e] = cipher_text
        else:
            cipher_text = encrypted.get(byte_e)
        text = byte_text.replace(e, cipher_text)
    return text


def process_encrypt_names(txt: str):
    ls = extract_names(txt)
    print(ls)
    encrypted_text = encrypt_names(ls, txt)
    return encrypted_text


def hash_names(spl: list, text: str):
    for e in spl:
        hash_e = hash(e)
        if hash_e not in hash_dict.keys():
            hash_dict[e] = hash_e
        else:
            hash_e = hash_dict.get(e)
        text = text.replace(e, str(hash_e))
    return text


t = """
Tarifs Škoda Enyaq Coupé (TTC) Element Clever Plus Sportline 100% électrique Batterie 85 286 ch"""
lst = ['Škoda', 'Enyaq Coupé', 'Element Clever Plus', 'Sportline']


print(hash_names(lst, t))
print(encrypt_names(lst, t))

