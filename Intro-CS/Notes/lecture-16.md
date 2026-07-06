# MIT 6.100L - Lecture 16: Python Classes

## Topics Covered

* Introduction to Object-Oriented Programming (OOP)
* Classes and Objects
* Creating Instances
* Constructors (`__init__`)
* Understanding `self`
* Instance Attributes
* Instance Methods
* Dot Notation
* Default Parameters

## Key Concepts

### Class

A **class** is a blueprint used to create objects.

```python
class Vehicle:
    pass
```

---

### Object (Instance)

An object is an instance created from a class.

```python
car = Vehicle()
```

---

### Constructor (`__init__`)

The constructor runs automatically whenever a new object is created.

```python
class Vehicle:
    def __init__(self, wheels, occupants, color):
        self.wheels = wheels
        self.occupants = occupants
        self.color = color
```

---

### `self`

`self` refers to the current object being created or used.

```python
self.color = color
```

stores the object's color.

---

### Attributes

Attributes store data about an object.

Example:

* wheels
* occupants
* color

Access them using dot notation:

```python
car.color
car.wheels
```

---

### Methods

Methods are functions that belong to a class.

```python
def add_n_occupants(self, n):
    self.occupants += n
```

Methods can access and modify the object's attributes through `self`.

---

### Default Parameters

Constructors can provide default values.

```python
def __init__(self, wheels, occupants, color="black"):
```

If no color is provided, `"black"` is used automatically.

---

### Raising Exceptions

Use exceptions to prevent invalid object states.

```python
if self.occupants + n > self.max_occupancy:
    raise ValueError("Maximum occupancy exceeded.")
```

---

## Practice

Implemented a `Vehicle` class supporting:

* Creating vehicle objects
* Default colors
* Maximum occupancy
* Occupancy validation
* Object attributes
* Instance methods

---

## Finger Exercise
```python
class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        # your code here
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        # your code here
        return self.radius


    def set_radius(self, radius):
        """ radius is a number
        Changes the radius of self to radius """
        # your code here
        self.radius = radius    

    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        # your code here
        pi = 3.14
        return pi * (self.radius ** 2)

    def equal(self, c):
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        # your code here
        return c.get_radius() == self.radius

    def bigger(self, c):
        if self.radius >= c.get_radius():
            return self
        else:
            return c
```

## Key Takeaways

* A class is a blueprint.
* An object is an instance of a class.
* `__init__()` initializes new objects.
* `self` represents the current object.
* Attributes store data.
* Methods define behavior.
* Objects combine data and behavior into reusable components.

---

**Course:** MIT 6.100L – Introduction to Computer Science and Programming Using Python
**Lecture:** 17 – Python Classes
