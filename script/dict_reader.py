import shelve
split = "p361_part_of"
d = shelve.open(f"./data/dict/{split}/decomp_dict")

print(d['Q49'])
d.close() 