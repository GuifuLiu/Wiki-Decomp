import re
import os



def process_file(input_file, output_file):
    pattern = re.compile(r'^(wd:Q\d+)\s+(wdt:P\d+)\s+(wd:Q\d+)')
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip().rstrip('.')
            parts = line.split()
            
            if len(parts) == 3 and parts[0].startswith('wd:Q') and parts[1].startswith('wdt:P') and parts[2].startswith('wd:Q'):
                q1 = parts[0][3:]
                p = parts[1][4:]
                q2 = parts[2][3:]
                outfile.write(f"{q1} {p} {q2}\n")
            
            elif len(parts) > 3 and parts[0].startswith('wd:Q') and parts[1].startswith('wdt:P'):
                q1 = parts[0][3:]
                p = parts[1][4:]
                for part in parts[2:]:
                    if part.startswith('wd:Q'):
                        q2 = part[3:].rstrip(',')
                        outfile.write(f"{q1} {p} {q2}\n")

if __name__ == '__main__':
    split_name = "part_of(P361)"
    os.chdir(f"{split_name}")
    cur_dir = os.getcwd()
    for filename in os.listdir(cur_dir):
        input_file = os.path.join(cur_dir, filename)
        if filename.endswith(".json") and os.path.isfile(input_file):
            output_file = os.path.join("../p361", f"{filename}")
            process_file(input_file, output_file)