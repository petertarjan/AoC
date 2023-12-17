from sys import stdin

sensors=[]
for line in stdin:
    s=line.split()
    assert s[0]+s[1]=="Sensorat"
    x=int(s[2][:-1].split("=")[1])
    y=int(s[3][:-1].split("=")[1])
    bx=int(s[8][:-1].split("=")[1])
    by=int(s[9].split("=")[1])
    sensors.append((x,y,bx,by))

if len(sensors)>20: # real data
    r=2000000
    lim=4000000
else:
    lim=20
    r=10

bc=set()
intvs=[]

for x,y,bx,by in sensors:
    d=abs(x-bx)+abs(y-by)
    rem=d-abs(r-y)
    if rem>=0:
        intvs.append((x-rem,x+rem))
    if by==r:
        bc.add(bx)

intvs.sort()
sol=intvs[0][1]-intvs[0][0]+1
pr=intvs[0][1]
for i in range(1,len(intvs)):
    if intvs[i][0]>pr:
        sol+=intvs[i][1]-intvs[i][0]+1
        pr=intvs[i][1]
    else:
        if intvs[i][1]>pr:
            sol+=intvs[i][1]-pr
            pr=intvs[i][1]

print("Part 1:",sol-len(bc))

for rr in range(lim+1):
    intvs=[]
    for x,y,bx,by in sensors:
        d=abs(x-bx)+abs(y-by)
        rem=d-abs(rr-y)
        if rem>=0:
            frm=max(0,x-rem)
            to=min(x+rem,lim)
            if frm<=to: intvs.append((frm,to))
    intvs.sort()
    pos=0 # last not found
    for p in intvs:
        if p[0]>pos:
            print("Part 2:",4000000*pos+rr)
            break
        else:
            pos=max(pos,p[1]+1)
    else:
        continue
    break


