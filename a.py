N = int(input())

M = int(input())

T = int(input())

h = (T // 60 + N) % 24

m = T % 60 + M

if m >= 60:
    h += 1
    m -= 60

h = str(h).zfill(2)
m = str(m).zfill(2)
print(f"{h}:{m}")