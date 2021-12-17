octs = [
["x","x","x","x","x","x","x","x","x","x","x","x"],
[7,6,1,2,6,4,8,2,1,7],
[7,6,1,7,2,3,7,6,7,2],
[2,8,5,3,8,7,1,8,3,6],
[7,2,1,4,3,6,7,1,3,5],
[1,5,3,3,3,6,5,6,1,4],
[6,2,5,8,1,7,2,8,6,2],
[5,3,7,7,6,7,5,5,8,3],
[5,6,1,3,2,6,8,2,7,8],
[8,3,8,1,1,3,4,4,6,5],
[3,4,4,5,4,2,8,7,3,3],
["x","x","x","x","x","x","x","x","x","x","x","x"]
]
"""
octs = [
["x","x","x","x","x","x","x","x","x","x","x","x"],
[5,4,8,3,1,4,3,2,2,3],
[2,7,4,5,8,5,4,7,1,1],
[5,2,6,4,5,5,6,1,7,3],
[6,1,4,1,3,3,6,1,4,6],
[6,3,5,7,3,8,5,4,7,8],
[4,1,6,7,5,2,4,6,4,5],
[2,1,7,6,8,4,1,7,2,1],
[6,8,8,2,8,8,1,1,3,4],
[4,8,4,6,8,4,8,5,5,4],
[5,2,8,3,7,5,1,5,2,6],
["x","x","x","x","x","x","x","x","x","x","x","x"]
]
"""
ctr = 0
coordPairs = [(0,1), (1,0), (1,1), (0,-1), (-1,0), (-1,-1), (1,-1), (-1,1)]
yC = 0
xC = 0
checkOcts = []
newFlash = []
newFlashes = []
seen = []
zCtr = 0
def evaluate(flashOcts):
    flashCtr = 0
    #print(flashOcts)
    while(flashOcts):
        for coord in flashOcts:
            if octs[coord[0]][coord[1]] == 0:
                for z in range(len(coordPairs)):
                    #print("Did it")
                    if octs[coord[0] + coordPairs[z][0]][coord[1] + coordPairs[z][1]] != "x":
                        yC = coord[0] + coordPairs[z][0]
                        xC = coord[1] + coordPairs[z][1]
                        if octs[yC][xC] < 9 and (yC,xC) not in seen:
                            octs[yC][xC] += 1
                        elif octs[yC][xC] == 9 and (yC,xC) not in seen:
                            flashCtr += 1
                            newFlashes.append((yC, xC))
                            octs[yC][xC] = 0
                            seen.append((yC,xC))
            flashOcts.remove(coord)
        if newFlashes:
            flashCtr += evaluate(newFlashes) 
    return(flashCtr)

for y in range(len(octs)):
    octs[y].append("x")
    octs[y].insert(0,"x")
for l in range(1, len(octs)-1):
        print(octs[l])

for d in range(100):
    print("Day", d+1)
    newFlash = []
    newFlashes = []
    seen = []
    for y in range(1,len(octs)-1):
        for x in range(1,len(octs[y])-1):
            #print("Current Oct =", octs[y][x])
            if octs[y][x] < 9 and (y,x) not in seen:
                octs[y][x] += 1
            elif octs[y][x] == 9 and (y,x) not in seen:
                ctr += 1
                octs[y][x] = 0
                seen.append((y,x))
                newFlash.append((y,x))
    print(newFlash)
    ctr += evaluate(newFlash)
    for l in range(1, len(octs)-1):
        print(octs[l])
    
print(ctr)
