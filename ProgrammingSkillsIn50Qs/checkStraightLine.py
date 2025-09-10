coordinate1s = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
coordinates1 = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
coordinates2 = [[0,0],[0,1],[0,-1]]
coordinates = [[2,1],[4,2],[6,3]]

def checkStraightLine(coordinates): #very slow solution, but I like the line method. The fastest way would be the second method I found
    differenceX = 0
    differenceY = 0

    if coordinates[1][0] - coordinates[0][0] == 0:
        for i in range(len(coordinates)):
            if coordinates[i][0] != 0:
                return False
        return True
    else:
        differenceX = coordinates[1][0] - coordinates[0][0]
        differenceY = coordinates[1][1] - coordinates[0][1]
        m = differenceY/differenceX

    print("difference X = ", differenceX)
    print("difference Y = ", differenceY)
    print("slope = ", m)
    b = coordinates[0][1] - (coordinates[0][0] * m)
    print(b)

    for i in range(len(coordinates)):
        print((coordinates[i][0] * m) + b)
        print(coordinates[i][1])
               
        if ((coordinates[i][0] * m) + b) != coordinates[i][1]:
            return False
    return True

print(checkStraightLine(coordinates))


def checkStraightLine(coordinates): #this is a very smart explanation, more explanation on how here under.
        (x0, y0), (x1, y1) = coordinates[: 2]
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False
        return True

''' find slope from point 1 and point 2
    compare the slopes of all other points wrt to the original slope

    Slope of points (x1, y1) and (x2, y2) is:
    (y2 - y1) / (x2 - x1)

    Slope of points (x1, y1) and (x3, y3) is:
    (y3 - y1) / (x3 - x1)
    
    for all three points to be on the same line, the slopes should be equal, in other words:
    (x3 - x1)*(y2 - y1) = (y3 - y1)*(x2 - x1)
    
    to avoid running into divide by zero error, use multiplication to find slope
'''