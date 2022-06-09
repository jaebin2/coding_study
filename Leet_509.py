fibo_dic = {}
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    try:
        fibo_dic[n] = fibo_dic[n-1] + fibo_dic[n-2]
    except:
        fibo_dic[n] = fibo(n-1) + fibo(n-2)
    return fibo_dic[n]
    
class Solution:
    def fib(self, n: int) -> int:
        return fibo(n)
