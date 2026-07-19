class CoffeeMachine(object):
    """
    a CoffeeMachine resources tracker
    class, checks whether there are 
    sufficient resources to make latte.
    """
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk
    def make_latte(self):
        """
        make your sweet latte 
        """
        # setting the needed resource values to make latte.
        # A latte requires:
        w = 200                  # water ml
        c = 20                   # coffee 20g
        m = 150                  # milk 150ml
        if (self.milk >= m) and (self.coffee >= c) and (self.water >= w):
            self.milk -= m
            self.coffee -= c
            self.water -= w
            print(f"Latte made! Remaining - Water: {self.water}ml, Coffee: {self.coffee}g, Milk: {self.milk}ml")
        else:
            print("Not enough resources to make a latte.")

person1 = CoffeeMachine(water=3000, coffee=100, milk=200)
person1.make_latte()
