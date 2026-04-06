class DynamicArray:
    def __init__(self, capacity: int):
        assert capacity > 0
        self.arr = [None] * capacity  # usamos None para indicar vazio
        self.size = 0                   # número de elementos
        self.capacity = capacity

    def get(self, i: int) -> int:
        # i é garantido válido pelo problema
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # assume não vazio
        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None  # opcional, limpa
        self.size -= 1
        return val

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_arr = [None] * new_capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity