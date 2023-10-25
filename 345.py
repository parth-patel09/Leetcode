class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        v=['a','e','i','o','u','A','E','I','O','U']
        l=list(s)
        j=len(l)-1
        while i < j:
            if l[i] not in v and l[j] not in v :
                i+=1
                j-=1
            elif l[i] in v and l[j] not in v :
                j-=1
            elif l[i] not in v and l[j] in v :
                i+=1
            else:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
                j-=1
                i+=1
            
        return ''.join(l)
print(Solution().reverseVowels('hello'))