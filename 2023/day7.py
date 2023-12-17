f=open("day7.in","rt")

def typ(s):
    l=[c for c in s]
    l.sort()
    if l[0]==l[1]==l[2]==l[3]==l[4]:
        return 10
    if l[0]==l[1]==l[2]==l[3] or l[1]==l[2]==l[3]==l[4]:
        return 9
    if l[0]==l[1]==l[2] and l[3]==l[4]:
        return 8
    if l[0]==l[1] and l[2]==l[3]==l[4]:
        return 8
    if l[0]==l[1]==l[2] or l[1]==l[2]==l[3] or l[2]==l[3]==l[4]:
        return 6
    if l[0]==l[1] and l[2]==l[3] or l[0]==l[1] and l[3]==l[4] or l[1]==l[2] and l[3]==l[4]:
        return 5
    if l[0]==l[1] or l[1]==l[2] or l[2]==l[3] or l[3]==l[4]:
        return 4
    return 1

def strongest(s):
    v=[]
    for x in ['2','3','4','5','6','7','8','9','T','Q','K','A']:
        f=s.replace('J',x)
        v.append((typ(f),f))
    v.sort()
    return v[-1][1]
        

def cnv(l):
    ret=[]
    for c in l:
        if c=="A":
            ret.append(14)
        elif c=="K":
            ret.append(13)
        elif c=="Q":
            ret.append(12)
        elif c=="J":
            ret.append(11)
        elif c=="T":
            ret.append(10)
        else:
            ret.append(int(c))
    return tuple(ret)
def cnv2(l):
    ret=[]
    for c in l:
        if c=="A":
            ret.append(14)
        elif c=="K":
            ret.append(13)
        elif c=="Q":
            ret.append(12)
        elif c=="J":
            ret.append(0)
        elif c=="T":
            ret.append(10)
        else:
            ret.append(int(c))
    return tuple(ret)

r=[]
r2=[]
for l in f:
    ss=l.rstrip().split()
    r.append((typ(ss[0]),cnv(ss[0]),int(ss[1])))
    st=strongest(ss[0])
    r2.append((typ(st),cnv2(ss[0]),int(ss[1])))
r.sort()
r2.sort()

s1=0
s2=0
for i in range(len(r)):
    s1+=(i+1)*r[i][2]
print(s1)

for i in range(len(r2)):
    s2+=(i+1)*r2[i][2]
print(s2)
