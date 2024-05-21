import time
start = time.time()
for i in range(9999999):
    s = "1" + "2"
    int(s)
print(time.time() - start)

start = time.time()
for i in range(9999999):
    s = ["1"]
    s.append("2")
    int("".join(s))
print(time.time() - start)
