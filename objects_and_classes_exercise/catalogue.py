class Catalogue:
    def __init__(self, name: str) -> None:
        self.name = name
        self.products = []

    def add_product(self, product_name: str) -> None:
        self.products.append(product_name)
    
    def get_by_letter(self, first_letter: str) -> list:
        return [product for product in self.products if product.startswith(first_letter)]
    
    def __repr__(self) -> str:
        returning_string = f"Items in the {self.name} catalogue:\n"
        returning_string += "\n".join(sorted(self.products))
        return returning_string