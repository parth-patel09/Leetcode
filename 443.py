class Solution:
    def compress(self, chars: list[str]) -> int:
        num=0
        i=0
        current=''
        while i<len(chars):
            if current == '' :
                current=chars[i]
                num+=1
                i+=1
            elif chars[i] == current :
                num+=1
                if i<len(chars)-1 and chars[i+1] == current :
                    chars.pop(i)
                else :
                    if i == len(chars)-1:
                        chars.pop(i)
                        while True :
                            if int(num/10) !=0 :
                                chars.insert(i,str(num%10))
                                num=int(num/10)

                            else :
                                chars.insert(i,str(num))
                                break
                        break
                    flag =0
                    chars.pop(i)
                    while True :
                            if int(num/10) !=0 :
                                chars.insert(i,str(num%10))
                                num=int(num/10)
                                flag+=1
                            else :
                                chars.insert(i,str(num))
                                break
                    i+=flag
                    i+=1
                    current=''
                    num=0
            else :
                current=''
                num=0
        return len(chars)


print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))