class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        Output = []
        tmp1={}
        tmp2={}
        
        for i in p:
            if i in tmp2.keys():
                tmp2.update({i:tmp2[i]+1})
            else:
                tmp2.update({i:1})
        
        for i in s[:len(p)]:
            if i in tmp1.keys():
                tmp1.update({i:tmp1[i]+1})
            else:
                tmp1.update({i:1})
 
        if tmp1 == tmp2:    
            Output.append(0)    
            
        for i in range(len(s)-len(p)):
            i+=1
            j = i + len(p) - 1
            
            if s[j] in tmp1.keys():
                tmp1.update({s[j]:tmp1[s[j]]+1})
            else:
                tmp1.update({s[j]:1})
                
            tmp1.update({s[i-1]:tmp1[s[i-1]]-1})
            if tmp1[s[i-1]] == 0:
                del tmp1[s[i-1]]
   
            if tmp1 == tmp2:    
                Output.append(i)    
            
        return Output