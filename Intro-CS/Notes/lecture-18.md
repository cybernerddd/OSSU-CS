# OSSU CS - MIT 6.0001 -- Lecture 19: Inheritance

**Status:** ✅ Completed

---

# What I Learned

Inheritance allows one class (the child/subclass) to reuse the attributes and methods of another class (the parent/superclass).

Instead of rewriting common code, subclasses inherit functionality and can extend or modify behavior.

Example:

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()
```

Output:

```
Some sound
```

---

# Parent vs Child Classes

Parent (Superclass)
- Defines common attributes and methods.

Child (Subclass)
- Inherits everything from the parent.
- Can add new attributes and methods.
- Can override inherited methods.

---

# Using `super()`

`super()` allows a subclass to call methods from its parent class.

Example:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

This initializes the parent class without rewriting its code.

---

# Method Overriding

A child class can replace a parent's implementation.

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")
```

Calling:

```python
dog.speak()
```

prints:

```
Woof!
```

instead of the parent's method.

---

# The `isinstance()` Function

Checks if an object belongs to a class.

```python
isinstance(dog, Dog)
```

Returns:

```
True
```

It also returns `True` for parent classes:

```python
isinstance(dog, Animal)
```

because `Dog` inherits from `Animal`.

---

# Why Inheritance Matters

Instead of duplicating code:

```
Car
Bike
Truck
Motorcycle
```

can all inherit from:

```
Vehicle
```

Common functionality is written once and reused everywhere.

Benefits:

- Less duplicated code
- Easier maintenance
- Better organization
- Cleaner object-oriented design

---

## Finger Exercises:
```python
class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self.myList = []

    def size(self):
        """
        Returns the length of the container list
        """
        # Your code here
        return len(self.myList)

    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
        # Your code here
        self.myList.append(elem)

class Stack(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The newest element in the container list is removed
        Returns the element removed or None if the queue contains no elements
        """
        # Your code here
        if self.size() > 0:
            return self.myList.pop()
        return None
```

---

# Key Concepts Learned

- Inheritance
- Parent (Superclass)
- Child (Subclass)
- `super()`
- Method overriding
- `isinstance()`
- Code reuse
- Extending existing classes

---

# Takeaway

Inheritance is about building on existing classes rather than starting from scratch. A subclass automatically gains the behavior of its parent while still being able to customize or extend it.

This makes Python programs easier to scale and maintain as projects grow.
