class Inventory:
    def __init__(self, _capacity: int) -> None:
        self.items = []
        self._capacity = _capacity

    def add_item(self, item: str) -> None or str:
        if self._capacity > len(self.items):
            self.items.append(item)
        else:
            return "not enough room in the inventory"
    
    def get_capacity(self) -> int:
        return self._capacity
    
    def __repr__(self) -> str:
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self._capacity - len(self.items)}"