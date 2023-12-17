import heapq

f=open("day17.in","rt")
A=[[int(c) for c in l.rstrip()] for l in f]

R=len(A)
C=len(A[0])

dirs=[(0,1),(0,-1),(1,0),(-1,0)]

def solve(mins,maxs):
    global A
    pq=[]
    for d in range(4):
        heapq.heappush(pq,(0,0,0,d,0))
    vis=[[[[False for c in range(maxs+1)] for r in range(4)] for c in range(C)] for r in range(R)]
    while True:
        dist,r,c,ad,an=heapq.heappop(pq)
        for d in range(4):
            if ad^d==1: continue
            if ad==d: an2=an+1
            else: an2=1
            if an2>maxs: continue
            if ad!=d and an<mins:
                continue
            r2=r+dirs[d][0]
            c2=c+dirs[d][1]
            if r2<0 or r2>=R: continue
            if c2<0 or c2>=C: continue
            dist2=dist+A[r2][c2]
            if r==R-1 and c==C-1:
                return dist
                go=False
                break
            else:
                ne=(dist2,r2,c2,d,an2)
                if not vis[r2][c2][d][an2]:
                    heapq.heappush(pq,ne)
                    vis[r2][c2][d][an2]=True

print(solve(1,3))
print(solve(4,10))
