print("#pragma once\n#include <vector>\nusing namespace std;")
print("struct step_t {")
print("	 int from,to,dist;")
print("  vector<int> is;")
print("};\n")
print("step_t vs[]={")

pos_cost=[(0,0),(1,0),(3,0),(5,0),(7,0),(9,0),(10,0),(2,1),(4,1),(6,1),(8,1),(2,2),(4,2),(6,2),(8,2)]
first=True
for fr in range(15):
    for to in range(15):
        if fr==to: continue
        if fr>6 and to>6 and abs(fr-to)==4: continue
        if (fr,to) in [(0,1),(1,0),(5,6),(6,5)]: continue
        dist=pos_cost[fr][1]+pos_cost[to][1]+abs(pos_cost[fr][0]-pos_cost[to][0])
        obs=[]
        if fr>10:obs.append(fr-4)
        if to>10:obs.append(to-4)
        ofr=pos_cost[min(fr,to)][0]
        oto=pos_cost[max(fr,to)][0]
        for p in range(min(ofr,oto)+1,max(ofr,oto)):
            if p%2==0:continue
            for i in range(len(pos_cost)):
                if pos_cost[i][0]==p:
                    obs.append(i)
        if first: first=False
        else: print(",")
        print("{"+str(fr)+", "+str(to)+", "+str(dist)+", {"+", ".join(map(str,obs))+"} }",end="")
print("\n};")
print("const int vss=sizeof(vs)/sizeof(vs[0]);")
