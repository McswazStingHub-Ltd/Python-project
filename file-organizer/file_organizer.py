import os
import shutil

FOLDERS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
}

source = input("Enter the folder to organize: ").strip()

if not os.path.isdir(source):
    print("Folder not found.")
    exit()

for filename in os.listdir(source):
    filepath = os.path.join(source, filename)

    if os.path.isdir(filepath):
        continue

    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    moved = False

    for folder, extensions in FOLDERS.items():
        if ext in extensions:
            destination = os.path.join(source, folder)
            os.makedirs(destination, exist_ok=True)
            shutil.move(filepath, os.path.join(destination, filename))
            print(f"Moved {filename} -> {folder}")
            moved = True
            break

    if not moved:
        other = os.path.join(source, "Others")
        os.makedirs(other, exist_ok=True)
        shutil.move(filepath, os.path.join(other, filename))
        print(f"Moved {filename} -> Others")

print("\nOrganization complete!")
