class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        Output = []
        num_dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
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
