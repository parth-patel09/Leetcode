class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m=max(candies)
        answer=[]
        m = m - extraCandies
        for i in range (len(candies)):
            if candies[i] >= m:
                answer.append(True)
            else:
                answer.append(False)
        return answer


print(Solution().kidsWithCandies([2,3,5,1,3],3))