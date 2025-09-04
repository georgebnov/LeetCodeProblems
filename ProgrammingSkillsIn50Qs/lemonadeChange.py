bills = [5,5,5,10,20]
bills1 = [5,5,10,10,20]

'''
My First Try Failed miserable with the time (36ms | Beats = 8.29%, 16.96MB | Beats 10.36%)
'''
def lemonadeChange(bills):
    change = {}
    exists = []
    for i in range(len(bills)):
        if bills[i] == 5:
            change[bills[i]] = change.get(bills[i], 0) + 1
            print(change)
        else:
            exists = findChange(change, bills[i])
            print(exists)
            print(exists == 0)
            if exists[0] != 0:
                for k in exists:
                    change[k] -= 1
                change[bills[i]] = change.get(bills[i], 0) + 1
                print(change)
            else:
                return False
    return True

def findChange(change, bill): #must return the change ex. if bills = 10, the return must be 5. or 0 (which signifies no change)
    giveBack =[]
    if (bill - 5) == 5:
        if 5 not in change or change[5] == 0:
            giveBack.append(0)
            return giveBack
        else:
            giveBack.append(5)
            return giveBack
    else:
        if 5 not in change or change[5] == 0:
            giveBack.append(0)
            return giveBack
        else:
            if change.get(10, 0) != 0:
                giveBack.extend([5, 10])
                return giveBack
            else:
                if change[5] >= 3:
                    giveBack.extend([5, 5, 5])
                    return giveBack
                else:
                    giveBack.append(0)
                    return giveBack


'''
Second Try: Still not satisfied (11ms | Beats = 20.24%, 17.89MB | Beats 10.36%)
but couldnt find a python solution that did faster than me. seems C would be the best way to solve this one!
'''

bills = [5,5,5,10,20]
bills1 = [5,5,10,10,20]

def lemonadeChange1(bills):
    change = {}
    for i in range(len(bills)):
        if bills[i] == 5:
            change[bills[i]] = change.get(bills[i], 0) + 1
        elif bills[i] == 10:
            if 5 not in change or change[5] == 0:
                return False
            else:
                change[5] -= 1
                change[bills[i]] = change.get(bills[i], 0) + 1
        elif bills[i] == 20:
            if 5 not in change or change[5] == 0:
                return False
            else:
                if change.get(10, 0) != 0:
                    change[5] -= 1
                    change[10] -= 1
                else:
                    if change[5] >= 3:
                        change[5] -= 3
                    else:
                        return False
    return True

print(lemonadeChange1(bills))