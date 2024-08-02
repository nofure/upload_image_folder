import os
# import requests
# def upload(filename):
#     url = "https://hangles-env.com/api/uploadFile"

#     payload = {'type': 'product'}
#     files=[
#     ('file',('banner เตือนภัย.png',open('/Users/notufure/Downloads/banner เตือนภัย.png','rb'),'image/png'))
#     ]
#     headers = {
#     'Authorization': '••••••'
#     }

#     response = requests.request("POST", url, headers=headers, data=payload, files=files)

#     print(response.text)
def is_image_file(filename):
    # Define image file extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
    return any(filename.lower().endswith(ext) for ext in image_extensions)

def list_image_files(folder_path):
    try:
        items = os.listdir(folder_path)
        image_files = [item for item in items if os.path.isfile(os.path.join(folder_path, item)) and is_image_file(item)]
        if not image_files:
            print(f"  No image files found in '{folder_path}'.")
        else:
            for image_file in image_files:
                print(f"  {os.path.join(folder_path, image_file)}")
    except Exception as e:
        print(f"Error reading folder '{folder_path}': {e}")

def search_files(base_path):
    try:
        # List all immediate subdirectories under the base path
        immediate_subdirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
        
        for subdir in immediate_subdirs:
            subdir_path = os.path.join(base_path, subdir)
            thumbnail_folder_path = os.path.join(subdir_path, 'other', 'thumbnail')
            original_folder_path = os.path.join(subdir_path, 'original')
            
            print(f"\nLevel 1 Folder: {subdir}")
            
            if os.path.isdir(thumbnail_folder_path):
                print(f" 'Thumbnail' folder found at: {thumbnail_folder_path}")
                print(f" Files in 'thumbnail' folder:")
                list_image_files(thumbnail_folder_path)
            elif os.path.isdir(original_folder_path):
                print(f" 'Thumbnail' folder not found. Showing files in 'original' folder at: {original_folder_path}")
                list_image_files(original_folder_path)
            else:
                print(f" Neither 'thumbnail' nor 'original' folders found in: {subdir_path}")
    except Exception as e:
        print(f"Error accessing base path: {e}")

# Example usage
base_path = "/Volumes/Macintosh HD/Users/notufure/Downloads/product3"  # Replace with your base folder path
search_files(base_path)
# python3 read_folder_in_original.py 