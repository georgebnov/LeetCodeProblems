'''
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
"G": move one step. Position: (0, 1). Direction: South.
"G": move one step. Position: (0, 0). Direction: South.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
Based on that, we return true.
'''

'''
My thoughts on how to solve it:
there are only 4 cases:
1) if the robot is looking north after the first run, and is not on [0,0] then it will never come back, if it is it will always come back
2) if the robot is looking south after the first run, then no matter what it will do the opposite moves, and come back to zero on the second run
3) if its looking east or west after the first run, then it will always turn the same direction after every run, so in 3 moves it will go back to lookign north, WHICH is coming back to our first point.

now I need to build a way to track the direction and the coordinates. and then from there jsut amke the differnet cases.
'''

# this is a Medium!
instructions = "GGLLGG"
instructions1 = "GL"

def isRobotBounded(instructions): #My version (3ms | Beats 23.53%, 12.55MB | Beats 15.03%)
    coordinate = [0, 0]
    direction = 0 #0 = north, 1 = east, 2 = south, 3 = west

    firstMove = makeMove(coordinate, direction, instructions)
    coordinate = firstMove[0]
    direction = firstMove[1]
    print(coordinate)
    print(direction)

    if direction == 1 or direction == 3:
        epoch = 0
        while epoch < 3:
            steps = makeMove(coordinate, direction, instructions)
            coordinate = steps[0]
            direction = steps[1]
            print(coordinate)
            print(direction)
            epoch += 1
        if direction == 0 and coordinate == [0,0]:
            return True
        else:
            return False
    
    elif direction == 2:
        return True

    elif direction == 0 and coordinate == [0,0]:
        return True
    else:
        return False

def makeMove(coordinate, direction, instructions):
    for i in range(len(instructions)):
        if instructions[i] == "G":
            if direction == 0:
                coordinate[0] += 1
            elif direction == 1:
                coordinate[1] += 1
            elif direction == 2:
                coordinate[0] -= 1
            else:
                coordinate[1] -= 1

        elif instructions[i] == "L":
            direction -= 1
            if direction < 0:
                direction = 3
        else:
            direction += 1
            if direction > 3:
                direction = 0
    
    return coordinate, direction 

print(isRobotBounded(instructions))


#Someone elses solution which is MUCH simpler and should be much quicker. very good solution by this guy!
def isRobotBounded2(instructions):
    x, y, dx, dy = 0, 0, 0, 1
    for i in instructions:
        if i == 'R': dx, dy = dy, -dx
        if i == 'L': dx, dy = -dy, dx
        if i == 'G': x, y = x + dx, y + dy
    return (x, y) == (0, 0) or (dx, dy) != (0,1)

print(isRobotBounded2(instructions))