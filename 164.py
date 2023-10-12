class Solution(object):
    def maximumGap(self, nums):
        num = sorted(nums)
        max =0
        for i in range (0,len(nums)-1):
            if num[i+1] - num[i] > max : 
                max = num[i+1] - num[i]
        return max
print(Solution().maximumGap([3,9,6,1]))