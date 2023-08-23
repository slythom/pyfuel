import requests
import json

def sp98():
    r = requests.get("https://www.data.economie.gouv.fr/api/records/1.0/search/?dataset=prix-carburants-fichier-quotidien-test-ods&q=&refine.prix_nom=SP98")
    data = r.text
    parse_json = json.loads(data)
    price = parse_json['records'][0]['fields']
    price = (price['prix_valeur'])
    return price

def sp95():
    r = requests.get("https://www.data.economie.gouv.fr/api/records/1.0/search/?dataset=prix-carburants-fichier-quotidien-test-ods&q=&refine.prix_nom=SP95")
    data = r.text
    parse_json = json.loads(data)
    price = parse_json['records'][0]['fields']
    price = (price['prix_valeur'])
    return price

def e10():
    r = requests.get("https://www.data.economie.gouv.fr/api/records/1.0/search/?dataset=prix-carburants-fichier-quotidien-test-ods&q=&refine.prix_nom=E10")
    data = r.text
    parse_json = json.loads(data)
    price = parse_json['records'][0]['fields']
    price = (price['prix_valeur'])
    return price

def e85():
    r = requests.get("https://www.data.economie.gouv.fr/api/records/1.0/search/?dataset=prix-carburants-fichier-quotidien-test-ods&q=&refine.prix_nom=E85")
    data = r.text
    parse_json = json.loads(data)
    price = parse_json['records'][0]['fields']
    price = (price['prix_valeur'])
    return price

def diesel():
    r = requests.get("https://www.data.economie.gouv.fr/api/records/1.0/search/?dataset=prix-carburants-fichier-quotidien-test-ods&q=&refine.prix_nom=Gazole")
    data = r.text
    parse_json = json.loads(data)
    price = parse_json['records'][0]['fields']
    price = (price['prix_valeur'])
    return price

def gpl():
    r = requests.get("https://www.data.economie.gouv.fr/api/records/1.0/search/?dataset=prix-carburants-fichier-quotidien-test-ods&q=&refine.prix_nom=GPLc")
    data = r.text
    parse_json = json.loads(data)
    price = parse_json['records'][0]['fields']
    price = (price['prix_valeur'])
    return price