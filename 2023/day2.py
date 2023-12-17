fname="day2.in"
f=open(fname,"rt")
sol=0
s2=0
for l in f:
    g,b=l.split(":")
    g=int(g.split()[1])
    good=True
    minb=minr=ming=0
    for c in b.split(";"):
        for d in c.split(","):
            e=list(d.split())
            e0=int(e[0])
            if e[1]=="blue":
                if e0>14: good=False
                minb=max(minb,e0)
            if e[1]=="red":
                if e0>12: good=False
                minr=max(minr,e0)
            if e[1]=="green":
                if e0>13: good=False
                ming=max(ming,e0)
    if good: sol+=g
    #print(minr,ming,minb)
    s2+=minr*ming*minb
print(sol)
print(s2)

        
    
