class MyStack:
    def __init__(self):
        self.ary = []

    def push(self, x: int) -> None:
        self.ary.append(x)

    def pop(self) -> int:
        return self.ary.pop()

    def top(self) -> int:
        return self.ary[-1]
        
    def empty(self) -> bool:
        if self.ary == []:
            return True
        else:
            return False
