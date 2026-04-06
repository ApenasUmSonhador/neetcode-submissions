class DynamicArray:
    def __init__(self, capacity: int):
        self.arr = [None] * capacity    # usamos None para indicar vazio
        self.size = 0                   # número de elementos
        self.capacity = capacity

    def get(self, i: int) -> int:
        # i é garantido válido pelo problema
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # i é garantido válido pelo problema
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # garantido não vazio pelo problema
        self.size -= 1
        val = self.arr[self.size]
        self.arr[self.size] = None
        return val

    def resize(self) -> None:
        self.arr += [None]*self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity