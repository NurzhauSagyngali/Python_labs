import re

def match():
    txt = input()  
    pattern = r"ab{2,3}"  
    if re.fullmatch(pattern, txt):  
        return "It is a match"
    else:
        return "No match"

print(match())
