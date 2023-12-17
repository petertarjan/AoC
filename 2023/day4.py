fname="day4.in"
f=open(fname,"rt")
sol=0
s2=0
w=[0]*1000
i=1
for l in f:
    i+=1
    w[i]+=1
    s2+=w[i]
    n=s=0
    a=list(l.split(":"))
    b=list(a[1].split("|"))
    c=set(map(int,b[0].split()))
    for x in map(int,b[1].split()):
        if x in c:
            n+=1
            if s==0: s=1
            else: s*=2
    sol+=s
    for a in range(1,n+1):
        w[i+a]+=w[i]
print(sol)
print(s2)


    

        
