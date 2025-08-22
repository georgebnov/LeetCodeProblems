nums = [0,1,0,3,12]
output = [1,3,12,0,0]

def moveZeroes(nums: list[int]) -> None:
    index2 = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[i]
            nums[i] = nums[index2]
            nums[index2] = temp
            index2 += 1
            print(nums, i)
        
    return nums

print(moveZeroes(nums))
            
'''
What did I learn:
1) in python, if you write: nums[index2], nums[i] = nums[i], nums[index2], which does the exact same thing if I saved the number first in the temp and then change spots and place the temp number into the other one.
'''