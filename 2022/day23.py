from sys import stdin

e={}
r=0
for line in stdin:
    line=line.rstrip()
    for c in range(len(line)):
        if line[c]=="#":
            e[(r,c)]=1
    r+=1

dirs=((-1,0),#N
      (1,0),#S
      (0,-1),#W
      (0,1))#E

def surr(el):
    global e
    if (el[0]-1,el[1]-1) in e: return True
    if (el[0]-1,el[1]) in e: return True
    if (el[0]-1,el[1]+1) in e: return True
    if (el[0],el[1]-1) in e: return True
    if (el[0],el[1]+1) in e: return True
    if (el[0]+1,el[1]-1) in e: return True
    if (el[0]+1,el[1]) in e: return True
    if (el[0]+1,el[1]+1) in e: return True
    return False

def dircheck(el,dir): # True if not empty
    global e
    if (el[0]+dir[0],el[1]+dir[1]) in e: return True
    if (el[0]+dir[0]+dir[1],el[1]+dir[1]-dir[0]) in e: return True
    if (el[0]+dir[0]-dir[1],el[1]+dir[1]+dir[0]) in e: return True
    return False

for step in range(10):
    # minr=999999999
    # maxr=-999999999
    # minc=999999999
    # maxc=-999999999
    # for p in e.keys():
    #     minr=min(minr,p[0])
    #     maxr=max(maxr,p[0])
    #     minc=min(minc,p[1])
    #     maxc=max(maxc,p[1])
    # for r in range(minr,maxr+1):
    #     for c in range(minc,maxc+1):
    #         if (r,c) in e:
    #             print("#",end="")
    #         else:
    #             print(".",end="")
    #     print()
    # print()


    ne={}
    fix=[]
    
    for el in e.keys():
        if surr(el):
            for i in range(4):
                if not dircheck(el,dirs[(step+i)%4]):
                    p=(el[0]+dirs[(step+i)%4][0],el[1]+dirs[(step+i)%4][1])
                    if p in ne:
                        if isinstance(ne[p],list): ne[p].append(el)
                        else:
                            ne[p]=[ne[p]]+[el]
                            fix.append(p)
                    else:
                        ne[p]=el
                    break
            else:
                ne[el]=1

        else:
            ne[el]=1
    for f in fix:
        for p in ne[f]:
            ne[p]=1
        del ne[f]
    e=ne

        
minr=999999999
maxr=-999999999
minc=999999999
maxc=-999999999
for p in e.keys():
    minr=min(minr,p[0])
    maxr=max(maxr,p[0])
    minc=min(minc,p[1])
    maxc=max(maxc,p[1])

print("Part1:",(maxr-minr+1)*(maxc-minc+1)-len(e))

step=10
while True:
    ne={}
    fix=[]

    emove=0
    for el in e.keys():
        if surr(el):
            for i in range(4):
                if not dircheck(el,dirs[(step+i)%4]):
                    emove+=1
                    p=(el[0]+dirs[(step+i)%4][0],el[1]+dirs[(step+i)%4][1])
                    if p in ne:
                        if isinstance(ne[p],list): ne[p].append(el)
                        else:
                            ne[p]=[ne[p]]+[el]
                            fix.append(p)
                    else:
                        ne[p]=el
                    break
            else:
                ne[el]=1

        else:
            ne[el]=1
    for f in fix:
        emove-=len(ne[f])
        for p in ne[f]:
            ne[p]=1
        del ne[f]
    e=ne

    step+=1
    if emove==0: break

print("Part2:",step)
