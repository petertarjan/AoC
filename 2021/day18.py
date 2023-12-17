#!/usr/bin/python3
from sys import stdin

def explodepos(t):
    nest=0
    for i in range(len(t)):
        if t[i]=="[":
            nest+=1
            if nest==5:
                return i+1
        elif t[i]=="]":
            nest-=1
    return -1

def sum(a,b):
    r="["+a+","+b+"]"
#    print("sum:",r)
    while True:
        startp=explodepos(r)
        while startp>=0:
            stopp=r.find("]",startp)
            assert stopp>0
            v,w=map(int,r[startp:stopp].split(","))
            lstart=startp-2
            while lstart>=0 and not r[lstart].isdigit():
                lstart-=1
            if lstart>=0:
                lstop=lstart+1
                while lstart>0 and r[lstart-1].isdigit():
                    lstart-=1
                rbegin=r[:lstart]+str(int(r[lstart:lstop])+v)+r[lstop:startp-1]
            else:
                rbegin=r[:startp-1]
            rstart=stopp+1
            while rstart<len(r) and not r[rstart].isdigit():
                rstart+=1
            if rstart<len(r):
                rstop=rstart+1
                while rstop<len(r) and r[rstop].isdigit():
                    rstop+=1
                rend=r[stopp+1:rstart]+str(int(r[rstart:rstop])+w)+r[rstop:]
            else:
                rend=r[stopp+1:]
            r=rbegin+"0"+rend
#            print("exp:",r)
            startp=explodepos(r)

        n=0
        nstart=0
        while n<len(r):
            if not r[n].isdigit():
                if n-nstart>1:
                    v=int(r[nstart:n])
                    r=r[:nstart]+"["+str(v//2)+","+str((v+1)//2)+"]"+r[n:]
#                    print("spl:", r)
                    break
                nstart=n+1
            n+=1
        if nstart==len(r):
            break
            
    return r

def magn(s):
    m=1
    r=0
    for c in s:
       if c.isdigit(): r+=m*int(c)
       elif c=="[": m*=3
       elif c==",": m=(m//3)*2
       elif c=="]": m//=2
       else: assert false
    return r

s=[]
for line in stdin:
    s.append(line.strip())

sol=s[0]
for i in range(1,len(s)): sol=sum(sol,s[i])
print("part1:",magn(sol))
mm=0
for i in range(len(s)):
    for j in range(len(s)):
        if i==j: continue
        mm=max(mm,magn(sum(s[i],s[j])))
print("part2:",mm)
