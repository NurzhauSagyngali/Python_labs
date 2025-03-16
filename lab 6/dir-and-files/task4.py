import os

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = sum(1 for line in file)
        print(f"The file '{file_path}' contains {line_count} lines.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = r'C:\Users\1111\Desktop\python\lab 6\dir-and-files\example.txt'

if os.path.exists(file_path):
    count_lines_in_file(file_path)
else:
    print(f"File '{file_path}' does not exist!")
