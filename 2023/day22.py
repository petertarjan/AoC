from heapq import heappush, heappop

f=open("day22.in","rt")
A=[]

for l in f:
    co1,co2=l.rstrip().split("~")
    x1,y1,z1=map(int,co1.split(","))
    x2,y2,z2=map(int,co2.split(","))
    A.append([[x1,y1,z1],[x2,y2,z2]])
    assert x1<=x2 and y1<=y2 and z1<=z2

n=len(A)
A.sort(key=lambda c: c[0][2])
supporters=[0]*n
supp=[[] for _ in range(n)]
for i in range(n):
    bz=0
    sp0=[]
    for j in range(i): # j<i
        x1=max(A[i][0][0],A[j][0][0])
        x2=min(A[i][1][0],A[j][1][0])
        y1=max(A[i][0][1],A[j][0][1])
        y2=min(A[i][1][1],A[j][1][1])
        if x1<=x2 and y1<=y2:
            bz=max(bz,A[j][1][2])
            sp0.append(j)
    zd=A[i][0][2]-bz-1
    assert zd>=0
    if zd>0:
        A[i][1][2]-=zd
        A[i][0][2]-=zd
    for s in sp0:
        if A[i][0][2]==A[s][1][2]+1:
            supporters[i]+=1
            supp[s].append(i)

# part1
print(sum(all(supporters[s]!=1 for s in supp[i]) for i in range(n)))

sol2=0
for i in range(n):
    di={}
    prc=[i]
    while len(prc)>0:
        p=heappop(prc)
        for j in supp[p]:
            di_n=di.get(j,supporters[j])-1
            di[j]=di_n
            if di_n==0:
                heappush(prc,j)
                sol2+=1
#part2
print(sol2)
