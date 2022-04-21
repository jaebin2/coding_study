# 1268. Search Suggestions System
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        Output = []
        products.sort()
        s = ""
        for i in searchWord:
            s += i
            tmp = []
            for j in range(len(products)):
                if products[j].find(s) == 0:
                    tmp.append(products[j])
            products = tmp
            if len(tmp) >= 3:
                tmp = tmp[0:3]
            Output.append(tmp)
        return Output