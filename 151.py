class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        l.reverse()
        return ' '.join(l)
        
print(Solution().reverseWords("this is Parth"))