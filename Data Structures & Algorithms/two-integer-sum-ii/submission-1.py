class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1 #create pointers for first and last elements

        while left < right: #this will keep iterating until we find the solution
            sum = numbers[left] + numbers[right] 
            if sum == target: #best case scenario: already equal to target
                return [left+1, right+1]
            elif sum < target: #if sum is less than target, increment left pointer to larger number
                left += 1
            else: #if sum is greater than target, increment right pointer to smaller number
                right -= 1

        