class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            try:
                count[i] = count[i] + 1
            except:
                count[i] = 1
            
        for i in count.keys():
            if count[i] > len(nums)/2:
                return i
