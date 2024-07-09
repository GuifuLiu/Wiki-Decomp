import re
import os
import json
import shelve
from tqdm import tqdm

def process_file(input_file):
    global num_edges, d

    with open(input_file, 'r') as infile:
        for line in infile:
            num_edges += 1
            line = line.strip()
            parts = line.split()
            
            if len(parts) == 3 and parts[0].startswith('Q') and parts[1].startswith('P') and parts[2].startswith('Q'):
                q1 = parts[0]
                p = parts[1]
                q2 = parts[2]     
                if q2 == "Q49":
                    print("q1", q1)
                    # print("q2 in d", q2 in d)
                    # print("q1 in d[q2]", q1 in d[q2])
                if p == "P361":
                    if q2 == "Q49":
                        if (q2 in d):
                            print("q2 in d")
                            print("d[q2]", d[q2])
                            # if q1 not in d[q2]:
                            #     print("need update")
                        else:
                            print("q2 NOT in d")
                        print("----------")
                    # Shelf is immutable. DO NOT append directly 
                    if q2 in d:
                        if q1 not in d[q2]:
                            temp = d[q2]
                            temp.append(q1)
                            d[q2] = temp
                    
                    else:
                        d[q2] = [q1]
                    
                     
                elif p == "P527":
                    if q1 in d:
                        if q2 not in d[q1]:
                            d[q1].append(q2)
                    else:
                        d[q1] = [q2]
                            
                elif p == 'P2670':
                    if q1 in d:
                        if q2 not in d[q1]:
                            d[q1].append(q2) 
                    else:
                        d[q1] = [q2]


if __name__ == '__main__':
    num_edges = 0
    ##############################
    #  Change split folder here  #
    ##############################
    split_name = "p361_part_of"

    in_dir = f"./data/triplet_clean/{split_name}"
    out_dir = f"./data/dict/{split_name}/decomp_dict"
    if os.path.exists(out_dir):
        os. remove(out_dir)

    d = shelve.open(out_dir)
    fnames = []
    for filename in os.listdir(in_dir):
        fnames.append(filename)
    for filename in tqdm(fnames):
        # print(filename)
        input_file = os.path.join(in_dir, filename)
        if os.path.isfile(input_file):
            process_file(input_file)
    
    # with open(os.path.join(dir, "small_big.json"), "w") as file:
    #     json.dump(small_big, file)
    d.close()

    

    

