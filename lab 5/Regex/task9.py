import re

text = input()
words = re.sub(r"(?<!^)([A-Z])", r" \1", text)

print(words)