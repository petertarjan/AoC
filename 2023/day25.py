from scipy.optimize import linprog
from time import time

vmap={}
vmapi=[]
edges=[]
def getvid(s):
    global vmap,vmapi,edges
    i=vmap.get(s,-1)
    if i<0:
        i=len(vmapi)
        vmapi.append(s)
        vmap[s]=i
        edges.append([])
    return i

def filt(A,src,dst):
    return [A[i] for i in range(len(A)) if i!=src and i!=dst]
    
with open("day25.in","rt") as f:
    for l in f:
        src,dstz=l.rstrip().split(":")
        for dst in dstz.split():
            srci=getvid(src)
            dsti=getvid(dst)
            edges[srci].append(dsti)
            edges[dsti].append(srci)

    N=len(vmapi)
    E=sum(len(e) for e in edges)
    assert E%2==0
    E//=2
    assert N==len(vmap)==len(edges)

    eid=0
    A_eq=[[0]*E for _ in range(N)]
    c=[0]*E
    for src in range(N):
        for dst in edges[src]:
            if src>dst: continue
            assert A_eq[dst][eid]==A_eq[src][eid]==0
            if src==0: c[eid]=-1
            A_eq[dst][eid]=1
            A_eq[src][eid]=-1
            eid+=1
    assert E==eid
    group0=1
    method='highs-ds'
    t0=time()
    for DST in range(1,N):
        sl=linprog(c, A_eq=filt(A_eq,0,DST), b_eq=[0]*(N-2), bounds=[(-1,1)]*E, method=method)
        r=round(-sl.fun,2)
        assert r==round(r)
        if r>3: group0+=1
    print(method,time()-t0)
    print(group0*(N-group0))
