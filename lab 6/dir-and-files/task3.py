import os

def check_path(path):
    if os.access(path, os.F_OK):
        print(f"The path exists: {path}\n")

        directory = os.path.dirname(path)
        print(f"Directory: {directory}")

        
        filename = os.path.basename(path)
        print(f"Filename: {filename}")
    else:
        print(f"The path does not exist: {path}")

specified_path = r'C:\Users\1111\Desktop\python\lab 6'
check_path(specified_path)
