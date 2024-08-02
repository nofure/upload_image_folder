import os
import requests

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
            file_count += 1
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                # print(f"{indent}Directory: {item}")
                # Recursive call for subdirectory
                read_folder_recursive2(item,item_path, level + 1)
            # else:
            #     file_count += 1
                # print(f"{indent}{file_count} File: {item_path}")
        
        # Print file count for the current directory
        print(f"{indent}Total files in '{path}': {file_count}")
    except Exception as e:
        print(f"An error occurred: {e}")



def read_folder_recursive2(folderName,path, level):
    try:
        # print(f"{indent}Directory: {folderName}")
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
            if(item_path=="original"):
                if os.path.isdir(item_path):
                    print(f"{indent}Directory: {item}")
                    # Recursive call for subdirectory
                    read_folder_recursive2(item_path, level + 1)
                else:
                    file_count += 1
                    print(f"{indent}{file_count} File: {item_path}")
        
        # Print file count for the current directory
        # print(f"{indent}Total files in '{path}': {file_count}")
    except Exception as e:
        print(f"An error occurred: {e}")


def upload_image(file_path, api_url):
    try:
        with open(file_path, 'rb') as image_file:
            files = {'file': image_file}
            response = requests.post(api_url, files=files)
            
            # Check if the request was successful
            if response.status_code == 200:
                print("Image uploaded successfully.")
                print("Response:", response.json())
            else:
                print("Failed to upload image.")
                print("Status code:", response.status_code)
                print("Response:", response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to the folder you want to read
folder_path = "/Volumes/Macintosh HD/Users/notufure/Downloads/product"
api_url = "https://cloud.hangles.com/OpenApi/updateProduct"

# Call the function
read_folder_recursive(folder_path)
