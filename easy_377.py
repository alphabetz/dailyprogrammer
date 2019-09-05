# Easy 377 Axis-aligned crate packing

def robot(cx, cy, bx, by): 
    # c = crate, b = box
    ax = 0
    ay = 0
    for i in range(bx, 0, -1):
        if bx == 1:
            ax = cx
            break
        if bx * i <= cx:
            #print(i)
            ax = i
            break
    for i in range(by, 0, -1):
        if by ==1 :
            ay = cy
            break
        if by * i <= cy:
            #print(i)
            ay = i
            break
    return ax * ay

robot(25, 18, 6, 5)
robot(10, 10, 1, 1)
robot(12, 34, 5, 6)
robot(12345, 678910, 1112, 1314)
robot(5, 100, 6, 1)
