from datetime import datetime, timedelta

now = datetime.now()
print(now.strftime("%Y-%m-%d"))

after_subtraction = now - timedelta(days=5)
print(after_subtraction.strftime("%Y-%m-%d"))