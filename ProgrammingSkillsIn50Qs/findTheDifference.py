s = "abcde"
t = "abfghcde"
def is_subsequence(s, t):
    x = 0
    print(s+t)
    for ch in s + t: #for each character that got placed into one making a full big array 
        x = x ^ ord(ch) #ord => turns all characters into unicode integer like a = 97 and then XORs them meaning finding pairs, and a^a = 0 but if 2 characters are different like a^b it will find the float point, so cumultive end will turn x into the non pair number.
        print(ch, ' - ', ord(ch), ' - ', x)
    return chr(x) #return only the array of x with all the not same numbers
print(is_subsequence(s, t)) #print the fucntion answer

"""
What Did I Learn:
1) ^ = XOR operator -> it finds symmetrical alignment and then removes it, in binary it works if its a pair = 0 and if they differ it turns into 1.
2) ord = function that turns characters into their unicode numbers like a = 97 or A = 65

What I Didn't understand:
1) x ^= ord(ch) how did this whole concocsion turned into saving only the last one into variable x...
-> solution: the answer is the infinite addition of XOR. 97 ^ 98 = 1100001 ^ 1100010 = 0000011 = 3 when you keep going it automatically clears up all the pairs,
   Seems like the cumulitive XOR right away clears out the pair numbers or character (if changed to unicode)
"""

x = ...