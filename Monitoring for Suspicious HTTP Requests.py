import re
import os
import time

# Define the path to your web server logs
LOG_FILE_PATH = "/var/log/httpd/access_log"  # Adjust path based on your web server

# Regular expression pattern to detect potential command injection attempts
# Looking for suspicious characters like `;`, `&&`, `|`, or abnormal inputs
INJECTION_PATTERN = re.compile(r'(;|&&|\|\||\|)')

def monitor_logs():
    """Monitor web server logs for potential command injection attempts."""
    if not os.path.exists(LOG_FILE_PATH):
        print(f"Log file not found: {LOG_FILE_PATH}")
        return

    print(f"Monitoring log file: {LOG_FILE_PATH} for suspicious activity...")

    # Open the log file
    with open(LOG_FILE_PATH, 'r') as log_file:
        # Go to the end of the file
        log_file.seek(0, os.SEEK_END)

        while True:
            # Read new lines as they are written
            line = log_file.readline()

            # If no new line, wait a bit and continue
            if not line:
                time.sleep(1)
                continue

            # Check for suspicious patterns
            if INJECTION_PATTERN.search(line):
                print(f"Potential Command Injection detected: {line.strip()}")
                log_alert(line.strip())

def log_alert(alert_message):
    """Log the alert to a separate file for further analysis."""
    with open("suspicious_activity.log", "a") as alert_log:
        alert_log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - ALERT: {alert_message}\n")

if __name__ == "__main__":
    monitor_logs()
