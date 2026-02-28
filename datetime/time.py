from datetime import datetime, date

now = datetime.now()
print(f'now', now) # 2026-02-17 16:07:07.690940

mydatetime = datetime(2021, 10, 3, 14, 20, 1)
print(f'mydatetime {mydatetime}')
mydatetime = mydatetime.replace(year=2020)
print(f'mydatetime {mydatetime}')

# DATE
date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)
diff = date1 - date2
print(f'diff: {diff}')

# DATETIME
datetime1 = datetime(2021, 11, 3, 14, 20, 1)
datetime2 = datetime(2020, 11, 3, 14, 10, 1)
diff = datetime1 - datetime2
print(f'diff: {diff}')
print(f'diff seconds: {diff.seconds}')
