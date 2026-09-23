"""
U (understanding):
    Inputs: string of characters
    Output: boolean
    Edge cases: empty, not characters, null values, wrong characters
M (match):
    Stack
P:
    1. Create Stack
    2. Create hash map with opening and closing brackets as keys:values
    3. for loop string, getting every character
        if it's a closing bracket 
            check if character is in the hash map
            check last
        elif it's not an opening bracket, it's not in the hashmap
            append it to the stack
I:
R:
E (evaluation):
    Time complexity: O(n)
    Space complexity: O(n), where n is the number of elements in the stack
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketDict = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for bracket in s:
            if bracket in bracketDict:
                if stack and stack[-1] == bracketDict[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False
        