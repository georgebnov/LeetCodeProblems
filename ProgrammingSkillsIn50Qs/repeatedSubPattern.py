s = "abababab"
# s = "bacbbacb" (a,2), (b,4), (c,2)
# s = "ababba" -> for this one it woudl work as the dictionary still works here. BUT the are not the same...
# if there is a value that is 1 return false immediately
#chech if the greates value is a multiple of the smallest value if it is then true, if not then false.

'''def repeatedSubstringPattern(s): #this didn't work
    count ={}
    
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
        print("dictionary =", ch, count.values())

    #check if the values of all keys are the same
    for value in count.values():
        print(value)
        if value == 1:
            return False
        
    max_value = max(count.values())
    min_value = min(count.values())
    print(max_value, min_value)
    if max_value % min_value != 0:
        return False

    return True
            
print(repeatedSubstringPattern(s))
'''

'''
The way to solve it: #didnt use this method
1) go letter by letter and append letters until the first letter repeats
2) if the next letter repeats again, then check the next letter, if the first letter again repeats then keep goin guntil the letter goes to the seocn dletter. (to get repeated words like bacbbacb, or bacbbbbacbbb)
3) then just create dictionary with the repeated word, and if there is more then 1 key in the dictionary then return false, if its only 1 return true.
'''

def repeatedSubstringPattern(s):
    length = len(s)

    for i in range(1, length // 2 + 1):
        if length % i == 0: # make sure that the number is equally divisable.
            checkWord = s[:i] #splitting the word to that specific length ex. s = "abababab", i = 3 , s[:i] = "abab"
            print(checkWord)
        if checkWord * (length // i) == s: #we know i is perfectly divisble by the total length, so we can find that factor. From there we can create a new word by appending the checkWord by the same factor. If the word is the same then we good!
                return True, checkWord
    return False, "none"
            
print(repeatedSubstringPattern(s))

'''
What did I learn?
1) multiplying (*) with strings means concatenation multiple times. Meaning if I multiple s = "ab", newWord = s * 2 = "abab"
2) range is function where you need to give start an end range(start, end)
3) [:i] (in this case) it can split the string at the specific spot. so s = "abababab", i = 3, s[:i] = "abab"
'''