import re
import os
import json

def process_file(input_file):
    global itemset
    
    with open(input_file, 'r') as infile:
        for line in infile:
            line = line.strip()
            parts = line.split()
            
            if len(parts) == 3 and parts[0].startswith('Q') and parts[1].startswith('P') and parts[2].startswith('Q'):
                q1 = parts[0]
                p = parts[1]
                q2 = parts[2]     
                itemset.add(q1)
                itemset.add(q2)


if __name__ == '__main__':
    ##############################
    #  Change split folder here  #
    ##############################
    
    split_name = "p361_part_of"
    os.chdir(f"../data/triplet/{split_name}")
    dir = os.getcwd()
    print(dir)
    itemset = set()
   
    for filename in os.listdir(dir):
        input_file = os.path.join(dir, filename)
        if filename.startswith("P") and os.path.isfile(input_file):
            process_file(input_file)
    
    sorted_items = sorted(list(itemset))
    os.chdir("../../items/")
    dir = os.getcwd()
    with open(os.path.join(dir, f"{split_name}.txt"), "w") as file:
        for item in sorted_items:
            file.write(item + "\n")
            
   
    

