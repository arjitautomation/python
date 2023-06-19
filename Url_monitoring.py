import requests

reachable_file = "reachable.txt"
unreachable_file = "unreachable.txt"

with open("Urls.txt", 'r') as f:
    lines = f.readlines()
    length = len(lines)
    with open(reachable_file, 'w') as reachable_file, open(unreachable_file, 'w') as unreachable_file:
        for line in lines:
            line = line.strip() 
            r = requests.get(line)
            if r.status_code == 200:
                reachable_file.write(line + " is reachable\n")
            else:
                unreachable_file.write(line + " is not reachable\n")
