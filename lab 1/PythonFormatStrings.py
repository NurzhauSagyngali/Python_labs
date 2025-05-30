#Create an f-string:
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#A placeholder can contain variables, operations, functions, and modifiers to format the value.
price = 59
txt = f"The price is {price} dollars"
print(txt)

#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)