from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(yesterday.strftime("%Y-%m-%d-%A"))

print(today.strftime("%Y-%m-%d-%A"))

print(tomorrow.strftime("%Y-%m-%d-%A"))