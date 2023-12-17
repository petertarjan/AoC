f=open("day14.in","rt")

A=[]
for l in f:
    A.append(l.rstrip())

n=len(A)
m=len(A[0])

s=0
load=[n]*m
for i in range(n):
    for j in range(len(A[i])):
        if A[i][j]=="O":
            s+=load[j]
            load[j]-=1
        elif A[i][j]=="#":
            load[j]=n-i-1

def north(A):
    R=len(A)
    C=len(A[0])
    B=[["."]*C for _ in range(R)]
    nextO=[0]*C
    for r in range(R):
        for c in range(C):
            if A[r][c]=="O":
                B[nextO[c]][c]="O"
                nextO[c]+=1
            elif A[r][c]=="#":
                nextO[c]=r+1
                B[r][c]="#"
    return B

def rotate(A):
    R=len(A)
    C=len(A[0])
    B=[["."]*R for _ in range(C)]
    for r in range(R):
        for c in range(C):
            B[c][R-1-r]=A[r][c]
    return B

def dump(B):
    for l in B:
        print("".join(l))

def calc(A):
    ret=0
    for r in range(len(A)):
        for c in range(len(A[0])):
            if A[r][c]=="O":
                ret+=len(A)-r
    return ret

print(s)

B=A[:]
steps=0
while True:
    steps+=1
    for _ in range(4):
        A=rotate(north(A))
        B=rotate(north(rotate(north(B))))
    if A==B:
        skip=1000000000-steps
        skip-=skip%steps
        steps+=skip
        break
while True:
    steps+=1
    for _ in range(4):
        A=rotate(north(A))
        B=rotate(north(rotate(north(B))))
    if steps==1000000000: break

print(calc(A))
