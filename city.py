n = 6
m = 6
l = [0,1,2,3,4,5]
d = []
dup = []
count = 0
mi = []
for i in range(n):
    if i in l:
        flag = 1
    else:
        dup.append(i)
for i in range(len(dup)):
    for j in range(len(l)):
        d.append(abs(l[j] - dup[i]))
    mi.append(min(d))
    del d[:]
if len(mi)==0:
    print(0)
else:
    print(max(mi))