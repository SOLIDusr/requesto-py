import sys
import time

import src.requesto as rq


table = rq.DataBase.Table("userdata", db.cursor)
times = []
default = time.time_ns() // 1_000_000
for i in range(200):
    sys.stdout.write(str(i) + "\n")
    table.fetchAll()
    times.append(time.time_ns()//1_000_000 - default)
print(times)
