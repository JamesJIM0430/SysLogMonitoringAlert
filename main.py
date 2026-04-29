def detect_suspicious_activity(log_file):
    suspicious_keywords = [
        "Failed password",
        "invalid user",
        "authentication failure"
    ]

    failed_count = 0
    threshold = 3  # alert if 3 or more attempts

    with open(log_file, "r") as file:
        for line in file:
            for keyword in suspicious_keywords:
                if keyword in line:
                    failed_count += 1

                    if failed_count >= threshold:
                        print("[ALERT] Multiple failed login attempts detected!")
                        print(line.strip())

                        with open("alerts.txt", "a") as alert_file:
                            alert_file.write(line)


if __name__ == "__main__":
    detect_suspicious_activity("sample_log.txt")
