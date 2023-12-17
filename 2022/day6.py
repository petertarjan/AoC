s=input()
part1runz=True
for i in range(len(s)-13):
    if part1runz:
        t=s[i:i+4]
        if len(set(t))==4:
            part1runz=False
            print("Part 1 :",i+4)
    t=s[i:i+14]
    if len(set(t))==14:
        print("Part 2 :",i+14)
        break

        
