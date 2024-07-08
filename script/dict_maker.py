import re
import os
import json

def process_file(input_file):
    global itemset, is_p361, num_edges
    global small_big, big_small

    with open(input_file, 'r') as infile:
        for line in infile:
            num_edges += 1
            line = line.strip()
            parts = line.split()
            
            if len(parts) == 3 and parts[0].startswith('Q') and parts[1].startswith('P') and parts[2].startswith('Q'):
                q1 = parts[0]
                p = parts[1]
                q2 = parts[2]     
                itemset.add(q1)
                itemset.add(q2)

                if is_p361:
                    if p == "P361":
                        if q2 in big_small:
                            if q1 not in big_small[q2]:
                                big_small[q2].append(q1)
                        else:
                            big_small[q2] = [q1]
                        if q1 in small_big:
                            if q2 not in small_big[q1]:
                                small_big[q1].append(q2)
                        else:
                            small_big[q1] = [q2]
                else:
                    if p == "P527":
                        if q1 in big_small:
                            if q2 not in big_small[q1]:
                                big_small[q1].append(q2)
                        else:
                            big_small[q1] = [q2]
                        if q2 in small_big:
                            if q1 not in small_big[q2]:
                                small_big[q2].append(q1)
                        else:
                            small_big[q2] = [q1]
                            
                    if p == 'P2670':
                        if q1 in big_small:
                            if q2 not in big_small[q1]:
                                big_small[q1].append(q2) 
                        else:
                            big_small[q1] = [q2]
                        if q2 in small_big:
                            if q1 not in small_big[q2]:
                                small_big[q2].append(q1)
                        else:
                            small_big[q2] = [q1]   


if __name__ == '__main__':
    num_edges = 0
    is_p361 = False
    ##############################
    #  Change split folder here  #
    ##############################
    
    split_name = "p2670_has_parts_of_the_class"
    os.chdir(f"../data/triplet/{split_name}")
    dir = os.getcwd()
    
    itemset = set()
    small_big = dict()
    big_small = dict()
    for filename in os.listdir(dir):
        if filename.endswith(".json"):
            if filename.find("P361") != -1:
                is_p361 = True
            input_file = os.path.join(dir, filename)
            if filename.endswith(".json") and os.path.isfile(input_file):
                process_file(input_file)
    
    sorted_items = sorted(list(itemset))
    os.chdir(f"../../items/{split_name}")
    dir = os.getcwd()
    with open(os.path.join(dir, "items.txt"), "w") as file:
        for item in sorted_items:
            file.write(item + "\n")
            
    os.chdir(f"../../dict/{split_name}")
    dir = os.getcwd()
    with open(os.path.join(dir, "big_small.json"), "w") as file:
        json.dump(big_small, file)
    
    with open(os.path.join(dir, "small_big.json"), "w") as file:
        json.dump(small_big, file)

    

    

