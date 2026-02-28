import datetime
# from datetime import datetime

mytime = datetime.time(2,20)
print(f'mytime: {mytime}')
print(f'mytime hour: {mytime.hour}')
print(f'mytime minutes: {mytime.minute}')
today = datetime.date.today()
print(f'today: {today}') # 2026-02-17
print(f'ctime of today', today.ctime()) # Tue Feb 17 00:00:00 2026
