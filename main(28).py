from datetime import datetime

for _ in range(int(input())):
    time1 = input()
    time2 = input()

    t1 = datetime.strptime(time1, "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.strptime(time2, "%a %d %b %Y %H:%M:%S %z")

    print(abs(int((t1 - t2).total_seconds())))