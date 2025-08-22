digits = [1,2,3]
def plusOne(digits):
    number = 0
    power = len(digits) - 1
    for i in range(len(digits)):
        tenth = 10 ** power
        number = number + (digits[i] * tenth)
        power -= 1
    
    number += 1

    answer = [int(d) for d in str(number)]
    return answer
print(plusOne(digits))

'''
What did I learn: (did it on my own fully)
1) [int(d) for d in str(number)] means = turns number into string, then loops over each number, and turns it into an integer, and because it's wrapped in [] it creates the array
2) apparently power is **
'''