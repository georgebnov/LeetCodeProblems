word1 = 'abcd'
word2 = 'pqq'
print(word1, word2)

def mergeAlternately(word1, word2):
    word1array = list(word1) # splitting the words into arrays
    word2array = list(word2)
    merged = []
    for i in range(max(len(word1array), len(word2array))): #find the size of the array of each word, take the biggest one, make a rangr for i which is from 0 to the biggest len
        if i < len(word1array):
            merged.append(word1array[i]) 
        if i < len(word2array):
            merged.append(word2array[i])
        #append the letters 1 by 1 until the i is not done, and even if the word is smaller, it will still append everythign else at the end, as it takes the biggest len
    return "".join(merged)

print(mergeAlternately(word1, word2))

'''
What did I learn:
1) list() = splits a string into an array of letters
2) len() = the number of letters in the string
3) max() = choses the biggest numeber from the lsit given to it and returns it
4) range() = used for loops, to give a range from 0 to a specific number you give it.
5) {arrayName}.append() = simple way to add something into the array you want.
6) "".join() = joins the array into a string, so you can return it as a string, not an array.
'''