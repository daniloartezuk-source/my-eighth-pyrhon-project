import re

def parse_emails(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    pattern = r"([\w\.-]+)@([\w\.-]+)\.\w+"
    matches = re.findall(pattern, content)
    return matches

print(parse_emails("input.txt"))