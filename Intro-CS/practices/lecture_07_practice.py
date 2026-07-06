#################
## EXAMPLE: simple Coordinate class
#################
class Coordinate(object):
    """ A coordinate made up of an x and y value """
    def __init__(self, x, y):
        """ Sets the x and y values """ 
        self.x = x
        self.y = y

# c = Coordinate(3,4)
# a = 0
# origin = Coordinate(a,a)
# print(c.x)
# print(origin.x)


class Coordinate(object):
    """ A coordinate made up of an x and y numerical value """
    def __init__(self, x, y):
        """ Sets the x and y values """
        self.x = x
        self.y = y
    def getX(self):
        """ Returns how far away self is on the x axis """
        return self.x
    def getY(self):
        """ Returns how far away self is on the y axis """
        return self.y
    def distance(self, other):
        """ Returns the euclidean distance between two Coordinate objects """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

c = Coordinate(3,4)
a = 0
origin = Coordinate(a,a)

# these 3 calls returns the same thing
# print(c.distance(origin))
#print(Coordinate.distance(c, origin))
#print(origin.distance(c))


###########################################################
################ AT HOME #####################
###########################################################
# Question 1:
# Write a class definition for a vehicle. A vehicle is defined by attributes:
# Number of wheels
# Number of occupants
# Color 
# Decide the type of each data attribute and document this
class Vehicle(object):
    def __init__(self, wheels, occupants, color):
        self.wheels = wheels
        self.occupants = occupants
        self.color = color
    
    
    
# Question 2:
# Create 2 vehicle instances using the class we wrote previously. 
# One red vehicle with 2 wheels, and 1 occupant
# One green vehicle with 18 wheels, and 3 occupants
# Print the first one's number of occupants
# Print the second one's color


red_vehicle = Vehicle(2, 1, "red")
green_vehicle = Vehicle(18, 3, "green")

# print(red_vehicle.occupants)
# print(green_vehicle.color)

# Question 3:
# Add on to the code from above for class Vehicle.
# Create another method for the vehicle class named add_n_occupants, 
# which takes in an int n. When called, self's number of occupants 
# increases by n. It returns the total occupants after the increase. 

class Vehicle(object):
    def __init__(self, w, o, c="black", max_occupancy=5):
        self.wheels = w
        self.occ = o
        self.color= c
        self.max_occupancy = max_occupancy
    # add method add_n_occupants here
    def add_n_occupants(self, n):
        total = 0 
        if (self.occ + n) > self.max_occupancy:
            raise ValueError("Occupants number exceeds max")
        else:
            total = self.occ + n 
        return total
        
v1 = Vehicle(4,2)
print(v1.occ)   # prints 2
print(v1.add_n_occupants(3))   # prints 5
print(v1.occ)
print(v1.color)

# Question 4:
# Add another data attribute to the Vehicle class, called max_occupancy,
# which is always 5. This attribute is not passed in as a parameter, but 
# is defined in the init.
# Modify the add_n_occupants methods such that if adding the occupants 
# exceeds the max_occupancy allowed for that vehicle, 
#   * you do not perform the increase, and
#   * you raise a ValueError with an apprpriate message

#Question 5:
# Modify the Vehicle class __init__ such that if a vehicle is created
# without specifying a color then the color is set to "black".
# Hint: remember default parameters?
