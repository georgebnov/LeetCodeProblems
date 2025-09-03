low = 800445804
high= 979430543

low1 = 8
high1 = 10

low2 = 3
high2 = 7

def countOdds(low, high): #first try (takes too long for high number)
    count = 0
    for i in range((high+1)-low):
        if (i + low) % 2 != 0:
            count += 1
    
    return count


def countOdds2(low, high): #Second Try (too slow, very innefficient code)
    count = 0
    if low % 2 != 0:
        count += 1
    if high % 2 != 0:
        count += 1
    
    if low % 2 != 0 or high % 2 != 0:
        newLow = low + 1
    else:
        newLow = low

    number = high - newLow

    count += (number // 2)
    
    return count

def countOdds3(low, high): #Third Try (20 ms, still kinda slow)
    count = 0
    number = high - low
    count += (number // 2)
    
    if low % 2 != 0 or high % 2 != 0:
        return count + 1
    else:
        return count

print(countOdds3(low, high))

def countOdds3(low, high): #Fourth Try (19 ms, Still not satisfied)
    count = ((high - low) // 2)
    if low % 2 != 0 or high % 2 != 0:
        return count + 1
    else:
        return count
    
def countOdds3(low, high): #5th Try (15 ms, average with everyone else)
    return (high + 1) / 2 - low / 2

'''
What did I learn?
1) By just adding 1 on one side it's possible to change everything.
'''