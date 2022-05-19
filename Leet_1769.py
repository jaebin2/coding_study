class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        Output = []
        tmp = 0
        
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j]=="1":
                    tmp += abs(j - i)
            Output.append(tmp)    
            tmp = 0
            
        return Output   
