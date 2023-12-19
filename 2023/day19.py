from functools import reduce
from operator import mul as multiplication

def prod(g):
    return reduce(multiplication,g)

f=open("day19.in","rt")

def procrule(t):
    u=list(t.split(":"))
    if len(u)==1:
        return (u[0],)
    assert len(u)==2
    assert u[0][0] in "xmas"
    assert u[0][1] in "<>"
    return ("xmas".index(u[0][0]),u[0][1],int(u[0][2:]),u[1]) # var op num action

rules={}
for l in f:
    s=l.rstrip()
    if s=="": break
    t=s.split("{")
    assert t[1][-1]=="}"
    rules[t[0]]=list(map(procrule,t[1][:-1].split(",")))

def apply_rule(r,xmas):
    for q in r:
        if len(q)==1:
            return q[0]
        v=xmas[q[0]]
        if q[1]=="<":
            if v<q[2]: return q[3]
        elif q[1]==">":
            if v>q[2]: return q[3]
    assert False
sol=0
for l in f:
    s=l.rstrip()
    assert s[0]=="{"
    assert s[-1]=="}"

    assert "".join(t.split("=")[0] for t in s[1:-1].split(","))=="xmas"
    xmas=tuple(int(t.split("=")[1]) for t in s[1:-1].split(","))
    rul="in"
    while rul not in "AR":
        rul=apply_rule(rules[rul],xmas)
    if rul=="A":
        sol+=sum(xmas)
    else: assert rul=="R"
print(sol)

def count(ranges,r):
    global rules
    assert len(ranges)==8
    assert all(ranges[2*i]<=ranges[2*i+1] for i in range(4))
    if r=="A":
        return prod((ranges[2*i+1]-ranges[2*i]+1 for i in range(4)))
    elif r=="R":
        return 0
    ret=0
    for q in rules[r]:
        if len(q)==1:
            return ret+count(ranges,q[0])
        else:
            var_i=q[0]
            op=q[1]
            num=q[2]
            if op=="<":
                maxp=min(ranges[2*var_i+1],num-1)
                if ranges[2*var_i]<=maxp:
                    rl=ranges[:]
                    rl[2*var_i+1]=maxp
                    ret+=count(rl,q[3])
                ranges[2*var_i]=max(ranges[2*var_i],num)
                if ranges[2*var_i]>ranges[2*var_i+1]: return ret
            else:
                assert op==">"
                minp=max(ranges[2*var_i],num+1)
                if minp<=ranges[2*var_i+1]:
                    rl=ranges[:]
                    rl[2*var_i]=minp
                    ret+=count(rl,q[3])
                ranges[2*var_i+1]=min(ranges[2*var_i+1],num)
                if ranges[2*var_i+1]<ranges[2*var_i]: return ret
    assert False
print(count([1,4000,1,4000,1,4000,1,4000],"in"))   
