class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        elif len(flowerbed) == 1 and flowerbed[0] == 1 and n==0:
            return True
        elif len(flowerbed) == 1 and flowerbed[0] == 1:
            return False

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and n != 0:
                if i == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n-=1
                elif i == len(flowerbed)-1:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        n-=1
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n-=1
        
        if n==0:
            return True
        else:
            return False
print(Solution().canPlaceFlowers([1,0,0,0,0],2))