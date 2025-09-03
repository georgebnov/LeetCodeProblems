salary1 = [4000,3000,1000,2000]
salary = [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000] #this one had issues with the floats. but thhats because it overflowed the bits.

def average(salary):
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