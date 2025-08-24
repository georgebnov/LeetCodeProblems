s = "day"

def lengthOfLastWord(s): # My Method (0ms, 12.64MB)
    length = 0
    i = len(s) - 1
    if len(s) == 1:
        return len(s)
    while i >= 0:
        print(i, s[i], length)
        if s[i] == " ":
            if [i-1] != " ":
                length = 0
                i -= 1
            else:
                i -= 1
        if s[i] != " ":
            if s[i-1] != " ":
                length += 1
                i -= 1
            elif s[i-1] == " ":
                length += 1
                return length
            else:
                length += 1
                return length
    return length

print (lengthOfLastWord(s))

'''
What did I learn:
1) Don't forget that sometimes, things get out of the loops. Not everything will end inside the loop. So just making sure that outside the loop it also ends, will go a long way.
2) "" != " ". if I am trying to compare to a space then it needs to be " ". "" = just means a cleared string.
'''