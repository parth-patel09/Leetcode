class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float('inf') 
        for n in nums: 
            if n <= first: 
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
    

print(Solution().increasingTriplet([6,7,1,2,8]))