class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            daysneeded=1
            cap=0
            for weight in weights:
                if cap+weight>mid:
                    daysneeded+=1
                    cap=weight
                else:
                    cap+=weight
            if daysneeded>days:
                low=mid+1
            else:
                high=mid
        return low
                
        