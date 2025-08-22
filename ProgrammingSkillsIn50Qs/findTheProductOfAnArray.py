nums = [-1,1,-1,1,-1]


def arraySign(nums):
    x = 1
    for i in range(len(nums)):
        x = x * nums[i]

    answer = signFunc(x)
    return answer
    
def signFunc(x):
    if x == 0:
        return 0
    if x > 0:
        return 1
    else:
        return -1
    
print(arraySign(nums))

# Solution on LeetCode:

class Solution(object):
    def arraySign(self, nums):
        x = 1
        for i in range(len(nums)):
            x = x * nums[i]

        return self.signFunc(x)
        
    def signFunc(self, x):
        if x == 0:
            return 0
        if x > 0:
            return 1
        else:
            return -1
        
'''
What did I learn:
1) So apparently there are things called classes in Python, whcih are in simple the blueprint to instances. Instances are just whats created from the class. There are attributes and methods, which are either variables or functions that belong to the class.
2) Python uses self like this: when we call self.signFunc(x), it says to look for the signFunc function that belongs to this class. So if we had another function called signFunc outside of this class, it would not be called.

So in simple when we are solving somethign inside a class, we use self, if we want to call something outside of the class, we dont use self.
'''