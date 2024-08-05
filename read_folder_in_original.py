import os
import requests

# Dictionary to store folder_id -> image_url mapping
folder_image_urls = {}

def update_product():
    url = "https://cloud.hangles.com/OpenApi/updateProduct"
    
    headers = {
        'X-Authorization': 'Bearer bxcdiyOoCxRiSza0OKINJ9rUU7Vu3uWFvoXE5ASFVeSZ9i67Ez'
    }

    for folder_id, image_urls in folder_image_urls.items():
        # Prepare the payload with dynamic image URLs
        payload = {
            'data[0][product_id]': folder_id,
            'data[0][image_url]': image_urls[0] if image_urls else '',  # Primary image URL
        }

        # Dynamically add arr_image_url fields
        # for index, image_url in enumerate(image_urls):
        #     payload[f'data[0][arr_image_url][{index}]'] = image_url
        
        files = []
        try:
            print(f"payload {payload}")
            response = requests.post(url, headers=headers, data=payload, files=files)
            response.raise_for_status()  # Raise an exception for HTTP error responses
            print(f"Updated product {folder_id}: {response.text}")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred while updating product {folder_id}: {http_err}")
        except Exception as err:
            print(f"Other error occurred while updating product {folder_id}: {err}")

def upload_image(folder_id, image_path, image_name):
    # print(f"Uploading image '{image_name}'.")
    # print(f"Image path: '{image_path}'.")

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
        
        # Extract and store the URL from the 'data' field
        image_url = response_json.get('data')
        if image_url:
            # print(f"Uploaded image URL: {image_url}")
            if folder_id not in folder_image_urls:
                folder_image_urls[folder_id] = []
            folder_image_urls[folder_id].append(image_url)
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

def list_image_files(folder_id, folder_path, is_thumbnail=False):
    try:
        # print(f"\nLevel 1 Folder: {folder_id}")
        items = os.listdir(folder_path)
        # Filter and sort image files by name
        image_files = sorted(
            [item for item in items if os.path.isfile(os.path.join(folder_path, item)) and is_image_file(item)]
        )
        if not image_files:
            print(f"  No image files found in '{folder_path}'.")
        else:
            for image_file in image_files:
                upload_image(folder_id, os.path.join(folder_path, image_file), image_file)
                if is_thumbnail:
                    # Add the image URL to the folder_image_urls at index 0
                    folder_image_urls[folder_id].insert(0, folder_image_urls[folder_id].pop())
    except Exception as e:
        print(f"Error reading folder '{folder_path}': {e}")

def search_files(base_path):
    try:
        # List all immediate subdirectories under the base path
        immediate_subdirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
        
        for subdir in immediate_subdirs:
            subdir_path = os.path.join(base_path, subdir)
            original_folder_path = os.path.join(subdir_path, 'original')
            
            if os.path.isdir(original_folder_path):
                list_image_files(subdir, original_folder_path)
            else:
                print(f" 'original' folder not found in: {subdir_path}")

        # After processing all files, update product information
        update_product()
    
    except Exception as e:
        print(f"Error accessing base path: {e}")

def show():
    print(f"folder_image_urls  {folder_image_urls}")

# Example usage
base_path = r'C:\Users\nice_voxngola\Downloads\product'   # Replace with your base folder path
search_files(base_path)
