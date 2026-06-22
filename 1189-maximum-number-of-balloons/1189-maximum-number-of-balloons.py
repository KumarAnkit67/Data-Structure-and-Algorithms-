class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        x = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }
        for char in text:
            if char in x:
                x[char] += 1

        return min(
            x['b'],
            x['a'],
            x['l'] // 2,
            x['o'] // 2,
            x['n']
        )

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna