haystack = 'leetcode'
needle = 'leeto'

n = len(haystack)
m = len(needle)

def strStr (haystack, needle):
    for i in range(n - m + 1): #the difference in the word + 1, will give the space for the needle word to be inside haystack still. if it can't right away return -1 (smart)
        print(i, haystack[i], needle[i])
        if haystack[i] == needle[0]: #if the letter of the haystack matches the first letter of the needle word, make j = 0
            j = 0
            while j < m and haystack[i + j] == needle[j]: #j is a counter of the letters that are correct, so keep looping till j counter reaches the amount of letters in needle word and the number haystack[i+j] (i = is the letter it started from, j the counter,) is equal to needle[j], so the letters of the word are equal then keep looping
                print(i, haystack[i +j], needle [j], j, m),
                j += 1
            if j == m: # when j reaches m then return the i which is the inital position of the letter where it started from 
                return i
    return -1 #if not enough sapce for the full word and the word is not there return -1

print(strStr(haystack, needle))

'''
What did I learn:
1) soemtimes solving an issue is a numebers game, rather than going till the end just check if the word fits into the haystack, from there if not and the letter doesnt match give out answer right away
2) I'm thinking in the way of words flowing but I need to change my mind to comparison and counting. Rather than saying "keep going till..." say more of "while this and this..."

What I need to learn:
1) how to think in terms of loops, and makin gthe loops smart, not just doing 1 loop for 1 letter, but how can I speed up the process or doing it smarter.
'''