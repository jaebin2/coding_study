class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        Output = []

        for i,v in enumerate(words):
            for j,m in enumerate(words):
                if i != j:
                    text = ""
                    text = v + m
        
                    if text == text[::-1]:
         
                        Output.append((i,j))
                    
        return Output
