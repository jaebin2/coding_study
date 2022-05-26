class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        Output = 0
        count = 1
        
        nums.sort()
        nums.append(0)
        
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                count += 1
            else:
                Output += count*(count-1)/2
                count = 1
   
        return int(Output)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        tmp_dic = {}
        Output = 0
        
        for i in nums:
            if i in tmp_dic.keys():
                tmp_dic[i] += 1
            else:    
                tmp_dic[i] = 1
         
        for i in tmp_dic.keys():
            if tmp_dic[i] != 1:
                Output += tmp_dic[i]*(tmp_dic[i]-1)/2
                
        return int(Output)
