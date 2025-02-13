class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sol_list=[]
        for i,x in enumerate(nums):
            if target-x in nums:
                if (target-x==x and nums.count(x)>1) or target-x!=x:
                    sol_list.append(i)
        return sol_list