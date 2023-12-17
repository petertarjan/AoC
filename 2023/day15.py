f=open("day15.in","rt")

def h(o,c):
	o+=ord(c)
	o*=17
	o=o%256
	return o

A=[]
r=0
sol=0
boxes=[[] for _ in range(256)]

for l in f:
    for s in l.rstrip().split(","):
        o=0
        o2=-1
        for c in s:
            if c in "=-":
                o2=o
            o=h(o,c)
        sol+=o
        if s[-1]=="-":
            lbl=s[:-1]
            nb=[]
            for k,v in boxes[o2]:
                if k!=lbl:
                    nb.append((k,v))
            boxes[o2]=nb
        else:
            b=s.split("=")
            assert len(b)==2
            nb=[]
            fnd=False
            lbl=b[0]
            for k,v in boxes[o2]:
                if k!=lbl:
                    nb.append((k,v))
                else:
                    fnd=True
                    nb.append((k,int(b[1])))
            if not fnd:
                nb.append((lbl,int(b[1])))
            boxes[o2]=nb
#    for i in range(256):
#        if len(boxes[i])>0:
#            print(i,boxes[i])
#    break
            
print(sol)
sol2=0
for i in range(256):
    for j in range(len(boxes[i])):
        sol2+=(i+1)*(j+1)*boxes[i][j][1]
print(sol2)
