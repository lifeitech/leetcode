class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        a = 0
        for s in S:
            if s in J:
                a = a + 1
        return a