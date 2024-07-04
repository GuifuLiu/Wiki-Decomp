import json
import re
import time 
import requests
import os
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

split_name = "p2670_has_parts_of_the_class"
os.chdir(f"../data/{split_name}")

with open("items.txt", 'r') as infile, open('claims_to_strings.json', 'a') as out:
    claims = []
    for line in infile:
        claims.append(line.strip())
    claim_dict = {} 
    
    sparql_values = list(map(lambda id: "wd:" + id, claims))[:476]
    n_split = 476
    for i in range(0, len(sparql_values), n_split):
        sparql_values_split = sparql_values[i:i+n_split] if i+n_split < len(sparql_values) else sparql_values[i:]
        item2label = wikidata_query('''
            SELECT ?item ?itemLabel WHERE {
            VALUES ?item { %s }
            SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }''' % " ".join(sparql_values_split))

        for result in item2label :
            item = re.sub(r".*[#/\\]", "", result['item']['value'])
            label = result['itemLabel']['value']
            claim_dict[item] = label
        
        json.dump(claim_dict, out)
        time.sleep(0.5)