import re

def parse_logs(file_content):
    """
    Parse the content of a ROS log file.
    Args:
        file_content (str): The content of the log file as a string.
    Returns:
        list: A list of dictionaries, each containing the parsed log details.
    """
    # Define the regex pattern to match log entries
    log_pattern = r"\[(.+?)\] \[(.+?)\] \[(.+?)\] (.+)"
    
    # Parse each line in the file
    logs = []
    for line in file_content.splitlines():
        match = re.match(log_pattern, line)
        if match:
            logs.append({
                "timestamp": match.group(1),  # First capture group
                "severity": match.group(2),   # Second capture group
                "node": match.group(3),       # Third capture group
                "message": match.group(4),    # Fourth capture group
            })
    
    return logs

def filter_logs(logs, severity=None, keyword=None):
    """
    Filter logs based on severity level and keywords.
    """
    filtered = logs
    if severity:
        filtered = [log for log in filtered if log["severity"] == severity]
    if keyword:
        filtered = [log for log in filtered if keyword.lower() in log["message"].lower()]
    return filtered
