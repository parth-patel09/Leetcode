class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        ans ={}
        for word in strs:
            
            word1=''.join(sorted(word))
            print(word1)
            if word1 in ans.keys() :
                ans[word1].append(word)
            else :

                 ans[word1]= [word]
        print(ans)
        return ans.values()
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))