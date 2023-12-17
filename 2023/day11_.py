
f=open("day11.in","rt")
A=[]
for l in f:
    A.append(l.rstrip())
    if all(c=="." for c in A[-1]):
        A.append(A[-1])


C=len(A[0])
B=[[] for _ in range(len(A))]
for c in range(C):
    for i in range(len(A)):
        B[i].append(A[i][c])
    if all(l[c]=="." for l in A):
        for i in range(len(A)):
            B[i].append(".")
C=len(B[0])
R=len(B)
p=[]
for r in range(R):
    for c in range(C):
        if B[r][c]=="#":
            p.append((r,c))
s=0
for i in range(len(p)-1):
    for j in range(i+1,len(p)):
        s+=abs(p[i][0]-p[j][0])+abs(p[i][1]-p[j][1])

print(s)

