import re

def check_password(password):
    if (8 <= len(password) <= 12 and
        re.search(r"[a-z]", password) and
        re.search(r"[A-Z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[$#@]", password)):
        return "Valid"
    return "Invalid"

for _ in range(3):
    pwd = input()
    print(check_password(pwd))
