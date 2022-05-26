class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        tmp_dic = {}
        Output = []
        
        for j, i in enumerate(groupSizes):
            if i in tmp_dic.keys():
                tmp_dic[i].append(j)
            else:    
                tmp_dic[i] = [j]
        
        for i in sorted(list(tmp_dic.keys())):
            tmp = 0
            for _ in range(int(len(tmp_dic[i])/i)):
                Output.append(tmp_dic[i][tmp:tmp+i])
                tmp += i
                
        return Output
