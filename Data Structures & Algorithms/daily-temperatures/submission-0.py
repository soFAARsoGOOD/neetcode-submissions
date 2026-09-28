"""
U:
    Input: List of int
    Output: List of int
M:
    Stack

1. Push the currTemp into the stack

2. For each element, loop forward
    dayCounter += 1
    
    if initialTemp < currentTemp
        continue
    else:
        stack.append(dayCounter)
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                output[stackInd] = i - stackInd
            stack.append((t,i))
        return output

                