class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        res = []
        for word in words:
            w = word.lower()
            wset = set(w)
            if wset <= set1 or wset <= set2 or wset <= set3:
                res.append(word)
        return res