s = "MCMXCIV"
'''
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
I can be placed before V (5) and X (10) to make 4 and 9. 
IV = 4
IX = 9
X can be placed before L (50) and C (100) to make 40 and 90. 
XL = 40
XC = 90
C can be placed before D (500) and M (1000) to make 400 and 900.
CD = 400
CM = 900
'''
def romanToInt(s): #My Version (8ms, 12.42MB)
    t = s + "Q" 
    number = 0
    i = 0
    while i < len(s):
        if t[i] == "M":
            number += 1000; i += 1
        elif t[i] == "D":
            number += 500; i += 1
        elif t[i] == "C":
            if t[i+1] == "D":
                number += 400; i += 2
            elif t[i+1] == "M":
                number += 900; i += 2
            else:
                number += 100; i += 1
        elif t[i] == "L":
            number += 50; i += 1
        elif t[i] == "X":
            if t[i+1] == "L":
                number += 40; i += 2
            elif t[i+1] == "C":
                number += 90; i += 2
            else:
                number += 10; i += 1
        elif t[i] == "V":
            number += 5; i += 1
        elif t[i] == "I":
            if t[i+1] == "V":
                number += 4; i += 2
            elif t[i+1] == "X":
                number += 9; i += 2
            else:
                number += 1; i += 1
        else:
            i += 1
    return number

print(romanToInt(s))

def romanToInt(s): #ChatGPTs version which is mcuh smarter
    val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0
    i = 0
    while i < len(s):
        if i+1 < len(s) and val[s[i]] < val[s[i+1]]:
            total += val[s[i+1]] - val[s[i]]
            i += 2
        else:
            total += val[s[i]]
            i += 1
    return total

'''
What did I learn:
1) Comapring my version to ChatGPTs version, it seems that there was an easier way (if next letter exist, and is smaller, than do 1 - the other and add, if not just add the value.)
2) How to learn to think this way I dont know yet.
'''