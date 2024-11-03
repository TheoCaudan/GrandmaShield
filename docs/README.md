# *This project is on testing*


# Utility Scripts for File Management, Backup, and Security

This repository contains a series of Python scripts that automate various tasks such as backing up files, organizing directories, cleaning up downloads, and performing basic security checks. Below is a brief overview of each script and how to use them.

---

## Table of Contents
1. [Backup Files Script](#backup-files-script)
2. [Clean Empty Files and Directories Script](#clean-empty-files-and-directories-script)
3. [Cleanup Downloads Script](#cleanup-downloads-script)
4. [Duplicate File Finder Script](#duplicate-file-finder-script)
5. [Organize Files Script](#organize-files-script)
6. [Security Monitoring Script](#security-monitoring-script)
7. [Setup Instructions](#setup-instructions)

---

### Backup Files Script

This script backs up files from a source directory to a specified destination directory. It copies all files, retaining the folder structure.

- **File**: `backup_files.py`
- **Function**: Copies all files from `src_dir` to `dest_dir`.
- **Usage**:
    ```python
    src_dir = "C:/path/to/documents"
    dest_dir = "Z:/Backup/Documents"
    backup_files(src_dir, dest_dir)
    ```
- **Example Output**: `Copied C:/path/to/documents/file.txt to Z:/Backup/Documents/file.txt`

---

### Clean Empty Files and Directories Script

This script searches for and removes empty files and directories within a specified directory.

- **File**: `remove_empty_files_and_dirs.py`
- **Function**: Deletes files with zero bytes and removes empty directories.
- **Usage**:
    ```python
    directory_to_clean = "C:/path/to/your/directory"
    remove_empty_files_and_dirs(directory_to_clean)
    ```
- **Example Output**: `Deleted empty file: C:/path/to/file.txt`

---

### Cleanup Downloads Script

Moves files older than a specified number of days from the downloads folder to an archive folder with the current date.

- **File**: `cleanup_downloads.py`
- **Function**: Archives files from `download_dir` older than `days` days to `archive_dir`.
- **Usage**:
    ```python
    download_dir = "C:/Users/YourUsername/Downloads"
    archive_dir = "C:/Users/YourUsername/Archives"
    cleanup_downloads(download_dir, archive_dir)
    ```
- **Example Output**: `Archived file.txt to C:/Users/YourUsername/Archives/Archive_2024-11-01`

---

### Duplicate File Finder Script

Finds and deletes duplicate files within a directory by comparing file hashes.

- **File**: `find_and_delete_duplicates.py`
- **Function**: Identifies duplicate files by computing SHA-256 hash values.
- **Usage**:
    ```python
    directory = "C:/path/to/your/directory"
    duplicates = find_duplicates(directory)
    delete_duplicates(duplicates)
    ```
- **Example Output**: `Deleted duplicate: C:/path/to/duplicate.txt (Original: C:/path/to/original.txt)`

---

### Organize Files Script

This script organizes files within a directory either by file type (extension) or by the last modification date.

- **File**: `organize_files.py`
- **Functions**:
  - `organize_files_by_type`: Organizes files by file extension.
  - `organize_files_by_date`: Organizes files by last modification date.
- **Usage**:
    ```python
    directory = "C:/path/to/your/directory"
    organize_files_by_type(directory)  # Organizes by type
    # organize_files_by_date(directory)  # Uncomment to organize by date
    ```
- **Example Output**: `Moved file.txt to C:/path/to/your/directory/TXT`

---

### Security Monitoring Script

Monitors the system for certain security indicators, such as startup programs, recently modified sensitive files, and unusual network connections.

- **File**: `security_monitor.py`
- **Function**: Checks for:
  - Startup programs not on a whitelist.
  - Recently modified files in sensitive directories.
  - Suspicious network connections.
- **Usage**:
    ```python
    # Ensure `config.json` is correctly set up
    run_security_check()
    ```
- **Configuration File**:
    - **config.json** should define `whitelist` for programs and connections, and `sensitive_dirs` for monitoring.
- **Example Output**: Logs findings to `security_log.json`.

---

### Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/yourrepo.git
    cd yourrepo
    ```

2. **Set Up Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Use `venv\Scripts\activate` on Windows
    ```

3. **Install Required Packages**:
    - Run `pip install -r requirements.txt` (if applicable) to install dependencies like `psutil`.

4. **Configuration**:
    - **config.json**: Modify this file to customize the whitelist for `security_monitor.py` and specify sensitive directories.

---

### Example `config.json`

```json
{
  "whitelist": {
    "startup_programs": ["Program1", "Program2"],
    "network_connections": [
      {"ip": "192.168.0.1", "port": 80},
      {"ip": "192.168.0.2", "port": 443}
    ]
  },
  "sensitive_dirs": [
    "C:/Users/YourUsername/Documents",
    "C:/Users/YourUsername/Desktop"
  ]
}
