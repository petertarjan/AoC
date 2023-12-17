f=open("day16.in","rt")

A=[]
for l in f:
    A.append(l.rstrip())

#print(A)

rays=[]

R=len(A)
C=len(A[0])
#print(R,C)

def solve(r,c,d):
        global A,R,C
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        energized=[[[0,0,0,0] for cc in range(C)] for rr in range(R)]
        rays.append((d,r,c))

        while len(rays)>0:
                d,r,c=rays[-1]
                del rays[-1]
                r+=dirs[d][0]
                c+=dirs[d][1]              
                if r<0 or r>=R or c<0 or c>=C: continue
                if energized[r][c][d]>0: continue
                energized[r][c][d]=1
                x=A[r][c]
                if x==".":
                        rays.append((d,r,c))
                if d==0:
                        if x=="|":
                                rays.append((2,r,c))
                                rays.append((3,r,c))
                        if x=="-":
                                rays.append((0,r,c))
                        if x=="/":
                                rays.append((3,r,c))
                        if x=="\\":
                                rays.append((2,r,c))
                elif d==1:
                        if x=="|":
                                rays.append((2,r,c))
                                rays.append((3,r,c))
                        if x=="-":
                                rays.append((1,r,c))
                        if x=="/":
                                rays.append((2,r,c))
                        if x=="\\":
                                rays.append((3,r,c))
                elif d==2:
                        if x=="|":
                                rays.append((2,r,c))
                        if x=="-":
                                rays.append((0,r,c))
                                rays.append((1,r,c))
                        if x=="/":
                                rays.append((1,r,c))
                        if x=="\\":
                                rays.append((0,r,c))
                elif d==3:
                        if x=="|":
                                rays.append((3,r,c))
                        if x=="-":
                                rays.append((0,r,c))
                                rays.append((1,r,c))
                        if x=="/":
                                rays.append((0,r,c))
                        if x=="\\":
                                rays.append((1,r,c))

        #print(energized)
        sol=0
        for l in energized:
                for e in l:
                        if e[0]>0 or e[1]>0 or e[2]>0 or e[3]>0:
                             sol+=1
##                             print("#",end="")
##                        else:
##                             print(".",end="")
##                print()
                                
        return sol

print(solve(0,-1,0))

sol2=0
for r in range(R):
        s=solve(r,-1,0)
        sol2=max(s,sol2)
        s=solve(r,C,1)
        sol2=max(s,sol2)

for c in range(C):
        s=solve(-1,c,2)
        sol2=max(s,sol2)
        s=solve(R,c,3)
        sol2=max(s,sol2)
print(sol2)


