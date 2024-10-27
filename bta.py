# Sample data: Replace this with actual dataset
data = [
    {'user_id': 101, 'login_time': '08:30', 'session_duration': 300, 'num_logins_per_day': 5},
    {'user_id': 102, 'login_time': '09:00', 'session_duration': 150, 'num_logins_per_day': 3},
    {'user_id': 101, 'login_time': '11:00', 'session_duration': 500, 'num_logins_per_day': 8},
    {'user_id': 103, 'login_time': '16:00', 'session_duration': 30, 'num_logins_per_day': 2},
    {'user_id': 104, 'login_time': '22:30', 'session_duration': 600, 'num_logins_per_day': 4},
]

# Set thresholds for anomaly detection
MAX_SESSION_DURATION = 450  # in seconds
MAX_LOGINS_PER_DAY = 7      # max number of logins considered normal

# Function to convert login_time to minutes since midnight
def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

# Detect anomalous behaviors
for record in data:
    login_minutes = time_to_minutes(record['login_time'])
    session_duration = record['session_duration']
    num_logins = record['num_logins_per_day']

    is_anomaly = False
    if session_duration > MAX_SESSION_DURATION:
        print(f"Anomaly Detected for User {record['user_id']}: Long session duration ({session_duration} seconds)")
        is_anomaly = True

    if num_logins > MAX_LOGINS_PER_DAY:
        print(f"Anomaly Detected for User {record['user_id']}: Too many logins ({num_logins})")
        is_anomaly = True

    if not is_anomaly:
        print(f"User {record['user_id']} has normal activity.")
