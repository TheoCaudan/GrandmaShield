# Importing functions from each of the scripts
from automatic_backup import backup_files
from downloads_cleaner import cleanup_downloads
from directory_cleaner import remove_empty_files_and_dirs
from dpl_handler import find_duplicates, delete_duplicates
from file_organizer import organize_files_by_type, organize_files_by_date
from security_wholesome import run_security_check

# Directories to use
SRC_DIR = "C:/path/to/documents"  # Source directory for backup
DEST_DIR = "Z:/Backup/Documents"  # Backup destination
DOWNLOADS_DIR = "C:/Users/YourUsername/Downloads"  # Downloads directory
ARCHIVE_DIR = "C:/Users/YourUsername/Archives"  # Archive directory
CLEANUP_DIR = "C:/path/to/clean"  # Directory for cleanup and organization

def main_maintenance():
    # 1. Clean up old downloads
    print("Starting Downloads Cleanup...")
    cleanup_downloads(DOWNLOADS_DIR, ARCHIVE_DIR, days=7)

    # 2. Remove empty files and directories
    print("Removing empty files and directories...")
    remove_empty_files_and_dirs(CLEANUP_DIR)

    # 3. Find and delete duplicate files
    print("Finding and deleting duplicate files...")
    duplicates = find_duplicates(CLEANUP_DIR)
    delete_duplicates(duplicates)

    # 4. Organize files by type and date
    print("Organizing files by type...")
    organize_files_by_type(CLEANUP_DIR)

    print("Organizing files by modification date...")
    organize_files_by_date(CLEANUP_DIR)

    # 5. Backup important files
    print("Starting Backup...")
    backup_files(SRC_DIR, DEST_DIR)

    # 6. Run security checks
    print("Running Security Check...")
    run_security_check()

    print("System maintenance and security check complete.")

# Run the maintenance script
if __name__ == "__main__":
    print("Maintenance process started...")
    main_maintenance()
    print("All tasks completed successfully.")
