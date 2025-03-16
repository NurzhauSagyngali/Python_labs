def copy_file(file, copyoffile):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()  
    with open(copyoffile, 'w', encoding='utf-8') as c:
        c.write(content)  

old = r'C:\Users\1111\Desktop\python\lab 6\dir-and-files\file.txt'
new_one = r'C:\Users\1111\Desktop\python\lab 6\dir-and-files\copyoffile.txt'


copy_file(old, new_one)
