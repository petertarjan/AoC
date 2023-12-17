import time
start_time = time.time()
f=open("day5.in","rt")

s=list(f.readline().rstrip().split(":"))
assert s[0]=="seeds"
s=list(map(int,s[1].split()))
f.readline()
assert len(s)%2==0
s2=[(s[i],s[i+1]) for i in range(0,len(s),2)]
print(s2)

for cnv in ["seed-to-soil map:","soil-to-fertilizer map:","fertilizer-to-water map:","water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:"]:
    assert f.readline().rstrip()==cnv
    t=list(map(int,f.readline().rstrip().split()))
    ns2=[]
    while len(t)==3:
        for i in range(len(s)):
            if isinstance(s[i],int) and t[1]<=s[i]<t[1]+t[2]:
                s[i]=(s[i]-t[1]+t[0],)
        for i in range(len(s2)):
            cleft=max(t[1],s2[i][0])
            cright=min(t[1]+t[2],s2[i][0]+s2[i][1])
            if cleft<cright:
                ns2.append((cleft-t[1]+t[0],cright-cleft))
                leftn=cleft-s2[i][0]
                rightn=s2[i][0]+s2[i][1]-cright
                s2[i]=(s2[i][0],leftn)
                if rightn>0:
                    s2.append((cright,rightn))
        t=list(map(int,f.readline().rstrip().split()))
    s2+=ns2
    ns2=[]
    for st,l in s2:
        if l>0:
            ns2.append((st,l))
    s2=ns2

    for i in range(len(s)):
        if not isinstance(s[i],int): s[i]=s[i][0]


print(min(s))
print(min(a for a,b in s2))
stop_time = time.time()
print(stop_time-start_time)
