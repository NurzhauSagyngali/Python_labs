import re

text = input("Enter text: ")
match = re.search("^a.*b$", text)  

if match:
    print("Match found!")
else:
    print("No match found!")
