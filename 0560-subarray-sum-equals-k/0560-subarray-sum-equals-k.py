class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}
        count = 0
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum - k in prefix_sum:
                count += prefix_sum[current_sum - k]
            prefix_sum[current_sum] = prefix_sum.get(current_sum,0) + 1
        return count        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna