import os
import sys

def count_files_by_extension(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")

        files = [file for file in os.listdir(directory)
 if os.path.isfile(os.path.join(directory, file))]

        extension_counts = {}
        for file in files:
            _, file_extension = os.path.splitext(file)
            extension_counts[file_extension] = extension_counts.get(file_extension, 0) + 1

        print(f"File counts by extension in {directory}:")
        for extension, count in extension_counts.items():
            print(f"{extension}: {count} file(s)")

        if not extension_counts:
            print("No files found in the directory.")

    except FileNotFoundError:
        print(f"Error: Directory not found - {directory}")
    except PermissionError:
        print(f"Error: No read permissions for the directory - {directory}")
    except Exception as e:
        print(f"Error: {e}")

def main():

    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    count_files_by_extension(directory_path)


main()