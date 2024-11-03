import shutil
import os

def backup_files(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for root, _, files in os.walk(src_dir):
        for file in files:
            file_path = os.path.join(root, file)
            dest_path = os.path.join(dest_dir, os.path.relpath(file_path, src_dir))
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(file_path, dest_path)
            print(f"Copied {file_path} to {dest_path}")

# ///////////////////////////////
src_dir = "C:/path/to/documents"
dest_dir = "Z:/Backup/Documents"
backup_files(src_dir, dest_dir)
