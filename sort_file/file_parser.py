import sys
from pathlib import Path


IMAGES = []
VIDEO = []
DOCUMENTS = []
AUDIO = []
OTHER = []
ARCHIVES = []


FOLDERS = []

REGISTER_EXTENSIONS = {
    'JPEG': IMAGES,
    'PNG': IMAGES,
    'JPG': IMAGES,
    'SVG': IMAGES,
    'AVI': VIDEO,
    'MP4': VIDEO,
    'MOV': VIDEO,
    'MKV': VIDEO,
    'DOC': DOCUMENTS,
    'DOCX': DOCUMENTS,
    'TXT': DOCUMENTS,
    'PDF': DOCUMENTS,
    'XLSX': DOCUMENTS,
    'PPTX': DOCUMENTS,
    'MP3': AUDIO,
    'OGG': AUDIO,
    'WAV': AUDIO,
    'AMR': AUDIO,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES,
    'ZIP': ARCHIVES,
}

EXTENSIONS = set()
UNKNOWN = set()

def get_extension(file_name: str) -> str:
    return Path(file_name).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue
        ext = get_extension(item.name)
        full_name = folder / item.name
        if not ext:
            OTHER.append(full_name)
        else:
            try:
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(full_name)
            except KeyError:
                UNKNOWN.add(ext)
                OTHER.append(full_name)


if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f'Start in folder{folder_for_scan}')

    scan(Path(folder_for_scan))
    print(IMAGES)
    print(VIDEO)
    print(DOCUMENTS)
    print(AUDIO)
    print(OTHER)
    print(ARCHIVES)

    print(f'There are files of types {EXTENSIONS}')
    print(f'Unknown files {UNKNOWN}')