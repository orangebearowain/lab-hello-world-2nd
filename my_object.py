from dataclasses import dataclass, field

@dataclass
class pizza:
    name: str
    size: int = 10
    topping: str = "Cheese"
    slice_left: int = 6

    def big(self, sizes: int):
        self.size = sizes
    
    def items(self, new_topping: str):
        self.topping = new_topping
        
    def left(self, remains: int):
        self.slice_left = remains
    
    
    def status(self):
        return f"{self.name}: \n Toppings: {self.topping}, \n Size: {self.size} inches, \n Slices left: {self.slice_left}"

if __name__ == "__main__":
    pineapple_pizza = pizza(name="Pineapple pizza", size=16, topping="Pineapple", slice_left=4)
    extra_cheese_pizza = pizza(name="Extra cheese pizza", size=12, topping="Extra cheese", slice_left=6)
    
    
    print(pineapple_pizza.status()) 
    print(extra_cheese_pizza.status())  