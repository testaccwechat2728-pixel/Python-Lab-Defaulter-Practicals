"""
Practical No. 9: File Manipulations in Python
Operations: Open, Close, Read, Write, Append, and Copy from one file to another.
"""

import shutil
import os

# Define file paths
source_file = 'source.txt'
destination_file = 'destination.txt'
append_file = 'append_file.txt'

def perform_file_operations():
    # 1. Open, Write, and Read from Source File
    print("After Writing and Reading from the Source File:")
    try:
        # Open file in write mode (creates a new file or overwrites existing)
        with open(source_file, 'w') as file:
            file.write('This is the original content.\n')
            file.write('Adding some more text.')

        # Open file in read mode to display contents
        with open(source_file, 'r') as file:
            content = file.read()
            print("Read content from source file:")
            print(content)
    except IOError as e:
        print(f"Error opening/reading file: {e}")

    # 2. Append to a File
    print("\nAfter Appending to the Source File:")
    try:
        # Open file in append mode (adds to the end of the file)
        with open(source_file, 'a') as file:
            file.write('\nAppending new content.')

        # Verify appending by reading the file again
        with open(source_file, 'r') as file:
            content = file.read()
            print("Content after appending:")
            print(content)
    except IOError as e:
        print(f"Error opening/reading/appending file: {e}")

    # 3. Copy Content from One File to Another
    print("\nAfter Copying the Source File to the Destination File:")
    try:
        # Copy the content from source_file to destination_file
        shutil.copy(source_file, destination_file)
        print(f"File copied from {source_file} to {destination_file}. Content of the destination file:")

        # Verify copy by reading the destination file
        with open(destination_file, 'r') as file:
            content = file.read()
            print(content)
    except IOError as e:
        print(f"Error copying file: {e}")

if __name__ == "__main__":
    perform_file_operations()
