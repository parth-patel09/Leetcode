class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i,j=0,0
        ans =""
        while True:
            if i < len(word1) :
                ans += word1[i]
            if j < len(word2) :
                ans += word2[j]
            if i >= len(word1) and i >= len(word2) : 
                break
            i+=1
            j+=1
        return ans

print(Solution().mergeAlternately("abc","pqr"))