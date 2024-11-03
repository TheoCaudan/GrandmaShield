import os
import hashlib

def get_file_hash(file_path):
    hasher = hashlib.sha256() 
    # Recupere le hash du fichier
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_duplicates(directory):
    hashes = {}
    duplicates = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)
            if file_hash in hashes:
                duplicates.append((file_path, hashes[file_hash]))
            else:
                hashes[file_hash] = file_path
    return duplicates

def delete_duplicates(duplicates):
    for duplicate, original in duplicates:
        os.remove(duplicate)
        print(f"Deleted duplicate: {duplicate} (Original: {original})")

# Changer le chemin pour qu'il pointe vers le dossier a nettoyer
directory = "C:/path/to/your/directory"
duplicates = find_duplicates(directory)
delete_duplicates(duplicates)
