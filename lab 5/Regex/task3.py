import re

text = input("Enter text: ")
matches = re.findall(r"\b[a-z]+(?:_[a-z]+)+\b", text)  
print(matches)

if matches:
    print("Matches found")
else:
    print("No matches found")
