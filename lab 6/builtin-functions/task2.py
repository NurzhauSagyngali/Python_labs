text = input("Enter a string: ")  

uppers = sum(map(str.isupper, text))
lowers = sum(map(str.islower, text))

print("Upper case letters:", uppers, "Lower case letters:", lowers)
