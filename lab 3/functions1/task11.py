def palindrome(word):
    if word == word[::-1]:
        return True
    return False

word = input().strip()

print(palindrome(word))
    
    