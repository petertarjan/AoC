from sys import stdin
from copy import deepcopy

def g2s(i):
    return {0:".",1:"#",2:"o"}[i]

def dumpgrid(g):
    return "\n".join(["".join([g2s(i) for i in line]) for line in g])

rt=[]
for line in stdin:
    if line=="": break
    s=line.split()
    for i in range(1,len(s),2):
        assert s[i]=="->"
    nr=[]
    for i in range(0,len(s),2):
        c,r=map(int,s[i].split(","))
        nr.append((r,c))
    rt.append(nr)

min_r=min(min(r for r,c in nr) for nr in rt)
max_r=max(max(r for r,c in nr) for nr in rt)
min_c=min(min(c for r,c in nr) for nr in rt)
max_c=max(max(c for r,c in nr) for nr in rt)

g=[[0 for c in range(min_c,max_c+1)] for r in range(max_r+1)]

for ro in rt:
    r,c=ro[0]
    g[r][c-min_c]=1
    for i in range(1,len(ro)):
        gr,gc=ro[i]
        if gr==r:
            while c<gc:
                c+=1
                g[r][c-min_c]=1
            while c>gc:
                c-=1
                g[r][c-min_c]=1
        else:
            assert c==gc
            while r<gr:
                r+=1
                g[r][c-min_c]=1
            while r>gr:
                r-=1
                g[r][c-min_c]=1

g2=[]
new_max_c=502+max_r
new_min_c=498-max_r
for line in g:
    g2.append([0]*(min_c-new_min_c)+line+[0]*(new_max_c-max_c))

go=True
steps=-1
while go:
    steps+=1
    sr=0
    sc=500
    go=True
    while True:
        sr+=1
        if sr>max_r:
            go=False
            break
        if g[sr][sc-min_c]==0:
            pass
        elif sc-1<min_c:
            go=False
            break
        elif g[sr][sc-1-min_c]==0:
            sc-=1
        elif sc+1>max_c:
            go=False
            break
        elif g[sr][sc+1-min_c]==0:
            sc+=1
        else:
            g[sr-1][sc-min_c]=2
            break

#print(dumpgrid(g))
print("Part1 :",steps)

max_r+=2
max_c=new_max_c
min_c=new_min_c
g2.append([0 for c in range(min_c,max_c+1)])
g2.append([1 for c in range(min_c,max_c+1)])

go=True
steps=-1
while go:
    steps+=1
    sr=0
    sc=500
    go=True
    while True:
        if sr==max_r-1:
            g2[sr][sc-min_c]=2
            break            
        sr+=1
        if sr>max_r:
            go=False
            break
        if g2[sr][sc-min_c]==0:
            pass
        elif sc-1<min_c:
            go=False
            break
        elif g2[sr][sc-1-min_c]==0:
            sc-=1
        elif sc+1>max_c:
            go=False
            break
        elif g2[sr][sc+1-min_c]==0:
            sc+=1
        else:
            if g2[sr-1][sc-min_c]!=0:
                go=False
                break
            g2[sr-1][sc-min_c]=2
            break

#print(dumpgrid(g2))
print("Part 2 :",steps)
