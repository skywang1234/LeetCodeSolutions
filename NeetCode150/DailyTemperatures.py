class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                idx = stack.pop()
                output[idx]=i-idx
            stack.append(i)
        return output