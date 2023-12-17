f=open("marci.in","rt")

def solve(A):
    r=0
    n=len(A[0])
    for i in range(1,n):
        ok=True
        for x in A:
            le=min(i,n-i)
            if x[i-le:i]!=x[i+le-1:i-1:-1]:
                ok=False
                break
        if ok:
            r+=i
    m=len(A)
    for i in range(1,m):
        le=min(i,m-i)
        if A[i-le:i]==A[i+le-1:i-1:-1]:
            r+=100*i
    return r

def diff(a,b):
    r=0
    for c,d in zip(a,b):
       if c!=d:
           r+=1
    return r

def diffr(a,b):
    return sum(diff(aa,bb) for aa,bb in zip(a,b))

def solve2(A):
    r=0
    n=len(A[0])
    for i in range(1,n):
        dif=0
        for x in A:
            le=min(i,n-i)
            dif+=diff(x[i-le:i],x[i+le-1:i-1:-1])
        if dif==1:
            r+=i
    m=len(A)
    for i in range(1,m):
        le=min(i,m-i)
        di=diffr(A[i-le:i],A[i+le-1:i-1:-1])
        if di==1:
            r+=100*i
    return r


sol2=sol=0
A=[]
for l in f:
    s=l.rstrip()
    if s=="":
        sol+=solve(A)
        sol2+=solve2(A)
        A=[]
    else:
        A.append(s)
if len(A)>0:
    sol+=solve(A)
    sol2+=solve2(A)
print(sol)
print(sol2)
