from typing import Any


class Stack:
    def __init__(self) -> None:
        self.lst = []
    
    def push(self, element: Any) -> None:
        self.lst.append(element)
    
    def pop(self) -> Any:
        old = self.lst[-1]
        del self.lst[-1]
        return old
    
    def empty(self) -> bool:
        return len(self.lst) == 0
    
    def top(self) -> Any:
        return self.lst[-1]
    
    def size(self) -> int:
        return len(self.lst)
