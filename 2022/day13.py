import functools
def cmp(l1,l2):
    if isinstance(l1,int) and isinstance(l2,int):
        return l1-l2
    if isinstance(l1,list) and isinstance(l2,list):
        i=0
        while i<len(l1) and i<len(l2):
            c=cmp(l1[i],l2[i])
            if c!=0: return c
            i+=1
        if i==len(l1) and i==len(l2): return 0
        if i==len(l1): return -1
        return 1
    if isinstance(l1,list): return cmp(l1,[l2])
    return cmp([l1],l2)
i=0
p1=0

l=[]
l.append([[2]])
l.append([[6]])
while True:
    i+=1
    try:
        while True:
            s1=input().strip()
            if s1!="": break
        s2=input().strip()
        e1=eval(s1)
        e2=eval(s2)
        c=cmp(e1,e2)
        if c<=0: p1+=i
        l.append(e1)
        l.append(e2)

    except:
        break

print("Part1 :",p1)
a=-1
b=-1
i=0

for x in sorted(l,key=functools.cmp_to_key(cmp)):
    i+=1
    if x==[[2]]: a=i
    if x==[[6]]: b=i
#    print(x)

print("Part2 :",a*b)

