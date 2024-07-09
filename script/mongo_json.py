import json 
import shelve
import pickle
from tqdm import tqdm
'''
Schema:
{
    "qid": "Q5",
    "label": "human",
    "part": [
        {
            "pid": "Q742609"
            "plabel": "human nature"
        }
        {
            "pid": "Q9165"
            "plabel": "soul"
        }
    ]
}
'''

split = "p361+p527"

with open(f'data/dict/{split}', 'r') as file:
    lines = file.readlines()

with open('./data/items/labels.pkl', 'rb') as f:
    labels = pickle.load(f)

with open(f"data/json/{split}.json", "a") as outfile: 
    outfile.write("[\n")
for line in tqdm(lines):

    items = line.split()
    if not (all(i in labels for i in items)):
        continue
    k = items[0]
    part_qids = items[1:]
    doc = {}
    doc["qid"] = k
    doc["label"] = labels[k]
    doc["part"] = []
    for part_qid in part_qids:
        part = {}
        part_label = labels[part_qid]
        part["pid"] = part_qid
        part["plabel"] = part_label
        doc["part"].append(part)

    with open(f"data/json/{split}.json", "a") as outfile: 
        json.dump(doc, outfile)
        outfile.write(",\n")

with open(f"data/json/{split}.json", "a") as outfile: 
    outfile.write("]")
