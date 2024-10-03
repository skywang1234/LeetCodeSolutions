class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = cur = 0
        time = [(target-pos)/s for pos, s in sorted(zip(position, speed))]
        for t in time[::-1]:
            if t > cur:
                fleets+=1
                cur = t
        return fleets