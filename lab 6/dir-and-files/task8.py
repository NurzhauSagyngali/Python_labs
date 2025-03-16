import os

def delete_file(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return
    
    # Check access permissions (read and write)
    if not os.access(file_path, os.R_OK):
        print(f"No read permission for the file {file_path}.")
        return
    if not os.access(file_path, os.W_OK):
        print(f"No write permission to delete the file {file_path}.")
        return

    try:
        os.remove(file_path)
        print(f"The file {file_path} has been successfully deleted.")
    except Exception as e:
        print(f"Error deleting the file: {e}")


file_path = r"C:\Users\1111\Desktop\python\lab 6\dir-and-files\deleting.txt"

delete_file(file_path)
