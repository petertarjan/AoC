f=open("day9.in","rt")

def difs(a):
    return [a[i+1]-a[i] for i in range(len(a)-1)]

def all0(a):
    for x in a:
        if x!=0: return False
    return True

s=0
s2=0
for l in f:
    a=list(map(int,l.rstrip().split()))
    A=[a]
    while not all0(A[-1]):
        A.append(difs(A[-1]))
    d=0
    d2=0
    for b in A[::-1]:
       d=d+b[-1]
       d2=b[0]-d2
    s+=d
    s2+=d2
print(s)
print(s2)
