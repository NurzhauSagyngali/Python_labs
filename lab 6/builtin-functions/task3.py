def palindrome(s):
    return s == "".join(reversed(s)) # join() - Joins the reversed characters into a new string.

text = input().lower()

if palindrome(text):
    print("Yes it is palindrome")
else:
    print("No it is not palindrome")