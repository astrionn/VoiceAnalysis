from datetime import datetime
start=datetime.now()
print(start)

for i in range(100000000000):
	a = 1

stop=datetime.now()
print(stop)
print(stop-start)