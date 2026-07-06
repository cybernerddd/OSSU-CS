class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # find area

    def area(self):
        return self.width * self.height
    
    # find perimeter

    def perimeter(self):
        """
        permeter = 2(l+w),

        """
        return 2 * (self.width + self.height)
    
    # find if the sides are equal

    def is_square(self):
        """
        returns a Bool, 
        if sides are equal or not
        """
        return self.width == self.height
    

# example
# Create a rectangle with width=10, height=5
rect1 = Rectangle(10, 5)

print("Area:", rect1.area())          # 50
print("Perimeter:", rect1.perimeter()) # 30
print("Is square?:", rect1.is_square()) # False
