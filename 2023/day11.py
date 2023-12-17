from bisect import bisect

f=open("day11.in","rt")
A=[]
rdup=[]
r=0
for l in f:
    A.append(l.rstrip())
    if all(c=="." for c in A[-1]):
        rdup.append(r)
    r+=1

cdup=[]
C=len(A[0])
R=len(A)
for c in range(C):
    if all(l[c]=="." for l in A):
        cdup.append(c)

p=[]
for r in range(R):
    for c in range(C):
        if A[r][c]=="#":
            p.append((r,c))
def cdiff(x,y,m):
    global cdup
    if x>y:
        x,y=y,x
    r=y-x
    return r+m*(bisect(cdup, y)-bisect(cdup, x))
def rdiff(x,y,m):
    global rdup
    if x>y:
        x,y=y,x
    r=y-x
    return r+m*(bisect(rdup, y)-bisect(rdup, x))

s=0
s2=0
for i in range(len(p)-1):
    for j in range(i+1,len(p)):
        s+=cdiff(p[i][1],p[j][1],1)
        s+=rdiff(p[i][0],p[j][0],1)
        s2+=cdiff(p[i][1],p[j][1],999999)
        s2+=rdiff(p[i][0],p[j][0],999999)


print(s)

print(s2)

