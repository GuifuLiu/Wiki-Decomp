import json
import re
import time 
import requests
import os
from tqdm import tqdm
from SPARQLWrapper import SPARQLWrapper, JSON


def wikidata_query(query):
    try:
        # set an agent to avoid 403 HTTP ERROR
        sparql = SPARQLWrapper("https://query.wikidata.org/sparql",
                               agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36')
        sparql.setReturnFormat(JSON)
        sparql.setQuery(query)
        sparql.setTimeout(60)  # 5 minutes
        # Get the answering {'head': {'vars': [...]}, 'results': {'bindings': [...]}}
        ans = sparql.query().convert()['results']['bindings']
    except:
        ans = []

    return ans


# def wikidata_query(query):
#     url = 'https://query.wikidata.org/sparql'
#     try:
#         r = requests.get(url, params = {'format': 'json', 'query': query})
#         return r.json()['results']['bindings']
#     except json.JSONDecodeError as e:
#         raise Exception('Invalid query')

##############################
#  Change split folder here  #
##############################

split_name = "all_claims.txt"
dir = os.getcwd()
os.chdir(f"./data/claim/")

with open(split_name, 'r') as infile, open('claim_labels.json', 'a') as out, open('blacklist.txt', 'a') as blacklist:
    claims = []
    for line in infile:
        claims.append(line.strip())
    sparql_values = list(map(lambda id: "wd:" + id, claims))

    n_split = 400
    for i in tqdm(range(0, len(sparql_values), n_split)):
        claim_dict = {} 
        sparql_values_split = sparql_values[i:i+n_split] if i+n_split < len(sparql_values) else sparql_values[i:]
        # print("split_len:",len(sparql_values_split))
        item2label = wikidata_query('''
            SELECT ?item ?itemLabel WHERE {
            VALUES ?item { %s }
            SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }''' % " ".join(sparql_values_split))

        for result in item2label :
            item = re.sub(r".*[#/\\]", "", result['item']['value'])
            label = result['itemLabel']['value']
            claim_dict[item] = label
            if item == label:
                blacklist.write(item + "\n")
        
        json.dump(claim_dict, out)
        out.write("\n")
        time.sleep(0.5)