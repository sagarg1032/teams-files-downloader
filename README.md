# Teams Files Downloader

A Python script to copy all files from a Teams or SharePoint folder to a local destination.

## Prerequisites
Before running the script, ensure the following:
1. Navigate to the Teams channel where your files are stored.
2. Click on the **Files** tab in the channel.
3. Click the **Sync** button to sync the folder to your local system. This will create a local copy of the files on your computer, accessible via File Explorer (Windows) or Finder (Mac).
4. Note the local folder path where the files are stored (e.g., `C:/Users/YourName/Teams/ChannelName`).

Once these steps are complete, you're ready to run the script.

## Features
- Recursively copies files and subfolders from the synced Teams folder.
- Handles permission errors gracefully.
- Automatically creates a timestamped destination folder.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/teams-files-downloader.git

## Install Python (if not already installed) and then Run the script.
