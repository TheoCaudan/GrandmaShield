import os
import shutil
import time
from datetime import datetime

def cleanup_downloads(download_dir, archive_dir, days=7):
    current_time = time.time()
    date_time = datetime.fromtimestamp(current_time)
    # Formatte la date pour le nom du dossier d'archives qui sera généré
    formatted_date = date_time.strftime('%Y-%m-%d') 
    archive_folder = os.path.join(archive_dir, f"Archive_{formatted_date}")
    os.makedirs(archive_folder, exist_ok=True)
    # Bouge les fichiers de plus de 7 jours dans un nouveau dossier d'archives
    for root, _, files in os.walk(download_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if os.stat(file_path).st_mtime < current_time - days * 86400:
                shutil.move(file_path, os.path.join(archive_folder, file))
                print(f"Archived {file} to {archive_folder}")

# Changer les chemins afin qu'ils correspondent aux dossiers que vous souhaiter archiver 
download_dir = "C:/Users/YourUsername/Downloads"
archive_dir = "C:/Users/YourUsername/Archives" 
cleanup_downloads(download_dir, archive_dir)
