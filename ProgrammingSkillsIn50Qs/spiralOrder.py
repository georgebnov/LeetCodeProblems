#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [1,2,3,6,9,8,7,4,5]

matrix = [[1,2,3],[4,5,6],[7,8,9]]

def spiralOrder(matrix):
    lenOfRows = len(matrix)
    lenOfCol = len(matrix[0])
    x, y, dx, dy = 0, 0, 1, 0
    order =[]

    for i in range(lenOfRows * lenOfCol):
        print(matrix[y][x])
        order.append(matrix[y][x])
        matrix[y][x] = "D"

        if not 0 <= x + dx < lenOfCol or not 0 <= y + dy < lenOfRows or matrix[y+dy][x+dx] == "D": #they stand in the bounds of 0 <= x + dx <lenOfRows and then they do the same for columns
            dx, dy = -dy, dx #changing direction clock-wise direciton.

        #Because the change will always be either 1 or -1, the change which way we are moving will be either adding or decreasing. thats why we add the change. 
        #And because only one will be moving the other is 0 it wont make changes of one which keeps it on track.
        x += dx
        y += dy
    
    return order

'''
What did I learn:
1) you can always control the movement by just keeping the direction of the movement. But always by keeping the direciton you can use it to als move up and down. the way you need it.
2) Stacking multiple ifs, into one, sometimes is simpler than trying to make it all run one after another.
3) keeping track of what you've already done is also something that is very important.
'''