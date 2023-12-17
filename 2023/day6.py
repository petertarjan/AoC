from math import sqrt,ceil,floor
f=open("day6.in","rt")

s=list(f.readline().rstrip().split(":"))
assert s[0]=="Time"
t=list(map(int,s[1].split()))
t2=int("".join(s[1].split()))
s=list(f.readline().rstrip().split(":"))
assert s[0]=="Distance"
d=list(map(int,s[1].split()))
d2=int("".join(s[1].split()))

sol=1
assert len(t)==len(d)
for t0,d0 in zip(t,d):
    det=t0**2-4*d0
    assert det>=0
    minv=floor(0.5*(t0-sqrt(det)))+1
    maxv=ceil(0.5*(t0+sqrt(det)))-1
    sol*=maxv-minv+1
print(sol)
det=t2**2-4*d2
assert det>=0
minv=floor(0.5*(t0-sqrt(det)))+1
maxv=ceil(0.5*(t0+sqrt(det)))-1
sol=maxv-minv+1
print(sol)


    
