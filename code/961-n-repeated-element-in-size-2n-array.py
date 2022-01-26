class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        a = set()
        for i in A:
            if i not in a:
                a.add(i)
            else:
                return i