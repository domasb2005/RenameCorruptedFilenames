import os

# Define the mapping of corrupted to correct characters
char_map = {
    '╙': 'ė',
    '╥': 'ę',
    '╤': 'č',
    '╒': 'š',
    '╫': 'ū',
    '╓': 'ų',
    '╪': 'ž',
    '╛': 'Š',
    '╢': 'Č',
    # New additions
    '╜': 'Į',
    '╘': 'į',
    '╨': 'ą',
}


def replace_chars(original_name):
    # Replace each corrupted character using the mapping
    for corrupt, correct in char_map.items():
        original_name = original_name.replace(corrupt, correct)
    return original_name

def rename_files_in_directory(path):
    # Walk through all directories and files in the provided path
    for root, dirs, files in os.walk(path):
        for name in files:
            # Construct full file path
            old_file_path = os.path.join(root, name)
            # Replace corrupted characters in the file name
            new_name = replace_chars(name)
            new_file_path = os.path.join(root, new_name)
            # Rename the file
            print(f"Renaming file '{old_file_path}' to '{new_file_path}'")
            os.rename(old_file_path, new_file_path)

        for name in dirs:
            # Construct full directory path
            old_dir_path = os.path.join(root, name)
            # Replace corrupted characters in the directory name
            new_name = replace_chars(name)
            new_dir_path = os.path.join(root, new_name)
            # Rename the directory
            print(f"Renaming directory '{old_dir_path}' to '{new_dir_path}'")
            os.rename(old_dir_path, new_dir_path)

# Replace 'your_directory_path' with the path to the directory containing the folders and files you want to rename
your_directory_path = "C:\\Users\\domas\\Downloads\\VBE KURINIAI\\VBE KURINIAI"
rename_files_in_directory(your_directory_path)
