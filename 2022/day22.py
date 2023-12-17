from sys import stdin

g=[]
for line in stdin:
    line=line.rstrip()
    if line=="": break
    g.append(line)

maxlen=max(len(s) for s in g)
for i in range(len(g)):
    if len(g[i])<maxlen:
        g[i]=g[i]+" "*(maxlen-len(g[i]))

t=input().strip()

r,c=0,0
while g[r][c]!=".": c+=1

def mysplit(s):
    ret=[]
    curr=[]
    for c in s:
        if c.isdigit():
            if isinstance(curr,int):
                curr=10*curr+int(c)
            else:
                if curr:
                    ret.append("".join(curr))
                curr=int(c)
        else:
            if isinstance(curr,int):
                ret.append(curr)
                curr=[]
            curr.append(c)
    if isinstance(curr,int):
        ret.append(curr)
    elif curr:
        ret.append("".join(curr))
    return ret

dirs=[(0,1),(1,0),(0,-1),(-1,0)]
d=0

for p in mysplit(t):
    if isinstance(p,int):
        dd=dirs[d]
        for _ in range(p):
            nr,nc=r,c
            while True:
                nr+=dd[0]
                nc+=dd[1]
                if nr>=len(g):
                    nr=0
                    while len(g[nr])<=nc or g[nr][nc] not in ".#": nr+=1
                    break
                elif nr<0:
                    nr=len(g)-1
                    while len(g[nr])<=nc or g[nr][nc] not in ".#": nr-=1
                    break
                elif nc>=len(g[nr]):
                    nc=0
                    while g[nr][nc] not in ".#": nc+=1
                    break
                elif nc<0:
                    nc=len(g[nr])-1
                    while g[nr][nc] not in ".#": nc-=1
                    break
                elif g[nr][nc] in ".#": break
                assert g[nr][nc]==" "

            if g[nr][nc]=="#":
                break
            r,c=nr,nc
    elif p=="R":
        d=(d+1)%4
    elif p=="L":
        d=(d+3)%4
    else:
        assert False
print("Part1:",1000*(r+1)+4*(c+1)+d)

a=50
if maxlen<50: a=4 # sample

#gdebug=[list(s) for s in g]
#ddebug=">v<^"

d=0
r,c=0,0
while g[r][c]!=".": c+=1

def calcdist(p,dir):
    global a
    if dir[0]==1:
        return a-p[0]%a
    if dir[0]==-1:
        return p[0]%a+1
    assert dir[0]==0
    if dir[1]==1:
        return a-p[1]%a
    if dir[1]==-1:
        return p[1]%a+1
    assert False


def mv(r,c,d,rot,d0,d1):
    global a,dirs
    nd=(d+rot)%4
    nr=r+(a*d0+1)*dirs[d][0]+a*d1*dirs[(d+1)%4][0]
    nc=c+(a*d0+1)*dirs[d][1]+a*d1*dirs[(d+1)%4][1]
    nr,nrm=nr//a,nr%a
    nc,ncm=nc//a,nc%a
    for i in range(rot):
        nrm,ncm=ncm,a-1-nrm
    return a*nr+nrm,a*nc+ncm,nd


pagetrans=( ( 1, 0, 1), ( 3, 0,-1),
            ( 2, 0, 2), ( 2, 0,-2),
            ( 1,-1, 2), ( 3,-1,-2),
            ( 3,-2, 3), ( 1,-2,-3),
            ( 2,-2, 2), ( 2,-2,-2),
            ( 0,-4, 2), ( 0,-4,-2),
            ( 3,-4, 1), ( 1,-4,-1))


for p in mysplit(t):
    if isinstance(p,int):
        for _ in range(p):
            nr=r+dirs[d][0]
            nc=c+dirs[d][1]
            nd=d
            if nc<0 or nr<0 or nr>=len(g) or nc>=len(g[nr]) or g[nr][nc]==" ":
                for rot,d0,d1 in pagetrans:

                    nr,nc,nd=mv(r,c,d,rot,d0,d1)
                    if nc>=0 and nr>=0 and nr<len(g) and nc<len(g[nr]) and g[nr][nc]!=" ":
#                        print(r,c,"->",nr,nc)

                        for _rot,_d0,_d1 in pagetrans:
                            nnr,nnc,nnd=mv(nr,nc,(nd+2)%4,_rot,_d0,_d1)
                            if nnc>=0 and nnr>=0 and nnr<len(g) and nnc<len(g[nr]) and g[nnr][nnc]!=" ":
                                break
                        else: assert False
#                        print((r,c,d),(nnr,nnc,nnd),(nr,nc,nd))
                        assert nnr==r and nnc==c and nnd==(d+2)%4

                        break
                else:
                    print(d,(r,c))
                    assert False

            if g[nr][nc]=="#": break
#            gdebug[r][c]=ddebug[d]
#            for gd in gdebug: print("".join(gd))
            r,c,d=nr,nc,nd
    elif p=="R":
        d=(d+1)%4
    elif p=="L":
        d=(d+3)%4
    else:
        assert False
print("Part2:",1000*(r+1)+4*(c+1)+d)
#gdebug[r][c]=ddebug[d]
#for gd in gdebug: print("".join(gd))
