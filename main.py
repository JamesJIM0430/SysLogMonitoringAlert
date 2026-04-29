def detect_suspicious_activity(log_file):
    suspicious_keywords = [
        "Failed password",
        "invalid user",
        "authentication failure"
    ]

    with open(log_file, "r") as file:
        for line in file:
            for keyword in suspicious_keywords:
                if keyword in line:
                    print("[ALERT] Suspicious activity detected:")
                    print(line.strip())

                    with open("alerts.txt", "a") as alert_file:
                        alert_file.write(line)


if __name__ == "__main__":
    detect_suspicious_activity("sample_log.txt")