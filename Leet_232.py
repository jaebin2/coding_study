class MyQueue:

    def __init__(self):
        self.count = 0
        self.di = {}
        self.dimin = 0

    def push(self, x: int) -> None:
        self.di[self.count] = x
        self.count += 1

    def pop(self) -> int:
        tmp = self.di[self.dimin]
        del(self.di[self.dimin])
        self.dimin += 1
        return tmp

    def peek(self) -> int:
        return self.di[self.dimin]

    def empty(self) -> bool:
        if self.di == {}:
            return True
        else:
            return False