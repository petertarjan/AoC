from sys import stdin

tick=0
val=1
sum=0
nextcheck=20
p2=""
for line in stdin:
    s=line.split()
    valnew=val
    p2+="#" if val-1<=tick%40<=val+1 else " "
    if len(s)==1 and s[0]=="noop":
#        print("NOOP")
        tick+=1
    elif len(s)==2 and s[0]=="addx":
#        print("ADDX")
        valnew=val+int(s[1])
        tick+=1
        p2+="#" if val-1<=tick%40<=val+1 else " "
        tick+=1
    if tick>=nextcheck:
#        print(nextcheck,val)
        sum+=nextcheck*val
        nextcheck+=40
    val=valnew

print("Part 1 :",sum)
print("Part 2 :")
for i in range(len(p2)):
    print(p2[i],end="\n" if i%40==39 else "")



