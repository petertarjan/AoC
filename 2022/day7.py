from sys import stdin
d={}

for line in stdin:
    s=line.split()
    if s[0]=="$" and s[1]=="cd" and s[2]=="/":
        currdir=[]
    elif s[0]=="$" and s[1]=="ls":
        continue
    elif s[0]=="dir":
#        ldir=currdir[:]
#        ldir.append(s[1])
        continue
    elif s[0].isnumeric():
        for i in range(len(currdir)+1):
            d[tuple(currdir[:i])]=d.get(tuple(currdir[:i]),0)+int(s[0])
    elif s[0]=="$" and s[1]=="cd":
        if s[2]=="..":
            del currdir[-1]
        else:
            currdir.append(s[2])
    
sum=0
good=999999999999999999
spaceneeded=30000000-(70000000-d[tuple([])])
for k,v in d.items():
    if v<=100000:
        sum+=v
    if v>=spaceneeded and v<good:
        good=v
print("Part 1 :",sum)
print("Part 2 :",good)


