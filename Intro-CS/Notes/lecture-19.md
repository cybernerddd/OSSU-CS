# Lecture 20 — Object-Oriented Programming Example (Fitness Tracker)

## What I Learned

Lecture 20 focused on building a real-world application using Object-Oriented Programming.

Instead of learning new syntax, the lecture showed how classes are designed in larger programs and why OOP is useful.

---

# Designing Classes

When creating a class, think about two things:

## Data Attributes (What the object IS)

These store information.

Example:

- start time
- end time
- calories
- workout type
- icon

```python
class Workout:
    def __init__(self, start, end, calories):
        self.start = start
        self.end = end
        self.calories = calories
```

---

## Methods (What the object DOES)

Methods define behavior.

Examples:

```python
get_calories()
set_calories()
get_start()
set_start()
```

---

# Getters and Setters

Instead of directly accessing:

```python
workout.calories
```

Use

```python
workout.get_calories()
```

Instead of

```python
workout.calories = 500
```

Use

```python
workout.set_calories(500)
```

This hides implementation details and makes code easier to maintain.

---

# Information Hiding

Users of a class shouldn't need to know how the class works internally.

Only expose methods.

This allows the implementation to change without breaking code.

---

# Class Variables

A class variable belongs to the class itself.

Example

```python
class Workout:
    cal_per_hr = 200
```

Every Workout object shares this value.

Access it using

```python
Workout.cal_per_hr
```

Changing it changes it for every instance.

---

# Datetime Objects

Instead of storing dates as strings, convert them into datetime objects.

```python
from dateutil import parser

start = parser.parse("9/30/2021 1:35 PM")
```

This allows easy calculations.

Example

```python
duration = end - start
duration.total_seconds()
```

---

# Estimating Calories

If calories are not provided:

```python
calories = hours * Workout.cal_per_hr
```

The object can calculate them automatically.

---

# Inheritance Review

Created

```python
class RunWorkout(Workout)
```

RunWorkout inherits everything from Workout.

It adds

- elevation
- running icon
- running type

```python
super().__init__(start, end, calories)
```

initializes everything from the parent class.

---

# Overriding Methods

A child class can replace a parent's method.

Example

Parent:

```python
get_calories()
```

Child:

```python
get_calories()
```

If GPS data exists:

calculate calories from distance.

Otherwise:

```python
return super().get_calories()
```

---

# super()

Calls the parent version.

Example

```python
super().__init__()
```

or

```python
super().get_calories()
```

Useful when extending instead of replacing functionality.

---

# Method Resolution

When Python sees

```python
rw.get_calories()
```

It searches:

1. RunWorkout
2. Workout
3. object

and uses the first version it finds.

---

# Reusing Parent Code

One print function can work for every subclass.

Example

```python
Workout
RunWorkout
SwimWorkout
```

All can use the same

```python
__str__()
```

without rewriting it.

---

# Parent vs Child Objects

A subclass can be used wherever a parent is expected.

Example

```python
Workout list

[
    Workout(),
    RunWorkout(),
    SwimWorkout()
]
```

This works because every subclass IS a Workout.

But a Workout is NOT always a RunWorkout.

---

# Equality with Subclasses

Parent compares

- start
- end
- calories

Child compares

- everything in parent
- elevation

```python
return super().__eq__(other) and self.elev == other.elev
```

## Finger Exercise:
```
Finger Exercise Lecture 20
In this problem, you will implement two classes according to the specification below: one Container class and one Queue class (a subclass of Container).     

Our Container class will initialize an empty list. The two methods we will have are to calculate the size of the list and to add an element. The second method will be inherited by the subclass. We now want to create a subclass so that we can add more functionality – the ability to remove elements from the list. A Queue will add elements to the list in the same way, but will behave differently when removing an element.

A queue is a first-in, first-out data structure. Think of a store checkout queue. The customer who has been in the line the longest gets the next available cashier. When implementing your Queue class, you will have to think about which end of your list contains the element that has been in the list the longest. This is the element you will want to remove and return.
```
### CODE
```
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

class Queue(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The oldest element in the container list is removed
        Returns the element removed or None if the stack contains no elements
        """
        # Your code here
        if self.size() == 0:
            return None

        return self.myList.pop(0)
```
---

# Biggest Lessons

- Real OOP is about designing software.
- Use getters/setters to hide implementation.
- Class variables are shared by every object.
- Datetime objects make date calculations simple.
- Inheritance avoids duplicate code.
- Child classes can extend or override parent behavior.
- super() allows child classes to reuse parent functionality.
- Python searches methods from child → parent → object.
