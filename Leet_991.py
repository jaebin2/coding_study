class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        while startValue != target:
            if target < startValue:
                startValue - target
                count += startValue - int(target)
                break
            if target % 2 == 1:
                target += 1
            else:
                target /= 2
            count += 1
        return count
