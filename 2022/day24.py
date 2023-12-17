from sys import stdin

g=[]
for line in stdin:
    line=line.rstrip()
    g.append(line)


assert g[0][1]=='.'
assert g[-1][-2]=='.'
bl_down=[]
bl_up=[]
bl_left=[]
bl_right=[]

R=len(g)
C=len(g[0])
for r in range(1,R-1):
    bl_down.append([])
    bl_up.append([])
    bl_left.append([])
    bl_right.append([])
    for c in range(1,C-1):
        bl_down[-1].append(g[r][c]=="v")
        bl_up[-1].append(g[r][c]=="^")
        bl_left[-1].append(g[r][c]=="<")
        bl_right[-1].append(g[r][c]==">")

R-=2
C-=2
assert len(bl_down)==R
assert len(bl_down[0])==C
assert len(bl_up)==R
assert len(bl_up[0])==C
assert len(bl_left)==R
assert len(bl_left[0])==C
assert len(bl_right)==R
assert len(bl_right[0])==C


dirs=[(0,0),(-1,0),(0,-1),(1,0),(0,1)]
step=0

def dump(bl):
    for bb in bl:
        print("".join(" X"[int(x)] for x in bb))
    print("------------------------------------")

pos=[(-1,0)]
phase=0
while pos:
    bl_down=bl_down[-1:]+bl_down[:-1]
    bl_up=bl_up[1:]+bl_up[:1]
    for i in range(R):
        bl_left[i]=bl_left[i][1:]+bl_left[i][:1]
        bl_right[i]=bl_right[i][-1:]+bl_right[i][:-1]
    npos=set()
    for p in pos:
        for d in dirs:
            r=p[0]+d[0]
            c=p[1]+d[1]
            if 0<=r<R and 0<=c<C and not bl_down[r][c] and not bl_up[r][c] and not bl_left[r][c] and not bl_right[r][c]:
                npos.add((r,c))
            if r==-1 and c==0:
                npos.add((r,c))
            if r==R and c==C-1:
                npos.add((r,c))
    step+=1
    pos=list(npos)
    if phase==0 and (R,C-1) in pos:
        print("Part1:",step)
        phase=1
        pos=[(R,C-1)]
    elif phase==1 and ((-1,0)) in pos:
        phase=2
        pos=[(-1,0)]
    if phase==2 and (R,C-1) in pos:
        print("Part2:",step)
        phase=1
        break


    

        
    
                      
