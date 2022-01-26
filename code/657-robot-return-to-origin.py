class Solution:
    def judgeCircle(self, moves: str) -> bool:
        left = moves.count('L')
        right  = moves.count('R')
        up = moves.count('U')
        down = moves.count('D')
        return left == right and up == down