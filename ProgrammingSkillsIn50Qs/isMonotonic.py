nums = [1, 2]
nums1 = [-5,-5,-5,-5,-2,-2,-2,-1,-1,-1,0]
nums2 = [9]
nums3 = [2,2,2,1,4,5]
nums4 = [1,1,1]

def isMonotonic(nums): #My solution (31ms, 24.24MB)
    for k in range(len(nums) - 1):
        if nums[k] != nums [k + 1]:
            if nums[k] >= nums[k + 1]: #monotonic decreasing
                for i in range(len(nums) - 1):
                    if nums[i] < nums[i + 1]:
                        return False
                return True
            if nums[k] <= nums[k + 1]: #monotonic increasing
                for i in range(len(nums) - 1):
                    if nums[i] > nums[i + 1]:
                        return False
                return True
    return True

def isMonotic2(nums): #My fathers solution (56ms, 20.61MB)
    direction = 0
    for k in range(len(nums) - 1):
        if ((nums[k] - nums[k+1]) < 0 and direction == 1) or ((nums[k] - nums[k+1]) > 0 and direction == -1): return False
        elif direction == 0 and (nums[k] - nums[k+1]) > 0 : direction = 1
        elif direction == 0 and (nums[k] - nums[k+1]) < 0 : direction = -1
               
    return True

print(isMonotonic(nums))

'''
What did I learn:
1) Use knoweldge from discrete math more. Put a hypothesis (in our case we say everything is true), then the tests must either approve or disapprove the hypothesis.
2) Apparently from the tests between my fathers and I, my code performed faster but has a larger memory space (the guess is because I don't have a storage variable, that changes, mine just flips each one and says true or false), but his is slower but less memory.
'''