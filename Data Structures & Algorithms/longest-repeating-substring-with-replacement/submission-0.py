class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #used to keep track of the size of valid subarray
        res = 0 #answer

        l = 0 
        maxf = 0 #keep track of longest so far

        for r in range(len(s)): #for loop: expanding
            count[s[r]] = 1 + count.get(s[r], 0) #adding the count
            maxf = max(maxf, count[s[r]]) #updating your answer

            while (r - l + 1) - maxf > k: #while loop - shrink = removing
                count[s[l]] -= 1 #decrementing the count
                l += 1 #shrink window by moving left pointer to the right
            res = max(res, r - l + 1)

        return res