class Solution(object):
    def search(self, nums, target):
        
        if target not in nums:
            return -1
        else:
            for n in nums:
                if n == target:
                    return nums.index(n)
                

        