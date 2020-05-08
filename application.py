que=[['add', 'hack'],['add', 'hackerrank'],['find', 'hac'],['find', 'hak']]
ins=[]
fi=[]
st=""
count=0
j=0
for i in range(len(que)):
    new=que[i][j]
    if new[0]=="a":
        ins.append(que[i][1])

    else:
        fi.append(que[i][1])
    new=""
print(ins)
print(fi)
for j in fi:
    print(j)
    st=""
    count=0
    for i in ins:
        if j in i:
            count=count+1
        else:
            count=count
    print(count)