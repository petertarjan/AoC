f=open("day12.in","rt")
sol=0

def get(l,i):
    if i>=len(l): return 0
    return l[i]

def add(l,i,x):
    if i>=len(l):
        l+=[0]*(i-len(l)+1)
    l[i]+=x

def dp():
    global s,g
    st=[[1]] # [gi][next possible index] - if next possible==len([gi]) -> ".?"
    for c in s:
        ns=[[] for i in range(len(g)+1)]
        if c in "?#":
            for gi in range(min(len(st),len(g))):
                for p in range(len(st[gi])):
                    if p>=g[gi]: break
                    add(ns[gi],p+1,st[gi][p])
        if c in "?.":
            for gi in range(len(st)):
                a=get(st[gi],0)
                if a>0: add(ns[gi],0,a)
                if gi<len(g):
                    a=get(st[gi],g[gi])
                    if a>0:
                        add(ns[gi+1],0,a)
        while len(ns[-1])==0: del ns[-1]
        st=ns
    r=0
    if len(st)>len(g):
        r+=get(st[len(g)],0)
    if len(st)>=len(g):
        r+=get(st[len(g)-1],g[-1])
    return r
               

sol2=0
for l in f:
    s,g=l.rstrip().split()
    g=list(map(int,g.split(',')))
    sol+=dp()
    s="?".join([s,s,s,s,s])
    g2=[]
    for i in range(5): g2+=g
    g=g2
    sol2+=dp()
print(sol)
print(sol2)
