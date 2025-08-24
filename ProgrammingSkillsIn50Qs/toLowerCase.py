s = "HELLO WORLD!"
def toLowerCase(s): #my simplest way (using pre-built function) (0ms, 12.55MB)
    return s.lower()

def toLowerCase2(s): #trying to solve without using the pre-built function) (0ms, 12.53MB)
    newS = ""
    for i in range(len(s)):
        if 65 <= ord(s[i]) <= 90:
            newS += chr(ord(s[i]) + 32)
        else:
            newS += s[i]
    return newS
print(toLowerCase2(s))

'''
What did I learn:
1) Using pre-built functions are more momory used then when doing making it on our own.
'''