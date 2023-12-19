from pathlib import Path
from user_assistant.sort_file.file_sorter import FileSorter


def sort_files():
    try:
        folder_for_scan = input('Enter folder for scan: ')
        sorter = FileSorter(Path(folder_for_scan))
        sorter.sort_files()
    except (FileNotFoundError, OSError) as e:
        print(f'Error: {e}')