

'Interview que: How to find how many file or high file in in folder with same extension python '

import os
from collections import Counter

def count_files_by_extension(folder_path):
    """
    Counts the number of files for each unique extension in a given folder.

    Args:
        folder_path (str): The path to the folder to analyze.

    Returns:
        dict: A dictionary where keys are file extensions (e.g., '.txt', '.py')
              and values are the counts of files with that extension.
    """
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return {}

    extensions = []
    for filename in os.listdir(folder_path):
        print(f'file name: {filename}')
        file_path = os.path.join(folder_path, filename)
        print(f'file path: {file_path}')
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            if ext:  # Only add if an extension exists
                extensions.append(ext.lower())  # Convert to lowercase for consistency

    extension_counts = Counter(extensions)
    return dict(extension_counts)

# Example usage:
folder = "/Users/samirb/Documents/WorkSpace/PythonWS/PythonWorkspace/src/PyDSA"  # Replace with the actual path to your folder
counts = count_files_by_extension(folder)

if counts:
    print(f"File counts by extension in '{folder}':")
    for ext, count in counts.items():
        print(f"  {ext}: {count} files")


#explaination:
# ✔ Why in this case: Developers use _ when they must assign a value (because unpacking requires it)
# but they don’t actually care about that value.
#
#example:
# _, ext = os.path.splitext(filename)
#
# os.path.splitext(filename) returns two values:
#
# * the filename without extension
# * the extension
#
# But if you only want the extension, you still need to unpack both values.
# So:
# *  _ = unnecessary value (ignored)
# * ext = useful value (the extension)