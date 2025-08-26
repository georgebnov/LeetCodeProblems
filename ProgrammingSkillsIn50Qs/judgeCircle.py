moves = "LL"


def judgeCircle(moves): #My first solution; Got destroyed Top 95% (75ms, 13.34MB)
    coordinates = [0,0]
    for i in range(len(moves)):
        if moves[i] == "U" or moves[i] == "D":
            if moves[i] == "U":
                coordinates[0]+= 1
            else:
                coordinates[0]-= 1
        if moves[i] == "L" or moves[i] == "R":
            if moves[i] == "R":
                coordinates[1] += 1
            else:
                coordinates[1] -= 1

    if coordinates == [0,0]:
        return True
    else:
        return False

def judgeCircle2(moves): #My second solution; Got destroyed Top 95% (66ms, 13.37MB)
    coordinates = [0,0]
    for i in range(len(moves)):
        if moves[i] == "U":
            coordinates[0]+= 1
        elif moves[i] == "D":
            coordinates[0]-= 1
        if moves[i] == "R":
            coordinates[1] += 1
        if moves[i] == "L":
            coordinates[1] -= 1

    if coordinates == [0,0]:
        return True
    else:
        return False

print(judgeCircle2(moves))

'''
What did I learn:
1) if you don't have a call after the the function to close it off, nothign will show in the terminal even if you ask it to print something
2) Actually don't really understand whats the issue with the system, giving me such a high number for ms. (to this day I do not knwo how to make this code faster)
'''