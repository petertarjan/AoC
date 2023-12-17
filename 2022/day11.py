from sys import stdin

def gcd(a,b):
    if a<0:
        a=-a
    if b<0:
        b=-b
    while a!=b and a>0 and b>0:
        if (a>b):
            a=a%b
        else:
            b=b%a
    if a==0:
        return b
    return a

i=-1
starting=[]
ops=[]
div=[]
ttrue=[]
tfalse=[]
for line in stdin:
    s=line.split()
    if len(s)==0: continue
    if s[0]=="Monkey":
        i+=1
        assert int(s[1][:-1])==i
        starting.append([])
        ops.append("")
        div.append(0)
        ttrue.append(-1)
        tfalse.append(-1)
    elif s[0]=="Starting":
        for j in range(2,len(s)):
            t=s[j]
            starting[i].append(int(t[:-1] if t[-1]=="," else t))
    elif s[0]=="Operation:":
        assert s[1]+s[2]+s[3]=="new=old"
        assert len(s)==6
        if s[4]=="+":
            ops[i]=(int(s[5]),1,0)
        else:
            assert s[4]=="*"
            if s[5]=="old":
                ops[i]=(0,0,1)
            else:
                ops[i]=(0,int(s[5]),0)
    elif s[0]=="Test:":
        assert s[1]+s[2]=="divisibleby"
        div[i]=int(s[3])
    elif s[0]=="If":
        if s[1]=="true:":
            assert s[2]+s[3]+s[4]=="throwtomonkey"
            ttrue[i]=int(s[5])
        elif s[1]=="false:":
            assert s[2]+s[3]+s[4]=="throwtomonkey"
            tfalse[i]=int(s[5])

g=1
for f in div:
    s=gcd(f,g)
    g=(g*f)//s

i+=1

def convert(old,op):
    return op[0]+old*(op[1]+old*op[2])

s1=[ss[:] for ss in starting]
i1=[0 for _ in range(i)]

for round in range(20):
    for a in range(i):
        for b in range(len(s1[a])):
            x=convert(s1[a][b],ops[a])
            x=x//3
            tto=ttrue[a] if x%div[a]==0 else tfalse[a]
            s1[tto].append(x)
            assert tto!=a
            i1[a]+=1
        s1[a]=[]


s2=[ss[:] for ss in starting]
i2=[0 for _ in range(i)]
for round in range(10000):
    for a in range(i):
        for b in range(len(s2[a])):
            x=convert(s2[a][b],ops[a])%g
            tto=ttrue[a] if x%div[a]==0 else tfalse[a]
            s2[tto].append(x)
            assert tto!=a
            i2[a]+=1
        s2[a]=[]

si1=sorted(i1)
si2=sorted(i2)

print("Part 1 :",si1[-1]*si1[-2])
print("Part 2 :",si2[-1]*si2[-2])


#Part 1 : 51075
#Part 2 : 11741456163
