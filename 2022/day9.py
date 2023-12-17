from sys import stdin

dd={"R":(1,0),"L":(-1,0),"U":(0,-1),"D":(0,1)}

T=[(0,0)]*10
Ts1=set([T[1]])
Ts2=set([T[9]])

def c(x,y):
    return x+1 if x<y else x-1 if x>y else x

for line in stdin:
    s=line.split()
    dir=dd[s[0]]
    cnt=int(s[1])
    for _ in range(cnt):
        T[0]=(T[0][0]+dir[0],T[0][1]+dir[1])
        for i in range(1,10):
            if abs(T[i-1][0]-T[i][0])<=1 and abs(T[i-1][1]-T[i][1])<=1: continue
            T[i]=(c(T[i][0],T[i-1][0]),c(T[i][1],T[i-1][1]))
        Ts1.add(T[1])
        Ts2.add(T[9])

print("Part 1 :",len(Ts1))
print("Part 2 :",len(Ts2))


