class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        tmp1, tmp2 = edges[0]
        for tmp3, tmp4 in edges[1:]:
            if (tmp3 == tmp1) | (tmp3 == tmp2):
                return tmp3
            if (tmp4 == tmp1) | (tmp4 == tmp2):
                return tmp4
