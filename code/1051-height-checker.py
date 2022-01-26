class Solution:
    def heightChecker(self, heights):
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))