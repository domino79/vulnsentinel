import re

# Define regex patterns for common attacks
patterns = {
    "SQL Injection": re.compile(r"('|%27|--|\b(SELECT|UNION|INSERT|DROP|UPDATE|DELETE)\b)", re.IGNORECASE),
    "XSS": re.compile(r"(<script|%3Cscript)", re.IGNORECASE),
    "Brute Force": re.compile(r"(login|signin).*(fail|invalid|unauthorized)", re.IGNORECASE)
}

def scan_log(file_path):
    flagged_entries = []

    try:
        with open(file_path, 'r') as log_file:
            for line_num, line in enumerate(log_file, start=1):
                for threat, pattern in patterns.items():
                    if pattern.search(line):
                        flagged_entries.append({
                            "line_number": line_num,
                            "threat_type": threat,
                            "log_entry": line.strip()
                        })
    except FileNotFoundError:
        print(f"File not found: {file_path}")

    return flagged_entries
