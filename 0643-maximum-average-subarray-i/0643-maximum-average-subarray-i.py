class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0

        for i in range(k):
            window_sum += nums[i]
        
        max_sum = window_sum
        left = 0

        for right in range(k, len(nums)):
            window_sum += nums[right]
            window_sum -= nums[left]
            if max_sum < window_sum:
                max_sum = window_sum
            left += 1
        return max_sum / k

        