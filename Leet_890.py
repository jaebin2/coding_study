# 890. Find and Replace Pattern
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def change(word):
            word_dict = {}
            tmp =  []
            for i, j in enumerate(word):
                word_dict.setdefault(j, str(i))
            tmp = [word_dict[i] for i in word]    
            return tmp
        pat = change(pattern)
        Output = [i for i in words if change(i) == pat]
        return Output