import re

text = input()
words = re.split(r"(?=[A-Z])", text)  

words = [word for word in words if word]

print(words)
