import re


def generate_sample_log():
    log_data = """2024-01-15 10:23:45 ERROR 404 192.168.1.1 Page not found
2024-01-15 10:25:12 INFO 200 192.168.1.2 Request successful
2024-01-15 10:27:33 ERROR 500 192.168.1.3 Internal server error
2024-01-15 10:30:01 ERROR 403 192.168.1.1 Access forbidden
2024-01-15 10:35:22 INFO 200 192.168.1.4 Request successful
2024-01-15 10:40:10 ERROR 404 192.168.1.5 Page not found
2024-01-15 10:45:55 ERROR 500 192.168.1.2 Internal server error
2024-01-15 10:50:30 INFO 200 192.168.1.3 Request successful
2024-01-15 10:55:18 ERROR 403 192.168.1.6 Access forbidden
2024-01-15 11:00:45 ERROR 404 192.168.1.1 Page not found"""

    with open("server.log", "w") as file:
        file.write(log_data)
    print("Sample log file created.")


def read_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


def analyze_log(filename):
    error_counts = {}
    ip_counts = {}
    timestamps = []
    total_lines = 0
    error_lines = 0

    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\d{3}) (\d+\.\d+\.\d+\.\d+)'

    for line in read_lines(filename):
        total_lines += 1
        match = re.search(pattern, line)
        if match:
            timestamp = match.group(1)
            level = match.group(2)
            error_code = match.group(3)
            ip = match.group(4)

            timestamps.append(timestamp)

            if level == "ERROR":
                error_lines += 1
                if error_code in error_counts:
                    error_counts[error_code] += 1
                else:
                    error_counts[error_code] = 1

                if ip in ip_counts:
                    ip_counts[ip] += 1
                else:
                    ip_counts[ip] = 1

    return total_lines, error_lines, error_counts, ip_counts, timestamps


def save_report(total_lines, error_lines, error_counts, ip_counts):
    with open("log_report.txt", "w") as file:
        file.write("=" * 40 + "\n")
        file.write("         LOG ANALYSIS REPORT\n")
        file.write("=" * 40 + "\n")
        file.write(f"Total Lines Processed : {total_lines}\n")
        file.write(f"Total Errors Found    : {error_lines}\n")
        file.write("\nError Code Summary:\n")
        file.write("-" * 40 + "\n")
        for code, count in error_counts.items():
            file.write(f"  Error {code}  :  {count} times\n")
        file.write("\nTop IPs with Errors:\n")
        file.write("-" * 40 + "\n")
        for ip, count in ip_counts.items():
            file.write(f"  {ip}  :  {count} errors\n")
        file.write("=" * 40 + "\n")
    print("Report saved to log_report.txt")


def display_report(total_lines, error_lines, error_counts, ip_counts):
    print("\n" + "=" * 40)
    print("         LOG ANALYSIS REPORT")
    print("=" * 40)
    print(f"  Total Lines Processed : {total_lines}")
    print(f"  Total Errors Found    : {error_lines}")
    print("\n  Error Code Summary:")
    print("-" * 40)
    for code, count in error_counts.items():
        print(f"  Error {code}  :  {count} times")
    print("\n  Top IPs with Errors:")
    print("-" * 40)
    for ip, count in ip_counts.items():
        print(f"  {ip}  :  {count} errors")
    print("=" * 40)


def main():
    print("=" * 40)
    print("        Log File Analyzer")
    print("=" * 40)

    while True:
        print("\n1. Create sample log file")
        print("2. Analyze log file")
        print("3. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            generate_sample_log()

        elif choice == "2":
            filename = input("Enter log file name (press Enter for server.log): ").strip()
            if filename == "":
                filename = "server.log"
            try:
                total_lines, error_lines, error_counts, ip_counts, timestamps = analyze_log(filename)
                display_report(total_lines, error_lines, error_counts, ip_counts)
                save_report(total_lines, error_lines, error_counts, ip_counts)
            except FileNotFoundError:
                print(f"File '{filename}' not found. Please create a sample log first.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()