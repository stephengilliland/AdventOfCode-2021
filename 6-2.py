# Got multiplyers from running first 80 days
# Position in list represents day
mul = [15341, 60655, 24616, 55342, 47371, 40784, 81256, 16526, 49997]
newMuls =   [15341, 60655, 24616, 55342, 47371, 40784, 81256, 16526, 49997]
print(mul)
for x in range(176):
    
    for y in range(len(mul)):
        if y == 0:
            newMuls[8] = mul[0]
            newMuls[6] = mul[0] + mul[7]
        elif y != 7:
            newMuls[y-1] = mul[y]
            
    mul = list(newMuls)
print(sum(mul))