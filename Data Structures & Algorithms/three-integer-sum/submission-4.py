class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums2 = sorted(nums)

        ans = set()
        for i, n in enumerate(nums2[:len(nums2)-2]):
            if i > 0 and nums2[i] == nums2[i-1]:
                continue
            i2 = i+1
            i3 = len(nums2) - 1
            
            
            while i2 < i3:
                sum1 = n + nums2[i2] + nums2[i3]
                if sum1 < 0:
                    i2 +=1
                elif sum1 > 0 :
                    i3 -=1
                else:
                    ans.add((n,nums2[i2], nums2[i3]))
                    i2 +=1
                    i3 -=1
                    
                    

            
        return list(ans)