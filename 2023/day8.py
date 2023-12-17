from math import gcd
f=open("day8.in","rt")

dir=f.readline().rstrip()
f.readline()
left={}
right={}

p2=[]
for l in f:
    src,dst=l.rstrip().split("=")
    src=src.replace(" ","")
    left[src],right[src]=dst.replace(" ","").replace("(","").replace(")","").split(",")
    if src[2]=="A":
        p2.append(src)

st=0
p="AAA"
while p!="ZZZ":
    if dir[st%len(dir)]=="L":
        p=left[p]
    else:
        p=right[p]
    st+=1
    
print(st)

s2=1
for p in p2:
    st=0
    while p[2]!="Z":
        if dir[st%len(dir)]=="L":
            p=left[p]
        else:
            p=right[p]
        st+=1
    g=gcd(s2,st)
    s2=s2*st//g
print(s2)
