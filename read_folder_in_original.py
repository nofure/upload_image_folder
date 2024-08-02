import os
import requests


def update_product():
    url = "https://cloud.hangles.com/OpenApi/updateProduct"

    payload = {'data[0][product_id]': '240600003200004',
    'data[0][image_url]': '00',
    'data[0][arr_image_url][0]': '0',
    'data[0][arr_image_url][1]': '1',
    'data[0][arr_image_url][2]': '2',
    'data[0][arr_image_url][3]': '3',
    'data[0][arr_image_url][4]': '4',
    'data[0][arr_image_url][5]': '5'}
    files=[

    ]
    headers = {
    'X-Authorization': 'Bearer bxcdiyOoCxRiSza0OKINJ9rUU7Vu3uWFvoXE5ASFVeSZ9i67Ez'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

def upload_iamge(image_path,image_name):
    print(f"Uploading image '{image_name}'.")
    print(f"Image path: '{image_path}'.")

    url = "https://hangles-env.com/api/uploadFile"

    # Determine the content type dynamically based on the file extension
    _, ext = os.path.splitext(image_name)
    content_type = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.bmp': 'image/bmp',
        '.tiff': 'image/tiff'
    }.get(ext.lower(), 'application/octet-stream')

    payload = {'type': 'product'}
    files = [
        ('file', (image_name, open(image_path, 'rb'), content_type))
    ]
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwaGVlcmFwaGF0eCIsInJvbGVzIjpbIlVzZXIiXSwiaXNzIjoiaHR0cDovL2hhbmdsZXNhcGktZW52LTUuYXAtc291dGhlYXN0LTEuZWxhc3RpY2JlYW5zdGFsay5jb20vYXBpL2xvZ2luIn0.FVsoF_N9t_Rb3KUkzvCMeTkGXh4pJZKymvitrWJ-NsM'
    }

    try:
        response = requests.post(url, headers=headers, data=payload, files=files)
        response.raise_for_status()  # Raise an exception for HTTP error responses
        
        # Parse the JSON response
        response_json = response.json()
        
        # Extract and print the URL from the 'data' field
        image_url = response_json.get('data')
        if image_url:
            print(f"Uploaded image URL: {image_url}")
        else:
            print("No URL returned in response data.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    finally:
        # Ensure the file is closed after uploading
        files[0][1][1].close()


def is_image_file(filename):
    # Define image file extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
    return any(filename.lower().endswith(ext) for ext in image_extensions)

def list_image_files(folder_id,folder_path):
    try:
        print(f"\nLevel 1 Folder: {folder_id}")
        items = os.listdir(folder_path)
        image_files = [item for item in items if os.path.isfile(os.path.join(folder_path, item)) and is_image_file(item)]
        if not image_files:
            print(f"  No image files found in '{folder_path}'.")
        else:
            for image_file in image_files:
                # print(f"  {os.path.join(folder_path, image_file)}")
                # print(f"{image_file}")
                upload_iamge(os.path.join(folder_path, image_file),image_file)
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
            
            # print(f"\nLevel 1 Folder: {subdir}")
            
            if os.path.isdir(thumbnail_folder_path):
                # print(f" 'Thumbnail' folder found at: {thumbnail_folder_path}")
                # print(f" Files in 'thumbnail' folder:")
                list_image_files(subdir,thumbnail_folder_path)
            elif os.path.isdir(original_folder_path):
                # print(f" 'Thumbnail' folder not found. Showing files in 'original' folder at: {original_folder_path}")
                list_image_files(subdir,original_folder_path)
            else:
                print(f" Neither 'thumbnail' nor 'original' folders found in: {subdir_path}")
    except Exception as e:
        print(f"Error accessing base path: {e}")

# Example usage
base_path = r'C:\Users\nice_voxngola\Downloads\product'   # Replace with your base folder path
search_files(base_path)
# python3 read_folder_in_original.py 