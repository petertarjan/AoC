from sys import stdin
d={}

m=[]

cr=0
for line in stdin:
    m.append(line.strip())
    c=line.find('S')
    if c>=0:
        Cpos=(cr,c)
    c=line.find('E')
    cr+=1

#print(Cpos)

R=len(m)
C=len(m[0])
#print(R,C)

for part in [1,2]:
    vis=[[False for c in range(C)] for r in range(R)]
    if part==1:
        vis[Cpos[0]][Cpos[1]]=True
        level=[Cpos]
    else:
        assert part==2
        level=[]
        for r in range(R):
            for c in range(C):
                if m[r][c] in ['a','S']:
                    level.append((r,c))
                    vis[r][c]=True

    steps=0
    dirs=[[-1,0],[1,0],[0,1],[0,-1]]
    while True:
        steps+=1
        nlevel=[]
        for (r,c) in level:
            for d in dirs:
                r1=r+d[0]
                c1=c+d[1]
                if 0<=r1<R and 0<=c1<C and not vis[r1][c1]:
                    if m[r1][c1]=="E":
                        g=ord('z')
                    else:
                        g=ord(m[r1][c1])
                    if m[r][c]=="S":
                        st=ord('a')
                    else:
                        st=ord(m[r][c])
                    if g<=st+1:
                        if m[r1][c1]=="E":
                            print("Part"+str(part)+":",steps)
                            break
                            
                        nlevel.append((r1,c1))
                        vis[r1][c1]=True
            else: continue
            break
        else:
            level=nlevel
            continue
        break


