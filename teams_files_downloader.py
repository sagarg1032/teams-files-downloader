import os
import shutil
from datetime import datetime
import sys
import re

# Check Python version compatibility
if sys.version_info < (3, 8):
    print("Error: Python 3.8 or newer is required for this script.")
    exit(1)

# Enter the Source Folder Path
source_path_input = input("Please enter the source folder path in Teams: ")

# Remove any double quotes from the source_path_input
source_folder = source_path_input.strip().replace('"', '')

# Check if the source folder exists
if not os.path.exists(source_folder):
    print(f"Error: Source folder does not exist at {source_folder}")
    exit(1)

# Check if the source folder is a valid directory
if not os.path.isdir(source_folder):
    print(f"Error: {source_folder} is not a valid directory.")
    exit(1)

# Enter the Destination Folder Path
folder_path_input = input("Please enter the folder path of your downloads folder: ")

# Remove any double quotes from the input folder path
folder_path = folder_path_input.strip().replace('"', '')

# Check if the folder path exists
if not os.path.isdir(folder_path):
    print(f"Error: {folder_path} is not a valid directory.")
    exit(1)

# Create a new folder in the provided folder path
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
new_folder_name = input("Please enter the folder name: ")

# Sanitize folder name to avoid invalid characters
invalid_chars = r'[<>:"/\\|?*]'
if re.search(invalid_chars, new_folder_name):
    print(f"Error: Folder name '{new_folder_name}' contains invalid characters.")
    exit(1)

destination_folder = os.path.join(folder_path, new_folder_name)

# Ensure the destination folder exists
try:
    os.makedirs(destination_folder, exist_ok=True)
    print(f"Destination folder created at: {destination_folder}\n")
except PermissionError as e:
    print(f"PermissionError: Unable to create destination folder. {e}")
    exit(1)
except Exception as e:
    print(f"Error: {e}")
    exit(1)

# Define the function to copy files
def copy_files(src, dest):
    # Check if source folder is empty (Added)
    if not os.listdir(src):
        print(f"Error: Source folder '{src}' is empty.")
        exit(1)
    
    # Iterate through all files and subdirectories in the source folder
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)

        # Add long path support for Windows
        if os.name == 'nt':
            s = f"\\\\?\\{s}"
            d = f"\\\\?\\{d}"

        try:
            if os.path.isdir(s):
                # Recursively copy subdirectories
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                # Copy files
                shutil.copy2(s, d)
                print(f"Copied {s} to {d}")
        except PermissionError as e:
            print(f"PermissionError: {e}. Skipping {s}.")
            # Log the error to a file (Added)
            with open("error_log.txt", "a") as log_file:
                log_file.write(f"PermissionError copying {s}: {e}\n")
        except Exception as e:
            print(f"Error: {e}. Skipping {s}.")
            # Log the error to a file (Added)
            with open("error_log.txt", "a") as log_file:
                log_file.write(f"Error copying {s}: {e}\n")

# Copy the files
copy_files(source_folder, destination_folder)

print("\nCopy completed. All files are in '{destination_folder}'.\n")

# Verify folder creation
if os.path.exists(destination_folder):
    print(f"Verified: Destination folder exists at {destination_folder}")
else:
    print(f"Error: Destination folder does not exist at {destination_folder}")