import os

def is_image_file(filename):
    # Define image file extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
    return any(filename.lower().endswith(ext) for ext in image_extensions)

def search_for_images_in_original(base_path):
    try:
        # List all immediate subdirectories under the base path
        immediate_subdirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
        
        for subdir in immediate_subdirs:
            subdir_path = os.path.join(base_path, subdir)
            original_folder_path = os.path.join(subdir_path, 'original')
            
            if os.path.isdir(original_folder_path):
                print(f"\nLevel 1 Folder: {subdir}")
                # print(f"'Original' folder path: {original_folder_path}")
                
                try:
                    # List all items in the "original" folder
                    items = os.listdir(original_folder_path)
                    image_files = [item for item in items if os.path.isfile(os.path.join(original_folder_path, item)) and is_image_file(item)]
                    
                    if not image_files:
                        print("  No image files found.")
                    else:
                        for image_file in image_files:
                            image_path = os.path.join(original_folder_path, image_file)
                            print(f"  Image file path: {image_path}")
                except Exception as e:
                    print(f"  Error reading 'original' folder: {e}")
    except Exception as e:
        print(f"Error accessing base path: {e}")

# Example usage
base_path = "/Volumes/Macintosh HD/Users/notufure/Downloads/product"  # Replace with your base folder path
search_for_images_in_original(base_path)
