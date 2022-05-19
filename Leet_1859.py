class Solution:
    def sortSentence(self, s: str) -> str:
        s = list(s.split())
        s_dic = {}
        Output = ""
        
        for i in range(len(s)):
            s_dic[int(s[i][-1])] = s[i][:-1]
        
        Output = s_dic[1]
        for i in range(len(s)-1):
            i = i + 2
            Output = Output + " " + s_dic[i]
            
        return Output    
