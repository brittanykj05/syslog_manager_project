# syslog_manager.py

def parse_syslog(file_path):
    # Dictionary to store the count of each log severity level
    severity_count = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "CRITICAL": 0
    }

    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Check for severity levels in each line and update the count
            if "[INFO]" in line:
                severity_count["INFO"] += 1
            elif "[WARNING]" in line:
                severity_count["WARNING"] += 1
            elif "[ERROR]" in line:
                severity_count["ERROR"] += 1
            elif "[CRITICAL]" in line:
                severity_count["CRITICAL"] += 1

    return severity_count

# Main function to run the script
if __name__ == "__main__":
    log_file_path = "syslog_sample.txt"
    summary = parse_syslog(log_file_path)

    # Print the summary
    print("Syslog Summary:")
    for severity, count in summary.items():
        print(f"{severity} messages: {count}")

