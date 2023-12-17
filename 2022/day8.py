from sys import stdin

g=[]
for line in stdin:
    s=map(int,line.strip())
    g.append(list(s))

R=len(g)
C=len(g[0])
vis=[[False]*C for _ in range(R)]

for r in range(R):
    mx=g[r][0]
    vis[r][0]=True
    for c in range(1,C):
        if g[r][c]>mx:
            mx=g[r][c]
            vis[r][c]=True
    mx=g[r][C-1]
    vis[r][C-1]=True
    for c in range(C-2,-1,-1):
        if g[r][c]>mx:
            mx=g[r][c]
            vis[r][c]=True

for c in range(C):
    mx=g[0][c]
    vis[0][c]=True
    for r in range(1,R):
        if g[r][c]>mx:
            mx=g[r][c]
            vis[r][c]=True
    mx=g[R-1][c]
    vis[R-1][c]=True
    for r in range(R-2,-1,-1):
        if g[r][c]>mx:
            mx=g[r][c]
            vis[r][c]=True


part1=sum(sum(map(int,v)) for v in vis)
print("Part 1 :",part1)

best=0
for r in range(1,R-1):
    for c in range(1,C-1):
        up=1
        while r-up>0 and g[r-up][c]<g[r][c]: up+=1
        down=1
        while r+down<R-1 and g[r+down][c]<g[r][c]: down+=1
        left=1
        while c-left>0 and g[r][c-left]<g[r][c]: left+=1
        right=1
        while c+right<C-1 and g[r][c+right]<g[r][c]: right+=1
        p=up*down*left*right
        best=max(best,p)

print("Part 2 :",best)


