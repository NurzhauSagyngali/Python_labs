import re

text = input()
words = text.split("_")
camel_case = words[0].lower() + "".join(word.capitalize() for word in words[1:])

print(camel_case)
