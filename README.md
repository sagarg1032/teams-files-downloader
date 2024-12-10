# Teams Files Downloader

A Python script to copy all files from a Teams or SharePoint folder to a local destination.

## Prerequisites
Before running the script, ensure the following:
1. Navigate to the Teams channel where your files are stored.
2. Click on the **Files** tab in the channel.
3. Click the **Sync** button to sync the folder to your local system. This will create a local copy of the files on your computer, accessible via File Explorer (Windows) or Finder (Mac).
4. Note the local folder path where the files are stored (e.g., `C:\Users\SagarGupta\Teams Channel name\folder name`).

Once these steps are complete, you're ready to run the script.

## Features
- Recursively copies files and subfolders from the synced Teams folder.
- Handles permission errors gracefully.
- Automatically creates a timestamped destination folder.

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/teams-files-downloader.git

2. Ensure Python is installed on your system. If not, download it from the official Python website and add it to your system's PATH.

## Usage

### Steps to Run the Script:
1. Sync the Teams folder to your local system (see **Prerequisites** section).
2. Open your terminal or command prompt.
3. Navigate to the directory where the script is located.
   ```bash
   cd /path/to/your/script
4. Run the script using Python:
   ```bash
   python teams_downloader.py
5. Follow the on-screen prompts:
   <b>Enter the source folder path </b>: This is the path to your synced Teams folder (e.g., C:/Users/YourName/Teams/ChannelName).
   <b>Enter the destination folder path</b>: The folder where you want to save the copied files (e.g., D:/Downloads).
   <b>Enter the folder name </b>: Provide a name for the new folder where files will be copied.

## Example Output

```bash
Please enter the source folder path in Teams: "C:\Users\SagarGupta\Teams Channel name\folder name"
Please enter the folder path of your downloads folder: "C:\Users\SagarGupta\Downloads"
Please enter the folder name: All_performance_decks
Destination folder created at: C:\Users\SagarGupta\Downloads\All_performance_decks
Copied C:\Users\SagarGupta\Teams Channel name\folder name\File1.pptx to C:\Users\SagarGupta\Downloads\All_performance_decks\File1.pptx
Copied C:\Users\SagarGupta\Teams Channel name\folder name\Folder1\File2.pptx to C:\Users\SagarGupta\Downloads\All_performance_decks\Folder1\File2.pptx
...
Copy completed. All files are in 'C:\Users\SagarGupta\Downloads\All_performance_decks'.
Verified: Destination folder exists at C:\Users\SagarGupta\Downloads\All_performance_decks.

Process finished with exit code 0