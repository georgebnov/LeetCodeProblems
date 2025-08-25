operations1 = ["5","2","C","D","+"]
operations3 = ["5","-2","4","C","D","9","+","+"]
operations2 = ["5","2","+"]
operations = ["1","C"]

'''
'+'. -> Record a new score that is the sum of the previous two scores.
'D'. -> Record a new score that is the double of the previous score.
'C'. -> Invalidate the previous score, removing it from the record.
'''

def calPoints(operations): #My version (0ms, 12.39MB)
    totalPoints = []
    summed = 0
    for i in range(len(operations)):
        if operations[i].lstrip("-").isdigit()== True:
            totalPoints.append(operations[i])
            print(totalPoints)
        else:
            if operations[i] == '+':
                last2digitsSum =  int(totalPoints[len(totalPoints)-2]) + int(totalPoints[len(totalPoints)-1])
                totalPoints.append(str(last2digitsSum))
                print(totalPoints)
            if operations[i] == "D":
                doubled = int(totalPoints[len(totalPoints)-1]) * 2
                totalPoints.append(str(doubled))
                print(totalPoints)
            if operations[i] == "C":
                del totalPoints[len(totalPoints) - 1]
                print(totalPoints)

    print(totalPoints)
    for k in range(len(totalPoints)):
        summed += int(totalPoints[k])
    
    return summed
    
print(calPoints(operations))

def calPoints2(operations): # I want to try to solve it without using the fiven functions like: .lstrip(), .isdigit()
    return False

'''
What did I learn:
1) When you want to add something to array, that has more than 1 cahracter or integer, and you use += operator it will actually split the letters into their own strings(it iterates through each one of them). Gotta use .append() to make it not do that.
2) int() = turns a string into and integer (well if it is an integer) and str() = turns anything into a string.
3) += can only use well with integers
4) sometimes thinking from the end helps more than thinking from the start (like i've used len(totalPoints)-1)
'''