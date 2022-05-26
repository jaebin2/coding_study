class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        tmp_dic = {}
        Output = 0
        
        for i in stones:
            if i in tmp_dic.keys():
                tmp_dic[i] += 1
            else:    
                tmp_dic[i] = 1
         
        for i in jewels:
            if i in tmp_dic.keys():
                Output += tmp_dic[i]
                
        return Output
