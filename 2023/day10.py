f=open("day10.in","rt")
A=[]
for l in f:
    A.append(l.rstrip())

for r in range(len(A)):
    for c in range(len(A[r])):
        if A[r][c]=="S":
            sr=r
            sc=c
ar=br=sr
ac=bc=sc
#dd=[[-1,0],[1,0],[0,-1],[0.1]]
def next(r,c,dd):
    global left, right
    r2,c2,dd2=next2(r,c,dd)
    if dd==0 or dd2==0:
        left.append((r,c-1))
        right.append((r,c+1))
    if dd==1 or dd2==1:
        left.append((r,c+1))
        right.append((r,c-1))
    if dd==2 or dd2==2:
        left.append((r+1,c))
        right.append((r-1,c))
    if dd==3 or dd2==3:
        left.append((r-1,c))
        right.append((r+1,c))
    return r2,c2,dd2
def next2(r,c,dd):
    global A,left,right
#    print(r,c,dd)
    if dd==0:
        if A[r][c] in ("|","S"):
            return r-1,c,0
        if A[r][c]=="7":
            return r,c-1,2
        if A[r][c]=="F":
            return r,c+1,3
        assert False
    if dd==1:
        if A[r][c] in ("|","S"): return r+1,c,1
        if A[r][c]=="L": return r,c+1,3
        if A[r][c]=="J": return r,c-1,2
        assert False
    if dd==2:
        if A[r][c] in ("-","S"): return r,c-1,2
        if A[r][c]=="L": return r-1,c,0
        if A[r][c]=="F": return r+1,c,1
        assert False
    if dd==3:
        if A[r][c] in ("-","S"): return r,c+1,3
        if A[r][c]=="J": return r-1,c,0
        if A[r][c]=="7": return r+1,c,1
        assert False
    assert False

s=0

def fill(r,c,col):
    global B
    prc=[(r,c)]
    while len(prc)>0:
        r,c=prc[-1]
        del prc[-1]
        if 0<=r<len(B):
            if 0<=c<len(B[0]):
                if B[r][c]==0:
                    B[r][c]=col
                    prc.append((r-1,c))
                    prc.append((r+1,c))
                    prc.append((r,c-1))
                    prc.append((r,c+1))

for d in range(4):
    if d==0 and A[ar-1][ac] not in ("|","7","F"): continue
    if d==1 and A[ar+1][ac] not in ("|","L","J"): continue
    if d==2 and A[ar][ac-1] not in ("-","L","F"): continue
    if d==3 and A[ar][ac+1] not in ("-","7","J"): continue
    left=[]
    right=[]
    st=1
    ad=bd=d
    B=[[0]*len(A[0]) for r in range(len(A)+1)]
    B[ar][ac]=1
    ar,ac,ad=next(ar,ac,ad)
#    br,bc,bd=next(br,bc,bd)
#    br,bc,bd=next(br,bc,bd)
#    while ar!=br or ac!=bc or ad!=bd:
    while ar!=sr or ac!=sc:
        B[ar][ac]=1
        st+=1
        ar,ac,ad=next(ar,ac,ad)
#        br,bc,bd=next(br,bc,bd)
#        br,bc,bd=next(br,bc,bd)
    s=max(s,(st+1)//2)
    s2=0
    for r,c in left: fill(r,c,2)
    for r,c in right: fill(r,c,3)
    print(B[len(A)])
    for l in B:
        for c in l:
            if c>1 and c!=B[len(A)][0]: s2+=1
    print(s2)
print(s)

