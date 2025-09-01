#Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
#Output: [[1,0,1],[0,0,0],[1,0,1]]

matrix = [[1,1,1],[1,0,1],[1,1,1]]

def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    locationZeros = []

    for p in range(rows): #My Solution (1ms | Beats = 86.17%, 13.28MB | Beats 13.23%)
        for o in range(cols):
            if matrix[p][o] == 0:
                locationZeros.append([p,o])
                
    for num in range(len(locationZeros)): #the item index
        #Change the full row to 0s (i), hold i loop over cols and change them to 0s
        for i in range(cols):
            matrix[locationZeros[num][0]][i] = 0
        #Change the full Col to 0s (k), hold k, loop over rows and change them to 0s
        for k in range(rows):
            matrix[k][locationZeros[num][1]] = 0
    return matrix
print(setZeroes(matrix))

'''
What did I learn:
1) It was just mind boggling. Needed to like get the logic down
'''