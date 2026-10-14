class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        mid = len(nums)//2
        #modified binary search
        while l < r:
            mid = (l + r) //2
            #Check mid and boundary element
            if nums[mid] <= nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            #assuming all are unique elements
        return nums[l]