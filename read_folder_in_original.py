import os

def search_for_direct_original_folders(base_path):
    try:
        # List all immediate subdirectories under the base path
        immediate_subdirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
        
        for subdir in immediate_subdirs:
            subdir_path = os.path.join(base_path, subdir)
            original_folder_path = os.path.join(subdir_path, 'original')
            
            if os.path.isdir(original_folder_path):
                print(f"\nFound 'original' folder at: {original_folder_path}")
                
                try:
                    # List all items in the "original" folder
                    items = os.listdir(original_folder_path)
                    print(f"Files in 'original' folder at '{original_folder_path}':")
                    
                    # Filter and print only files
                    file_list = [item for item in items if os.path.isfile(os.path.join(original_folder_path, item))]
                    if not file_list:
                        print("  No files found.")
                    else:
                        for file in file_list:
                            print(f"  {file}")
                except Exception as e:
                    print(f"Error reading folder: {e}")
    except Exception as e:
        print(f"Error accessing base path: {e}")

# Example usage
base_path = "/Volumes/Macintosh HD/Users/notufure/Downloads/product"  # Replace with your base folder path
search_for_direct_original_folders(base_path)
