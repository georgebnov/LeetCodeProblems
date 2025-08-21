s = 'rat'
t = 'car'

def isAnagram(s, t):
        if len(s) != len(t):
            return False
        
        counts = {} #creating a frequency map, where it will store the chracters and how many times they occured in that word
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1 #counts is the dictionary, .get(key, default) = means get the character, if its not there, default is 1, if its there then add 1, and so we created a count[ch] just a disctionary of characters for the word s

        for ch in t:
            if ch not in counts: #the letter doesn't exist = not an anagram
                return False
            counts[ch] -= 1 #if it exists, remove 1 frequency of that character form it's count, and disctionary
            if counts[ch] < 0: #if the letter exists but the frequency is 0 or less then not an anagram
                return False

        for c in counts.values(): #grabs all the values from each key in the dictionary and then if there any left overs it wont be 0 so its false but if its 0 then its an anagram
            if c != 0:
                return False

        return True

print(isAnagram(s, t))

def isAnagramXOR(s, t): #this is smart but would not work, because "aa" + "bb" 2 pairs of letter put together would sqtill be equal to 0 at the end. But they are not anagrams
    if len(s) != len(t):
        return False
    
    wordsTotal = s + t
    xor_sum = 0
    for ch in wordsTotal:
        xor_sum ^=ord(ch)
    if xor_sum == 0:
        return True
    return False

print(isAnagramXOR(s, t))

'''
What did I learn?
1) dictionary[something] is a disctionary that contains the key and the frequency of that key (must initalize the dictionary first)
2) dictionary.get(key, default) is a method that returns the value for the key if it exists, if not it is 0.
3) dictioney.values() is getting all the values without their keys, (I bet there is something for only taking out the keys)
'''