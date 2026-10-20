class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        interate through nums and maintain the window size of target number
        use a min_length to update and track the length of subarray under constraint
        start with left
        '''
        min_length = float("inf")
        left = 0
        sum_subarray = 0

        for right in range(len(nums)):
            sum_subarray += nums[right] 

            while sum_subarray >= target:
                min_length = min(min_length, right - left +1)
                sum_subarray -= nums[left]
                left += 1

        if min_length == float("inf"):
            return 0
        else:
            return min_length

            

