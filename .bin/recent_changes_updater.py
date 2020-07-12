import sys 
import re
from pprint import pprint

history = list()
changed_files = set()

for line in sys.stdin:
    diff = line.split()

    if diff[1] == "SUMMARY.md" or diff[1] == "README.md" or diff[1].startswith("."):
        continue

    history.append(line.split())

with open(".bin/README.md.template", "r") as template:
    changes_md = ""
    counter = 0

    for diff in history:
        if counter > 20:
            break

        if diff[1] in changed_files:
            continue

        changed_files.add(diff[1])
        changes_md += f"* [{diff[1]}]({diff[1]})\n"

        counter += 1

    template = ''.join(template.readlines())
    rendered = re.sub(r"{{CHANGES}}", changes_md, template)
    
    sys.stdout.write(rendered)
    