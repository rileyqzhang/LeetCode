class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        The window size should be at most k
        use set to check repetitive number
        iterate over nums
        '''
        seen = set()
        left = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                if right - left <= k:
                    return True
                else:
                    seen.remove(nums[left])
                    left += 1

            seen.add(nums[right])
        
        return False
                
                 
                


        
