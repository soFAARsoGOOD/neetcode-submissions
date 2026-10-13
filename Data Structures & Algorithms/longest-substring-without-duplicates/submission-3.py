'''
Pseudocode
1. Left = right = 0
2. for num in array:
    1. Add right to window
    2. right++

    3. While window is invalid
        1. remove left
        2. left++
    
    4. Update answer
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        result = 0
        seen = set()

        for end in range(len(s)): #iterate through the string
            while s[end] in seen: #check to see if the new character is a duplicate
                seen.remove(s[start]) #remove the duplicate character from the set
                start += 1
            seen.add(s[end])
            result = max(result, end - start + 1)
        return result


        
        