class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tmp = {}
        val_set = set()
        
        if n == 1:
            return 1
        
        for value, key in trust:
            if key in tmp.keys():
                tmp[key].add(value)
            else:
                tmp[key] = set([value])
            val_set.add(value)

        for i, j in tmp.items():
            if len(j) == n-1:
                if i not in val_set:
                    return i
            
        return -1
