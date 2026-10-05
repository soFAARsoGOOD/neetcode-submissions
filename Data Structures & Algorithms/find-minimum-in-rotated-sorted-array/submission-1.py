class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1 

        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]: #if the mid is greater than the right, we know the minimum value is going to be to the section to the right of mid
                left = mid + 1 #we know mid can't be the minimum, so move to the right of mid
            else:
                right = mid #if nums[mid] is less than right it COULD be the min, but we know for sure the min is somewhere on that side of the array.
        return nums[left] #once we've squeezed enough, left and right will converge onto the min value, so we don't need to do the last test like with a regular binary search.
