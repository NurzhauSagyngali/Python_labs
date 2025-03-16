def write_list_to_file(file_path, list):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in list:
            file.write(f"{item}\n")  
    print(file_path)


example = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

file_path = r'C:\Users\1111\Desktop\python\lab 6\dir-and-files\example.txt'

write_list_to_file(file_path, example)
