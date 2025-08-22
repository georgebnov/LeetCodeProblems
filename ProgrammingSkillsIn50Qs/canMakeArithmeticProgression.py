arr = [5,4,3,2,1]

def myOwnSorting(arr): #my own .sort()
    print(arr)
    for num in range(len(arr)):
        for k in range(len(arr)-1):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
            
    return arr

print(myOwnSorting(arr))

def canMakeArithmeticProgression(arr): #This solution beat 100% of people apparently haha
    arr.sort()

    change = arr[1] - arr[0]
    
    for i in range(1 , len(arr) - 1):
        if arr[i] + change != arr[i + 1]:
            return False
    return True

#I want to try to solve it without useing function .sort()

def canMakeArithmeticProgression2(arr): #using my own sorting function

    arr = myOwnSorting(arr)
    change = arr[1] - arr[0]
    
    for i in range(1 , len(arr) - 1):
        if arr[i] + change != arr[i + 1]:
            return False
    return True

print(canMakeArithmeticProgression2(arr))

'''
What did I learn:
1) Sorting is the fastest when you just switch one by one, each. each individual will have to flip with all the other integers, and this whol process will go on for the total length of the array
2) .sort() = really fast way of sorting arrays, pythons already exisitng function.
3) Don't forget that when you call somethign and it's undefined it will throw an error, like when you defined, just the range to be until len(arr) but then you ask to compare to the next integer in the arr. but there is no next when it gets to the end. So it was throwing an error.
'''