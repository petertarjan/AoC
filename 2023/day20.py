from collections import deque
from math import gcd

f=open("day20.in","rt")
mods={}
ff={}
nand={}

st={}
for l in f:
    name,dst=l.rstrip().split(">")
    assert name[-2:]==" -"
    name=name[:-2].strip()
    if name=="broadcaster":
        bc=[d.strip() for d in dst.split(",")]
    elif name[0]=="%":
        ff[name[1:]]=[d.strip() for d in dst.split(",")]
    elif name[0]=="&":
        nand[name[1:]]=[d.strip() for d in dst.split(",")]
        st[name[1:]]={}
    else: assert False

for n in bc:
    if n in nand:
        st[nand]["broadcaster"]=False
for v in ff:
    for n in ff[v]:
        if n in nand:
            st[n][v]=False
for v in nand:        
    for n in nand[v]:
        if n in nand:
            st[n][v]=False

for k,v in ff.items():
    assert "rx" not in v
mustsendlow=[k for k,v in nand.items() if "rx" in v]
assert len(mustsendlow)==1
for k,v in ff.items():
    assert mustsendlow[0] not in v
mustsendhigh=[k for k,v in nand.items() if mustsendlow[0] in v]
sh=[[] for i in range(4)]

lows=highs=0
for steps in range(20000):
    prc=deque([])
    prc.append(("broadcaster",False,"button"))
    while len(prc)>0:
        p=prc.popleft()
        if p[1] and p[2] in mustsendhigh:
            sh[mustsendhigh.index(p[2])].append(steps+1)
        if p[1]: highs+=1
        else: lows+=1
        if p[0]=="broadcaster":
            for m in bc:
                prc.append((m,p[1],"broadcaster"))
        elif p[0] in ff:
            s=st.get(p[0],False)
            if not p[1]:
                s=not s
                for m in ff[p[0]]:
                    prc.append((m,s,p[0]))
                st[p[0]]=s
        elif p[0] in nand:
            st[p[0]][p[2]]=p[1]
            out=not all(v for v in st[p[0]].values())
            for m in nand[p[0]]:
                prc.append((m,out,p[0]))
    if steps==999:
        print(lows*highs)

sol=1
for s in sh:
    for i in range(1,len(s)):
        assert s[i]==s[0]*(i+1)
    g=gcd(sol,s[0])
    sol=(sol*s[0])//g
print(sol)

