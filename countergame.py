n = 753838
s = 0
c = 0
count = 0
dup=n
p=0


while dup>1:
  while n > 1 and c==0:
    s = n % 2
    if s != 0:
        c = 1
    n = n/2
  if c ==1:
    i=0
    while 2 ** i <= dup:
        p= pow(2, i)
        i = i + 1
    p = pow(2, i - 1)
    dup =dup - p
    count = count + 1
  else:
     dup=dup/2
     count=count+1
  n=dup
  c==0
if count%2==0:
    print("sddsd")
else:
    print("sdsds")