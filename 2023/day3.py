def issymb(x):
    if x.isalnum() or x==".": return False
    return True

f=open("day3.in","rt")
m=[]
for line in f:
    m.append(line.rstrip())

sol1=0
stars={}
def add(r,c,n):
    global stars
    if (r,c) not in stars: stars[(r,c)]=[]
    stars[(r,c)].append(n)
for r in range(len(m)):
    c=0
    while c<len(m[r]):
        while c<len(m[r]) and not m[r][c].isdigit():
            c+=1
        cd=c+1
        if c==len(m[r]): break
        while cd<len(m[r]) and m[r][cd].isdigit():
            cd+=1
        ok=False
        num=int(m[r][c:cd])
        if r>0:
            for c0 in range(max(0,c-1),min(len(m[r-1]),cd+1)):
                if issymb(m[r-1][c0]): ok=True
                if m[r-1][c0]=='*': add(r-1,c0,num)
        if r<len(m)-1:
            for c0 in range(max(0,c-1),min(len(m[r+1]),cd+1)):
                if issymb(m[r+1][c0]): ok=True
                if m[r+1][c0]=='*': add(r+1,c0,num)
        if c>0:
            if issymb(m[r][c-1]): ok=True
            if m[r][c-1]=='*': add(r,c-1,num)
        if cd<len(m[r]):
            if issymb(m[r][cd]): ok=True
            if m[r][cd]=='*': add(r,cd,num)
        if ok:
            sol1+=num
        c=cd
print(sol1)
sol2=0
for k,v in stars.items():
    if len(v)==2:
        sol2+=v[0]*v[1]
print(sol2)
