import re

text = input()
words = re.sub(r'(?<!^)([A-Z])', r'_\1', text).lower()

print(words)