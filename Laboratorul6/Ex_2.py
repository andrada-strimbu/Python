import os
import sys


def rename_files_with_sequence(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")

        files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

        for index, filename in enumerate(files, start=1):
            original_path = os.path.join(directory, filename)
            new_filename = f"file{index}{os.path.splitext(filename)[1]}"
            new_path = os.path.join(directory, new_filename)
            os.rename(original_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    rename_files_with_sequence(directory_path)


main()