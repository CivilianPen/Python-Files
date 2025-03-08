f = open('inf_26_04_21_24.txt').readlines()
max_delta = 0
for s in f[:-2]:
    delta = 0
    seted = []
    if s.count("G")<25:
        seted = set(s)
    for i in seted:
        delta = max(s.rfind(i) - s.find(i),delta)
    max_delta = max(delta, max_delta)

print(max_delta)
