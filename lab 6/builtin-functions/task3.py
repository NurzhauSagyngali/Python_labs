def palindrome(s):
    return s == "".join(reversed(s))

text = input().lower()

if palindrome(text):
    print("Yes it is palindrome")
else:
    print("No it is not palindrome")