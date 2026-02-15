# Problem: Analyze Server Log File

# Log format example:
# 2026-02-15 10:00:01 INFO User logged in
# 2026-02-15 10:01:12 ERROR Database connection failed
# 2026-02-15 10:02:45 WARNING Memory usage high
# 2026-02-15 10:03:22 ERROR Timeout occurred
# 2026-02-15 10:05:10 INFO File uploaded

# Requirements
# Count number of:
    # INFO logs
    # WARNING logs
    # ERROR logs
# Show total log count
# Show error messages separately

# Python Log Analysis Program
log_file = "programs/server.log"
info_count = 0
warning_count = 0
error_count = 0
error_messages = []

with open(log_file, "r") as file:       #with is called a context manager.
    for line in file:
        if "INFO" in line:
            info_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "ERROR" in line:
            error_count += 1
            error_messages.append(line.strip())

print("Total INFO logs:", info_count)
print("Total WARNING logs:", warning_count)
print("Total ERROR logs:", error_count)
print("\nError Details:")
for msg in error_messages:
    print(msg)

# Example Output
# Total INFO logs: 2
# Total WARNING logs: 1
# Total ERROR logs: 2

# Error Details:
# 2026-02-15 10:01:12 ERROR Database connection failed
# 2026-02-15 10:03:22 ERROR Timeout occurred

# Interview Explanation: I read the log file line by line to avoid loading the entire file into memory, classify logs based on severity, count occurrences, and extract error details for debugging.
