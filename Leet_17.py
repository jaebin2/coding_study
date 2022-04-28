class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        Output = []
        num_dic = {'2':('a','b','c'),'3':('d','e','f'),'4':('g','h','i'),'5':('j','k','l'),'6':('m','n','o'),'7':('p','q','r','s'),'8':('t','u','v'),'9':('w','x','y','z')}
        
        if len(digits) == 0:
            return Output
        
        elif len(digits) == 1:
            for i in num_dic[digits[0]]:
                Output.append(i)
            return Output
            
        elif len(digits) == 2:
            for i in num_dic[digits[0]]:
                for j in num_dic[digits[1]]:
                    Output.append(i+j)
            return Output
        
        elif len(digits) == 3:
            for i in num_dic[digits[0]]:
                for j in num_dic[digits[1]]:
                    for m in num_dic[digits[2]]:
                        Output.append(i+j+m)
            return Output
        
        elif len(digits) == 4:
            for i in num_dic[digits[0]]:
                for j in num_dic[digits[1]]:
                    for m in num_dic[digits[2]]:
                        for n in num_dic[digits[3]]:
                            Output.append(i+j+m+n)
            return Output