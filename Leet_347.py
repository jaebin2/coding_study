class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Output = []
        nums_dict = {}
        
        for i in nums:
            if i not in nums_dict.keys():
                nums_dict[i] = 1
            else:
                nums_dict[i] = nums_dict[i] + 1
            
        sorted_dict = sorted(nums_dict.items(), key = lambda item: item[1], reverse = True)

        for i in sorted_dict[0:k]:
            Output.append(i[0])
        
        return Output
