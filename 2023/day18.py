from bisect import bisect_left

f=open("day18.in","rt")

r=0
c=0

dirs=[(0,1),(1,0),(0,-1),(-1,0)]
dc="RDLU"

maxr=maxc=-9999999
minr=minc=9999999

in1=[]
in2=[]
r2=0
c2=0
r1l=set([0])
r2l=set([0])
c1l=set([0])
c2l=set([0])
for l in f:
    s=l.rstrip().split()
    d=dc.index(s[0])
    in1.append((d,int(s[1])))
    r+=dirs[d][0]*int(s[1])
    c+=dirs[d][1]*int(s[1])
    hd=int(s[2][2:-2],16)
    dir=int(s[2][-2])
    in2.append((dir,hd))
    r2+=dirs[dir][0]*hd
    c2+=dirs[dir][1]*hd
    r1l.add(r)
    c1l.add(c)
    r2l.add(r2)
    c2l.add(c2)

r1l=sorted(list(r1l))
c1l=sorted(list(c1l))
r2l=sorted(list(r2l))
c2l=sorted(list(c2l))

def fill(r,c,col,A):
    prc=[(r,c)]
    while len(prc)>0:
        r,c=prc[-1]
        del prc[-1]
        if 0<=r<len(A):
            if 0<=c<len(A[0]):
                if A[r][c]==".":
                    A[r][c]=col
                    prc.append((r-1,c))
                    prc.append((r+1,c))
                    prc.append((r,c-1))
                    prc.append((r,c+1))

def calc(rs,cs,inp):
    R=2*len(rs)
    C=2*len(cs)
    A=A=[["." for c in range(C)] for r in range(R)]
    r=c=0
    ri=bisect_left(rs,r)
    ci=bisect_left(cs,c)
    assert rs[ri]==r
    assert cs[ci]==c
    ri*=2
    ci*=2
    A[ri][ci]="#"
    left=[]
    right=[]
    for d,m in inp:
        if d==0:
            c+=m
            cin=bisect_left(cs,c)
            assert cs[cin]==c
            cin*=2
            assert cin>ci
            while cin>ci:
                ci+=1
                A[ri][ci]="#"
                left.append((ri-dirs[d][1],ci+dirs[d][0]))
                right.append((ri+dirs[d][1],ci-dirs[d][0]))
        elif d==1:
            r+=m
            rin=bisect_left(rs,r)
            assert rs[rin]==r
            rin*=2
            assert rin>ri
            while rin>ri:
                ri+=1
                A[ri][ci]="#"
                left.append((ri-dirs[d][1],ci+dirs[d][0]))
                right.append((ri+dirs[d][1],ci-dirs[d][0]))
        elif d==2:
            c-=m
            cin=bisect_left(cs,c)
            assert cs[cin]==c
            cin*=2
            assert cin<ci
            while cin<ci:
                ci-=1
                A[ri][ci]="#"
                left.append((ri-dirs[d][1],ci+dirs[d][0]))
                right.append((ri+dirs[d][1],ci-dirs[d][0]))
        elif d==3:
            r-=m
            rin=bisect_left(rs,r)
            assert rs[rin]==r
            rin*=2
            assert rin<ri
            while rin<ri:
                ri-=1
                A[ri][ci]="#"
                left.append((ri-dirs[d][1],ci+dirs[d][0]))
                right.append((ri+dirs[d][1],ci-dirs[d][0]))
        else:
            assert False
    for r,c in left:
        fill(r,c,"L",A)
    for r,c in right:
        fill(r,c,"R",A)
    sol=0
    if A[-1][-1]=="L":
        ptn="R#"
    elif A[-1][-1]=="R":
        ptn="L#"
    else: assert False
    for r in range(len(A)):
        for c in range(len(A[r])):
            if A[r][c] in ptn:
                rm=1
                if r%2==1:
                    rm=rs[r//2+1]-rs[r//2]-1
                cm=1
                if c%2==1:
                    cm=cs[c//2+1]-cs[c//2]-1
                sol+=rm*cm
                        
    return(sol)

print(calc(r1l,c1l,in1))
print(calc(r2l,c2l,in2))
