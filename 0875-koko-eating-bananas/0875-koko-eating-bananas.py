from math import ceil
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low=1
        high=max(piles)
        while low<high:
            mid=(low+high)//2
            hoursneeded=0
            for pile in piles:
                hoursneeded+=(pile+mid-1)//mid
            if hoursneeded<=h:
                high=mid
            else:
                low=mid+1
        return low