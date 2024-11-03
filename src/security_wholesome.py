import os
import json
from datetime import datetime, timedelta
import psutil
import winreg

def load_configuration():
    """Load configuration from a JSON file."""
    with open("config.json", "r") as file:
        return json.load(file)

# Load the configuration including the whitelist and sensitive directories
config = load_configuration()
whitelist = config["whitelist"]
sensitive_dirs = config["sensitive_dirs"]

def check_startup_programs():
    """Check for suspicious startup programs not in the whitelist."""
    suspicious_programs = []
    startup_keys = [
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        r"Software\Microsoft\Windows\CurrentVersion\RunOnce"
    ]

    for key in startup_keys:
        try:
            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key)
            for i in range(0, winreg.QueryInfoKey(reg_key)[1]):
                name, value, _ = winreg.EnumValue(reg_key, i)
                if name not in whitelist["startup_programs"]:
                    suspicious_programs.append({"name": name, "value": value})
            winreg.CloseKey(reg_key)
        except Exception as e:
            print(f"Error accessing registry: {e}")
    return suspicious_programs

def get_recently_modified_files(directory, days=1):
    """Get a list of recently modified files in a directory."""
    modified_files = []
    time_threshold = datetime.now() - timedelta(days=days)
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                if modified_time > time_threshold:
                    modified_files.append(file_path)
    except Exception as e:
        print(f"Error accessing directory {directory}: {e}")
    return modified_files

def check_network_connections():
    """Check for suspicious network connections not in the whitelist."""
    suspicious_connections = []
    for conn in psutil.net_connections():
        if conn.status == psutil.CONN_ESTABLISHED and conn.raddr:
            remote_ip = conn.raddr.ip
            remote_port = conn.raddr.port
            if not any(
                entry["ip"] == remote_ip and entry["port"] == remote_port
                for entry in whitelist["network_connections"]
            ):
                suspicious_connections.append({"ip": remote_ip, "port": remote_port})
    return suspicious_connections

def log_suspicious_activity(suspicious_programs, modified_files, network_connections):
    """Log suspicious activities to a JSON file."""
    log_entry = { 
        "timestamp": datetime.now().isoformat(), 
        "suspicious_startup_programs": suspicious_programs, 
        "recently_modified_files": modified_files,
        "suspicious_network_connections": network_connections 
    }
    
    # Append to the log file
    try:
        with open("security_log.json", "a") as log:
            log.write(json.dumps(log_entry) + "\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

def run_security_check():
    """Run the security check and log any findings."""
    suspicious_programs = check_startup_programs()
    modified_files = []
    for dir in sensitive_dirs:
        modified_files += get_recently_modified_files(dir)
    network_connections = check_network_connections()
    log_suspicious_activity(suspicious_programs, modified_files, network_connections)

if __name__ == "__main__":
    run_security_check()
    print("Security check completed. Check security_log.json for details.")
