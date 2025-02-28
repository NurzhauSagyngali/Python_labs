import re

def match():
    txt = input()  
    pattern = r"ab*"  
    if re.fullmatch(pattern, txt):  
        return "It is a match"
    else:
        return "No match"

print(match())
