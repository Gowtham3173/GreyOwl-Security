import logging
from collections import Counter

def summarize_logs(log_file="logs/model_logs.log"):
    threat_counts = Counter()
    try:
        with open(log_file, 'r') as file:
            for line in file:
                if "Threat flagged" in line:
                    threat_counts['Threats'] += 1
                elif "below threshold" in line:
                    threat_counts['Non-threats'] += 1
    except FileNotFoundError:
        logging.error("Log file not found. Ensure logs are being generated.")
        return

    logging.info("Summary of Predictions:")
    for category, count in threat_counts.items():
        logging.info(f"{category}: {count}")

# Example usage
summarize_logs()
