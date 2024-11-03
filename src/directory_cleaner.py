import os

def remove_empty_files_and_dirs(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        # Supprime les fichiers de taille nulle
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) == 0: 
                os.remove(file_path)
                print(f"Deleted empty file: {file_path}")

        # Supprime les dossiers vides
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                os.rmdir(dir_path) 
                print(f"Deleted empty directory: {dir_path}")
            except OSError as e:
                pass

# Changer le chemin pour qu'il pointe vers le dossier a nettoyer
directory_to_clean = "C:/Users/path/to/your/directory"
remove_empty_files_and_dirs(directory_to_clean)
