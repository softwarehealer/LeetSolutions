class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = defaultdict(int)
        max = -1
        for x in nums:
            ind_sum = 0
            y = x
            while x:
                ind_sum += (x%10)
                x = x // 10
            if count[ind_sum]!=0:
                if count[ind_sum] + y > max:
                    max = count[ind_sum] + y
                if count[ind_sum] < y:
                    count[ind_sum] = y
            else:
                count[ind_sum] = y
        return max