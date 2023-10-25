import os

# Folder path where the files are located
folder_path = 'downloads/'

# List all files in the folder
files = os.listdir(folder_path)

# Iterate through the files and change the extension from .mp4 to .mp3
for file in files:
    if file.endswith('.mp4'):
        new_name = os.path.splitext(file)[0] + '.mp3'
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)

        print(f"Renamed: {file} to {new_name}")

print("File extension change completed.")