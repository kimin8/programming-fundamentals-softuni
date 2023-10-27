class Vehicle:
    def __init__(self, type: str, model: str, price: float) -> None:
        self.type = type
        self.model = model
        self.price = price
        self.owner = None
    
    def buy(self, money: int, owner: str) -> str:
        if money >= self.price and self.owner == None:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"
        elif money < self.price:
            return "Sorry, not enough money"
        elif self.owner != None:
            return "Car already sold"
    
    def sell(self) -> None or str:
        if self.owner != None:
            self.owner = None
        else:
            return "Vehicle has no owner"
    
    def __repr__(self) -> str:
        if self.owner != None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"