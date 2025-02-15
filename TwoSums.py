from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = defaultdict(int,dict.fromkeys(set(nums),1))
        sol_list=[]
        for i,x in enumerate(nums):
            if num_dict[target-x]:
                if target-x!=x or ( target-x==x and nums.count(x) > 1):
                    sol_list.append(i)
        return sol_list