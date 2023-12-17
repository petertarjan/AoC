from sys import stdin

d={}
for line in stdin:
    s=line.split()
    sp=s[0][:-1]
    if len(s)==2:
        d[sp]=int(s[1])
    else:
        d[sp]=s[1:]

def calc(name):
    global d
    dd=d[name]
    if isinstance(dd,int): return dd
    if dd[1]=="+": return calc(dd[0])+calc(dd[2])
    elif dd[1]=="-": return calc(dd[0])-calc(dd[2])
    elif dd[1]=="*": return calc(dd[0])*calc(dd[2])
    elif dd[1]=="/": return calc(dd[0])//calc(dd[2])
    else:
        assert False


print("Part1:",calc("root"))
del d["humn"]

d["root"][1]="-"

def solve(name,val):
    global d
    if name=="humn": return val
    dd=d[name]
    try:
        dv0=calc(dd[0])
    except:
        dv0=""
    try:
        dv2=calc(dd[2])
    except:
        dv2=""
    if dd[1]=="+":
        if dv0!="":
            return solve(dd[2],val-dv0)
        else:
            return solve(dd[0],val-dv2)
    elif dd[1]=="-":
        if dv0!="":
            return solve(dd[2],dv0-val)
        else:
            return solve(dd[0],val+dv2)
    elif dd[1]=="*":
        if dv0!="":
            return solve(dd[2],val//dv0)
        else:
            return solve(dd[0],val//dv2)
    elif dd[1]=="/":
        if dv0!="":
            return solve(dd[2],dv0//val)
        else:
            return solve(dd[0],val*dv2)
    else:
        assert False

print("Part2:",solve("root",0))
