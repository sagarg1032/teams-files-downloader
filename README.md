# Teams Files Downloader

## Overview
This Python script enables users to copy all files and subdirectories from a specified source folder to a destination folder. It ensures error handling, supports long paths on Windows, and validates user inputs to create a reliable and user-friendly experience.



## Features
- Supports long paths on Windows (paths longer than 260 characters).
- Logs errors like permission issues to `error_log.txt` for troubleshooting.
- Recursively copies files and directories, preserving the folder structure.
- Validates folder paths and names to prevent invalid inputs.
- Ensures compatibility with Python 3.8 and above.



## Prerequisites
Before running the script, ensure the following:
1. Navigate to the Teams channel where your files are stored.
2. Click on the **Files** tab in the channel.
3. Click the **Sync** button to sync the folder to your local system. This will create a local copy of the files on your computer, accessible via File Explorer (Windows) or Finder (Mac).
4. Note the local folder path where the files are stored (e.g., `C:\Users\SagarGupta\Teams Channel name\folder name`).

Once these steps are complete, you're ready to run the script.

Note: **Learn how to sync Teams files**: Follow [this guide](https://techcommunity.microsoft.com/blog/microsoftteamscommunityblog/how-to-sync-teams-files-to-local-computer/3671933) for step-by-step instructions.



## Requirements
- **Python Version**: Python 3.8+
- **Modules Used**:
  - `os`
  - `shutil`
  - `datetime`
  - `sys`
  - `re`



## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/teams-files-downloader.git
   ```


2. Ensure Python is installed on your system. If not, download it from the official Python website and add it to your system's PATH.


## Usage

### Steps to Run the Script:
1. Sync the Teams folder to your local system (see **Prerequisites** section).
2. Open your terminal or command prompt.
3. Clone the repository or download the script.
5. Navigate to the directory where the script is located.
   ```bash
   cd /path/to/your/script
   ```
4. Run the script using Python:
   ```bash
   python teams_files_downloader.py
   ```
5. Follow the on-screen prompts:
   - <b>Please enter the source folder path in Teams</b>: This is the path to your synced Teams folder (e.g., C:/Users/YourName/Teams/ChannelName).
   - <b>Please enter the folder path of your downloads folder</b>: The folder where you want to save the copied files (e.g., D:/Downloads).
   - <b>Please enter the folder name</b>: Provide a name for the new folder where files will be copied.


## Example Input
```plaintext
Please enter the source folder path in Teams: C:/Users/YourName/Teams/ChannelName/source_folder
Please enter the folder path of your downloads folder: C:/Users/YourName/destination_folder
Please enter the folder name: Teams_data2024
```


## Example Output
```plaintext
Destination folder created at: C:/Users/YourName/destination_folder/Teams_data2024
Copied C:/Users/YourName/Teams/ChannelName/source_folder/file1.txt to C:/Users/YourName/destination_folder/Teams_data2024/file1.txt
PermissionError: [Errno 13] Permission denied: 'C:/Users/YourName/Teams/ChannelName/source_folder/protected_file.txt'. Skipping C:/Users/YourName/Teams/ChannelName/source_folder/protected_file.txt.
Copy completed. All files are in 'C:/Users/YourName/destination_folder/Teams_data2024'.
Verified: Destination folder exists at C:/Users/YourName/destination_folder/Teams_data2024
```

**Error Log (`error_log.txt`):**
```plaintext
PermissionError copying C:/Users/YourName/Teams/ChannelName/source_folder/protected_file.txt: [Errno 13] Permission denied: 'C:/Users/YourName/Teams/ChannelName/source_folder/protected_file.txt'
```


## How It Works
1. **Input Validation**:
   - Checks if the source folder exists and is valid.
   - Validates destination folder paths and ensures folder names don’t contain invalid characters.

2. **Folder Creation**:
   - Creates a new folder in the specified destination path.
   - Handles errors like `PermissionError` during folder creation.

3. **Copy Process**:
   - Recursively copies directories and files using `shutil.copytree` and `shutil.copy2`.
   - Adds long path support for Windows to handle paths exceeding 260 characters.

4. **Error Handling and Logging**:
   - Logs errors such as permission issues to `error_log.txt`.
   - Skips inaccessible files without stopping the entire process.


## Contributions
Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your branch.
4. Open a pull request.


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
- **Sagar Gupta**
- GitHub: [sagarg1032](https://github.com/sagarg1032) - Explore more projects and contributions.


## Feedback
For any bugs, suggestions, or feature requests, feel free to open an issue on GitHub or reach out to me.

---

**Happy Coding!**