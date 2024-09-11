class Solution(object):
    def minEatingSpeed(self, piles, h):
        def canEatBananas(k):
            hours = 0
            for pile in piles:
                hours+= math.ceil(pile/k)
            return hours<=h
        low = 1
        high = max(piles)
        while low<high:
            mid = (low+high)//2
            if canEatBananas(mid):
                high = mid
            else:
                low = mid+1
        return low
        