class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r, mid = 0, len(nums)-1, len(nums)//2
        leftHalf = False
        while l <= r:
            mid = (l + r) //2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                #First half sorted
                leftHalf = True
            elif nums[l] > nums[mid]:
                #second half sorted
                leftHalf = False
            if leftHalf:
                if target >= nums[l] and target < nums[mid]:
                    r= mid -1
                else:
                    l = mid + 1
            if not leftHalf:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
