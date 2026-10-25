class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack=[]
        n=len(temperatures)
        answer=[0 for _ in range(n)]
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                j=stack.pop()
                answer[j]=i-j
            stack.append(i)
        return answer