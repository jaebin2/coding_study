class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        tmp = list(range(n))
        idx = 0

        while len(tmp) != 1:
            idx += k - 1
            while idx >= len(tmp):
                idx -= len(tmp)

            del(tmp[idx])
            
        return tmp[0] + 1
