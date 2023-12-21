from collections import deque
f=open("day21_.in","rt")
A=[]
for l in f:
    A.append(l.rstrip())

R=len(A)
C=len(A[0])
assert R==C and R%2==1
for r in range(R):
    if "S" in A[r]:
        rs=r
        cs=A[r].index("S")
        A[r]=A[r][:cs]+"."+A[r][cs+1:]
        break

def avails(A,r,c):
    global R,C
    if r>0 and c>0:
        if A[r-1][c]=="." or A[r][c-1]==".":
            if A[r-1][c-1]==".":
                yield r-1,c-1
    if r>0 and c<C-1:
        if A[r-1][c]=="." or A[r][c+1]==".":
            if A[r-1][c+1]==".":
                yield r-1,c+1
    if r<R-1 and c>0:
        if A[r+1][c]=="." or A[r][c-1]==".":
            if A[r+1][c-1]==".":
                yield r+1,c-1
    if r<R-1 and c<C-1:
        if A[r+1][c]=="." or A[r][c+1]==".":
            if A[r+1][c+1]==".":
                yield r+1,c+1
    if r>1:
        if A[r-1][c]=="." and A[r-2][c]==".":
            yield r-2,c
    if r<R-2:
        if A[r+1][c]=="." and A[r+2][c]==".":
            yield r+2,c
    if c>1:
        if A[r][c-1]=="." and A[r][c-2]==".":
            yield r,c-2
    if c<C-2:
        if A[r][c+1]=="." and A[r][c+2]==".":
            yield r,c+2

def step(s):
    global A
    s2=set()
    for r,c in s:
        for rn,cn in avails(A,r,c):
            s2.add((rn,cn))
    return s2

s=set([(rs,cs)])
for _ in range(32):
    s=step(s)
print(len(s))

############################################################
REALDATA=all(A[r][cs]=="." for r in range(R)) and all(A[rs][c]=="." for c in range(C))

STEPS=26501365 if REALDATA else 5000
ODD=(STEPS%2==1)

def avail(A,r,c):
    global R,C
    for d in [(0,1),(0,-1),(1,0),(-1,0)]:
        rn=r+d[0]
        if 0<=rn<R:
            cn=c+d[1]
            if 0<=cn<C:
                if A[rn][cn]==".":
                    yield rn,cn

def fill(A,r,c):
    global R,C
    prc=deque([(r,c)])
    assert A[r][c]=="."
    A[r][c]=0
    odd=even=0
    while len(prc)>0:
        rr,cc=prc.popleft()
        n=A[rr][cc]+1
        if n%2==1: even+=1
        else: odd+=1
        for r2,c2 in avail(A,rr,cc):
            A[r2][c2]=n
            prc.append((r2,c2))
    return n,even,odd

def genB(r,c):
    B=[[c for c in l] for l in A]
    maxsteps,even,odd=fill(B,r,c)
    return B,maxsteps,even,odd

firstcell,firstmax,feven,fodd=genB(rs,cs)
tl,tlmax,tleven,tlodd=genB(0,0)
tr,trmax,treven,trodd=genB(0,C-1)
bl,blmax,bleven,blodd=genB(R-1,0)
br,brmax,breven,brodd=genB(R-1,C-1)

if REALDATA:
    t_,t_max,t_even,t_odd=genB(0,cs)
    b_,b_max,b_even,b_odd=genB(R-1,cs)
    l_,l_max,l_even,l_odd=genB(rs,0)
    r_,r_max,r_even,r_odd=genB(rs,C-1)

assert feven==tleven==treven==bleven==breven
assert fodd==tlodd==trodd==blodd==brodd

sol=fodd if ODD else feven

def calcdiag(ff,m,t):
    global STEPS,ODD,feven,fodd,R
    cnt=(STEPS-ff-m)//R+1
    cnt1=(cnt+1)//2
    cnt2=cnt//2
    assert cnt1+cnt2==cnt
    part1=cnt1**2
    part2=cnt2*(cnt2+1)
    assert part1+part2==(cnt*(cnt+1))//2
    so=0
    stepsleft=STEPS-ff-cnt*R
    odd=ODD if cnt%2==0 else not ODD
    mul=cnt+1
    while stepsleft>=0:
        for r in range(R):
            for c in range(C):
                if t[r][c] in ("#","."): continue
                if t[r][c]<=stepsleft:
                    if t[r][c]%2==1 and odd:
                        so+=mul
                    elif t[r][c]%2==0 and not odd:
                        so+=mul

        mul+=1
        stepsleft-=R
        odd=not odd

    ffull1=fodd if ODD else feven
    ffull2=feven if ODD else fodd
    return ffull1*part1+ffull2*part2+so

def calcstraight(ff1,m1,t1,ff2,m2,t2):
    global STEPS,ODD,feven,fodd,R
    ffm=min(ff1+m1,ff2+m2)
    cnt=(STEPS-ffm)//R+1
    cnt1=(cnt+1)//2
    cnt2=cnt//2
    assert cnt1+cnt2==cnt
    stepsleft1=STEPS-ff1-cnt*R
    stepsleft2=STEPS-ff2-cnt*R
    so=0
    odd=ODD if cnt%2==1 else not ODD
    while True:
        if stepsleft1<0 and stepsleft2<0:
            break
        for r in range(R):
            for c in range(C):
                if t1[r][c] in ("#","."): continue
                if t1[r][c]<=stepsleft1 or t2[r][c]<=stepsleft2:
                    assert t1[r][c]%2==t2[r][c]%2
                    if t1[r][c]%2==1 and odd: so+=1
                    elif t1[r][c]%2==0 and not odd: so+=1
        stepsleft1-=R
        stepsleft2-=R
        odd=not odd
    ffull1=feven if ODD else fodd
    ffull2=fodd if ODD else feven
    return ffull1*cnt1+ffull2*cnt2+so


def calcstraight3(ff1,m1,t1,ff2,m2,t2,ff3,m3,t3):
    global STEPS,ODD,feven,fodd,R
    ffm=min(ff1+m1,ff2+m2,ff3+m3)
    cnt=(STEPS-ffm)//R+1
    cnt1=(cnt+1)//2
    cnt2=cnt//2
    assert cnt1+cnt2==cnt
    stepsleft1=STEPS-ff1-cnt*R
    stepsleft2=STEPS-ff2-cnt*R
    stepsleft3=STEPS-ff3-cnt*R
    so=0
    odd=ODD if cnt%2==1 else not ODD
    while True:
        if stepsleft1<0 and stepsleft2<0 and stepsleft3<0:
            break
        for r in range(R):
            for c in range(C):
                if t1[r][c] in ("#","."): continue
                if t1[r][c]<=stepsleft1 or t2[r][c]<=stepsleft2 or t3[r][c]<=stepsleft3:
                    assert t1[r][c]%2==t2[r][c]%2==1-t3[r][c]%2
                    if t1[r][c]%2==1 and odd: so+=1
                    elif t1[r][c]%2==0 and not odd: so+=1
        stepsleft1-=R
        stepsleft2-=R
        stepsleft3-=R
        odd=not odd
    ffull1=feven if ODD else fodd
    ffull2=fodd if ODD else feven
    return ffull1*cnt1+ffull2*cnt2+so

sol+=calcdiag(firstcell[0][0]+2,brmax,br)
sol+=calcdiag(firstcell[R-1][C-1]+2,tlmax,tl)
sol+=calcdiag(firstcell[R-1][0]+2,trmax,tr)
sol+=calcdiag(firstcell[0][C-1]+2,blmax,bl)
if REALDATA:
    sol+=calcstraight3(firstcell[0][0]+1,blmax,bl,firstcell[0][C-1]+1,brmax,br,firstcell[0][cs]+1,b_max,b_)
    sol+=calcstraight3(firstcell[R-1][C-1]+1,trmax,tr,firstcell[R-1][0]+1,tlmax,tl,firstcell[R-1][cs]+1,t_max,t_)
    sol+=calcstraight3(firstcell[0][0]+1,trmax,tr,firstcell[R-1][0]+1,brmax,br,firstcell[rs][0]+1,r_max,r_)
    sol+=calcstraight3(firstcell[R-1][C-1]+1,blmax,bl,firstcell[0][C-1]+1,tlmax,tl,firstcell[rs][C-1]+1,l_max,l_)
else:
    sol+=calcstraight(firstcell[0][0]+1,blmax,bl,firstcell[0][C-1]+1,brmax,br)
    sol+=calcstraight(firstcell[R-1][C-1]+1,trmax,tr,firstcell[R-1][0]+1,tlmax,tl)
    sol+=calcstraight(firstcell[0][0]+1,trmax,tr,firstcell[R-1][0]+1,brmax,br)
    sol+=calcstraight(firstcell[R-1][C-1]+1,blmax,bl,firstcell[0][C-1]+1,tlmax,tl)
print(sol)

#625382480005896 az
