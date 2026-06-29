class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        third = float('-inf')
        second = float('-inf')
        first = float('-inf')
        
        for i in nums:
            if i == first or i == second or i == third:
                continue
            if i > first:
                third = second
                second = first
                first = i
            elif i > second:
                third = second
                second = i
            elif i > third:
                third = i

        if third == float('-inf'):
            return first
        else:
            return third    



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna