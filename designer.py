a=[1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7]
new=[]
s=zaba
al="abcdefghijklmnopqrstuvwxyz"
for i in s:
    if i in al:
        ind=al.index(i)
        q=a[ind]
        new.append(q)
l=len(new)
new.sort()
m=new[l-1]
print(m*l)
