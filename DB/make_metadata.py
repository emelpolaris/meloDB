import os

# Path to the folder-db
folder_path = 'txt'

# Get the list of text files in the folder
file_list = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

# Create the metadata.list file and write the file metadata to it
with open('metadata.list', 'w') as metadata_file:
    for file_name in file_list:
        with open(os.path.join(folder_path, file_name), 'r') as text_file:
            file_content = text_file.read()
            metadata_file.write(f"{file_name}|EN-US|EN|{file_content}")
