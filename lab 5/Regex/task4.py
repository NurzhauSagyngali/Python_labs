import re

text = input()
matches = re.findall(r"\b[A-Z][a-z]+\b", text)

print(matches)

if matches:
    print("Matches found!")
else:
    print("No matches found!")