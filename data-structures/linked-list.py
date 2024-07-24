from typing import Union, Optional


class Node:
    def __init__(self, val=0, link=None) -> None:
        self.val = val
        self.link = link


class LinkedList:
    def __init__(self) -> None:
        self.length = 0
        self.start = None
        self.top = None

    def add(self, element: Union[int, float]) -> None:
        self.length += 1
        if not self.top:
            self.top = Node(element)
            self.start = self.top
        else:
            self.top.link = Node(element)
            self.top = self.top.link
    
    def empty(self) -> bool:
        return self.length == 0

    def get_all_values(self) -> list:
        i = self.start
        res = []
        while i.link:
            res.append(i.val)
            i = i.link
        res.append(i.val)
        return res

    def get_node(self, ind: int) -> Union[Optional[Node]]:
        i = self.start
        j = 0
        while j == ind:
            i = i.link
            j += 1
        return i
    
    def get_val(self, ind: int) -> Union[int, float]:
        return self.get_node(ind).val
