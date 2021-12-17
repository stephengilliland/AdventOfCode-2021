
target = [56,76,-162,-134]
#target = [20, 30, -10, -5]
targetArea = []
for y in range(target[2], target[3]):
    for x in range(target[0],target[1]):
        targetArea.append([x,y])
print(targetArea)
width = target[1]-target[0]
height = abs(target[2]) - abs(target[1])

velocities = 0
xPos = 0
yPos = 0
notFound = True
vel = [0,0]
yPosition = 0
yPositionsTemp = []

for x in range(300):
    for y in range(300):
        vel = [x,y] #10,5
        xPos = 0
        yPos = 0
        notFound = True
        yPositionsTemp = []
        while xPos < target[1] and yPos > target[2]:
            yPositionsTemp.append(yPos)
            xPos += vel[0]
            yPos += vel[1]
            if vel[0] > 0:
                vel[0] -= 1
            if vel[0] < 0:
                vel[0] += 1
            vel[1] -= 1
            if [xPos,yPos] in targetArea:
                notFound = False
                break
        if notFound:
            #print(vel)
            pass
        else:
            if max(yPositionsTemp) > yPosition:
                yPosition = max(yPositionsTemp)
print("Position",yPosition)
        
                


