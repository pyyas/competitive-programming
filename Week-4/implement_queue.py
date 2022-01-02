class MyQueue:

    def __init__(self):
        self._data = []
        

    def push(self, x: int) -> None:
        self._data.append(x)
        

    def pop(self) -> int:
        return self._data.pop(0)
        

    def peek(self) -> int:
        return self._data[0]
        

    def empty(self) -> bool:
        if len(self._data) == 0:
            return True
        return False
