from math import gcd
from sympy import Symbol
from sympy import solve

def simplify(a,b):
    g=gcd(a,b)
    if abs(g)==1: return a,b
    return a//g,b//g

with open("day24.in", "rt") as f:
    A=[]
    for l in f:
        P,V=l.rstrip().split("@")
        px,py,pz=map(int,P.split(","))
        vx,vy,vz=map(int,V.split(","))
        A.append(((px,py,pz),(vx,vy,vz)))

if len(A)>=100:
    tmin=200000000000000
    tmax=400000000000000
else:
    tmin=7
    tmax=27


def crossprod(x1,y1,x2,y2):
    return x1*y2-x2*y1

sol=0
for i in range(len(A)-1):
    for j in range(i+1,len(A)):
        t1d=crossprod(A[i][1][0],A[i][1][1],A[j][1][0],A[j][1][1])
        t2d=crossprod(A[j][1][0],A[j][1][1],A[i][1][0],A[i][1][1])
        assert t1d+t2d==0
        dx=A[i][0][0]-A[j][0][0]
        dy=A[i][0][1]-A[j][0][1]
        if t1d==0:
            assert t2d==0
            assert crossprod(dx,dy,A[i][1][0],A[i][1][1])!=0
            continue
        t1n=crossprod(A[j][1][0],A[j][1][1],dx,dy)
        t2n=crossprod(dx,dy,A[i][1][0],A[i][1][1])
        if t1d<0: t1d,t1n=-t1d,-t1n
        if t2d<0: t2d,t2n=-t2d,-t2n
        if t1n<=0 or t2n<=0:
            continue
        t1n,t1d=simplify(t1n,t1d)
        t2n,t2d=simplify(t2n,t2d)

        x1n=A[i][0][0]*t1d+A[i][1][0]*t1n
        x1d=t1d
        x2n=A[j][0][0]*t2d+A[j][1][0]*t2n
        x2d=t2d
        x1n,x1d=simplify(x1n,x1d)
        x2n,x2d=simplify(x2n,x2d)
        assert x1n==x2n and x1d==x2d

        y1n=A[i][0][1]*t1d+A[i][1][1]*t1n
        y1d=t1d
        y2n=A[j][0][1]*t2d+A[j][1][1]*t2n
        y2d=t2d
        y1d=t1d
        y1n,y1d=simplify(y1n,y1d)
        y2n,y2d=simplify(y2n,y2d)
        assert y1n==y2n and y1d==y2d

        assert x1d>0 and y1d>0
        if tmin*x1d<=x1n<=tmax*x1d and tmin*y1d<=y1n<=tmax*y1d:
            sol+=1
print(sol)

x=Symbol('x')
y=Symbol('y')
z=Symbol('z')
vx=Symbol('vx')
vy=Symbol('vy')
vz=Symbol('vz')

eqs=[]
vars=[x,y,z,vx,vy,vz]
for i in range(3):
    p,v=A[i]
    x1,y1,z1=p
    vx1,vy1,vz1=v
    t=Symbol('t'+str(i))
    vars.append(t)
    eqs.append(x+t*vx-x1-t*vx1)
    eqs.append(y+t*vy-y1-t*vy1)
    eqs.append(z+t*vz-z1-t*vz1)
sol2=solve(eqs,vars,dict=True)[0]
print(sol2[x]+sol2[y]+sol2[z])

