import os

def read_folder_recursive(path, level=0):
    try:
        # Check if the provided path is a directory
        if not os.path.isdir(path):
            print(f"The path '{path}' is not a valid directory.")
            return
        
        # List the contents of the directory
        contents = os.listdir(path)
        indent = ' ' * 4 * level  # Indentation for subdirectories
        file_count = 0
        
        # Print directory information
        print(f"{indent}Contents of the folder '{path}':")
        for item in contents:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(f"{indent}Directory: {item}")
                # Recursive call for subdirectory
                read_folder_recursive(item_path, level + 1)
            else:
                file_count += 1
                print(f"{indent}File: {item}")
        
        # Print file count for the current directory
        print(f"{indent}Total files in '{path}': {file_count}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to the folder you want to read
folder_path = "/Volumes/Macintosh HD/Users/notufure/Downloads/product"

# Call the function
read_folder_recursive(folder_path)
