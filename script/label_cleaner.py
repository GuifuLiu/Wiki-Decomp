import json 
from tqdm import tqdm
import pickle

d = {}
with open('data/items/items_labels.json', 'r') as f:
    num_lines = sum(1 for line in f)
with open("data/items/items_labels.json", 'r') as file:
    for line in tqdm(file, total=num_lines):
        try:
            json_object = json.loads(line.strip())
            d = d | json_object
           
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON on line: {line.strip()}")
            print(e)

for k in list(d.keys()):
    if k == d[k]:
        del d[k]

with open('data/items/labels.pkl', 'wb') as handle:
    pickle.dump(d, handle, protocol=pickle.HIGHEST_PROTOCOL)

