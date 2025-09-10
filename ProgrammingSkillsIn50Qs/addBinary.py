
a = "11"
b = "1"
def addBinary(a, b): #My way:  0 ms | Beats 100.00%

    inta = int(a, 2)
    intb = int(b, 2)

    sum = inta +intb

    sumBin = bin(sum)
    sumBin = sumBin[2:]

    return sumBin
print(addBinary(a, b))

'''
Would liek to solve it wihtout using int and bin
but rather actually turn the numbers into integers and then back into binary wihtout python library.
'''