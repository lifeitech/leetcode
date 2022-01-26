class Solution:
    def diStringMatch(self, S):
        left = 0
        right = len(S)
        A = []
        for i in S:
            if i == 'I':
                A.append(left)
                left += 1
            else:
                A.append(right)
                right -= 1
        A.append(right)
        return A