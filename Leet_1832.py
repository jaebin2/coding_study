class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        tmp_dic = {}
        
        for i in sentence:
            tmp_dic[i] = None
        
        if len(tmp_dic) == 26:
            return True
        else:
            return False
