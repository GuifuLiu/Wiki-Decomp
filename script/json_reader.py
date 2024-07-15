import json
from tqdm import tqdm


items = []

with open("./data/json/items") as file:
    lines = file.readlines()
    ref = [line.rstrip() for line in lines]
print(len(ref))
with open("./data/json/p361+p527.json") as f:
    d = json.load(f)
    for di in tqdm(d):
        # print(di["label"])
        parts = []
        for pi in di["part"]:
            # print(pi)
            pid = pi["pid"]
            parts.append(pid)
        # print(parts)
        if any(item in ref for item in parts):
            items.append(di)

print(len(items))
with open('./data/json/valid.json', 'a') as fout:
    json.dump(items, fout)





        
        # items.append(di["qid"])
        # items_label.append(di["label"])
    
# with open('./data/json/items','a') as f:
# 	for i in items:
# 		f.write(f'{i}\n')

# with open('./data/json/items_label','a') as f:
# 	for i in items_label:
# 		f.write(f'{i}\n')
