import os

# Replace with the path to your directory
directory_path = "downloads"

def rename_files_in_directory(directory_path):
    # List all files in the directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # Sort the files by name
    files.sort()

    # Initialize a counter for renaming
    file_count = 1

    for old_filename in files:
        # Get the file extension
        file_extension = os.path.splitext(old_filename)[1]

        # Construct the new filename
        new_filename = f"{file_count:03d}{file_extension}"
        new_filepath = os.path.join(directory_path, new_filename)

        # Rename the file
        os.rename(os.path.join(directory_path, old_filename), new_filepath)

        print(f"Renamed: {old_filename} to {new_filename}")

        # Increment the counter
        file_count += 1

if __name__ == "__main__":
    rename_files_in_directory(directory_path)
