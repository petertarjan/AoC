from itertools import chain

def findnextnode(start, indir, B, vmap, fw, bw):
    global dirs
    le=1
    while True:
        if tuple(start) in vmap: break
        nds=[]
        for d in chain(range(1,indir),range(indir+1,5)):
            r=start[0]+dirs[d][0]
            c=start[1]+dirs[d][1]
            if B[r][c]>=0:
                nds.append((r,c,d))
        if len(nds)!=1:
            break
        le+=1
        indir=1+(2^(nds[0][2]-1))
        if B[start[0]][start[1]]>0:
            if B[start[0]][start[1]]!=nds[0][2]: fw=False
            if B[start[0]][start[1]]!=indir: bw=False
        B[start[0]][start[1]]=-1
        start=tuple(nds[0][:2])
    if B[start[0]][start[1]]>0:
        if B[start[0]][start[1]]==indir: fw=False
        if B[start[0]][start[1]]!=indir: bw=False
    return start, indir, le, fw, bw

dirs=(None,(-1,0),(0,-1),(1,0),(0,1))
ds=".^<v>"
with open("day23.in", "rt") as f:
    A=[l.rstrip() for l in f]
    assert all(all(c in "#."+ds for c in l) for l in A)
    R=len(A)
    C=len(A[0])   
    start=[0,1]
    assert all(A[start[0]][c]=="." if c==start[1] else "#" for c in range(C))
    stop=[R-1,C-2]
    assert all(A[stop[0]][c]=="." if c==stop[1] else "#" for c in range(C))
    B=[[-1 if c=="#" else ds.index(c) for c in l] for l in A]
    B[start[0]][start[1]]=-2
    B[stop[0]][stop[1]]=-3
    start[0]+=1
    stop[0]-=1
    assert B[start[0]][start[1]]==0 and B[stop[0]][stop[1]]==0
    sol2=0

    start, start_indir, le, fw, _=findnextnode(start, 1, B, {}, True, True)
    assert fw
    sol2+=le

    stop, stop_indir, le, _, bw=findnextnode(stop, 3, B, {}, True, True)
    assert bw
    sol2+=le

    vmap={start:0, stop:1}
    nextv=2
    edges=[[], []]

    prc=[start]
    sl2=0
    while len(prc)>0:
        p=prc[-1]
        pi=vmap[p]
        del prc[-1]
        for d in range(1,5):
            r=p[0]+dirs[d][0]
            c=p[1]+dirs[d][1]
            if B[r][c]>=0:
                fw=B[p[0]][p[1]]==0 or B[p[0]][p[1]]==d
                bw=B[p[0]][p[1]]==0 or B[p[0]][p[1]]!=d
                end, _, le, fw, bw=findnextnode((r,c),1+(2^(d-1)),B,vmap,fw,bw)
                v=vmap.get(end,-1)
                if v<0:
                    v=nextv
                    nextv+=1
                    vmap[end]=v
                    edges.append([])
                    prc.append(end)
                edges[pi].append((v,le,fw))
                edges[v].append((pi,le,bw))
    assert len(vmap)==len(edges)==nextv
    for loose in [False,True]:
        stack=[[0,0,sol2]] # vertex, edge index, acc. dist.
        free=[True]*nextv
        free[0]=free[1]=False
        while True:
            if len(edges[stack[-1][0]])>0:
                e=edges[stack[-1][0]][stack[-1][1]]
                if loose or e[2]:
                    if e[0]==1:
                        sl2=max(sl2,stack[-1][2]+e[1])
                    elif free[e[0]]:
                        free[e[0]]=False
                        stack.append([e[0],0,stack[-1][2]+e[1]])
                        continue
                stack[-1][1]+=1
            while stack[-1][1]==len(edges[stack[-1][0]]):
                free[stack[-1][0]]=True
                del stack[-1]
                if len(stack)==0: break
                stack[-1][1]+=1
            else: continue
            break
        print(sl2)
