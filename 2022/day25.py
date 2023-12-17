from sys import stdin

def dec(s):
    r=0
    for c in s:
        if c=="2":
            r=5*r+2
        elif c=="1":
            r=5*r+1
        elif c=="0":
            r=5*r
        elif c=="-":
            r=5*r-1
        elif c=="=":
            r=5*r-2
        else:
            assert False
    return r

def enc(x):
    r=[]
    while x!=0:
        if x%5==2:
            r.append("2")
            x=(x-2)//5
        elif x%5==1:
            r.append("1")
            x=(x-1)//5
        elif x%5==0:
            r.append("0")
            x=x//5
        elif x%5==4:
            r.append("-")
            x=(x+1)//5
        elif x%5==3:
            r.append("=")
            x=(x+2)//5
        else:
            assert False
    r="".join(r[::-1])
    return r

g=[]
sm=0
for line in stdin:
    s=line.rstrip()
    sm+=dec(s)
print("Part1:",enc(sm))
