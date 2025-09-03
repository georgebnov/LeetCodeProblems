salary1 = [4000,3000,1000,2000]
salary = [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000] #this one had issues with the floats. but thhats because it overflowed the bits.

def average(salary):  #My Solution (0ms | Beats = 100%, 12.53MB | Beats 12.82%)
    avg = 0
    divisor = 0

    max = findMaxMin(salary)[0]
    min = findMaxMin(salary)[1]
    print(max)
    print(min)

    for i in range(len(salary)):
        if salary[i] != min and salary[i] != max:
            avg += salary[i]
            divisor += 1

    return round(avg / divisor, 5)

def findMaxMin(salary):
    min = salary[0]
    max = 0
    for i in range(len(salary)):
        if salary[i] < min:
            min = salary[i]
        elif salary[i] > max:
            max = salary[i]
    
    return max, min

print(average(salary))


'''
What did I learn?
1) apparently there is a differnec ebetween python3 and python. When I was dividing numbers, in python unless it was a float it floor divides it. so 10/3 = 3 but 10.0/3 = 3.3333
2) Needs to not forget the self.function() that how you call it in class.
'''