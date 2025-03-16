import os
import string  # for generating alphabet

folder_path = r'C:\Users\1111\Desktop\python\lab 6\A-Z.txts'

for letter in string.ascii_uppercase: 
    file_path = os.path.join(folder_path, f"{letter}.txt")  
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"This is file {letter}.txt\n")  

print(folder_path)
