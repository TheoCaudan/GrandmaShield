import os
import shutil
from datetime import datetime

def organize_files_by_type(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1][1:] 
            target_folder = os.path.join(directory, file_extension.upper())
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, file))
            print(f"Moved {file} to {target_folder}")

def organize_files_by_date(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            date_folder = modified_time.strftime('%Y-%m')
            target_folder = os.path.join(directory, date_folder)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, file))
            print(f"Moved {file} to {target_folder}")

# Changer le chemin pour qu'il pointe vers le dossier a organiser
directory = "C:/Users/path/to/your/directory"

# Mettre en commentaire selon l'option souhaitée
organize_files_by_type(directory)
# organize_files_by_date(directory) 
