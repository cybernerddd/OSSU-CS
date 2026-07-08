# MIT 6.100L – Lecture 18 Notes

## Python Classes II – Dunder (Magic) Methods

### What are Dunder Methods?

Dunder ("double underscore") methods are special methods that Python automatically calls when using built-in operations.

Examples:

* `__init__()` → object creation
* `__str__()` → `print(object)`
* `__add__()` → `+`
* `__sub__()` → `-`
* `__mul__()` → `*`
* `__truediv__()` → `/`
* `__eq__()` → `==`
* `__lt__()` → `<`
* `__len__()` → `len(object)`
* `__float__()` → `float(object)`
* `__pow__()` → `**`

These methods allow custom classes to behave like Python's built-in types.

---

## Why Dunder Methods?

Without dunder methods:

```python
fraction1.times(fraction2)
```

With dunder methods:

```python
fraction1 * fraction2
```

The second version is much cleaner and more Pythonic.

---

## The `__str__()` Method

By default, printing an object gives something like:

```text
<__main__.Coordinate object at 0x...>
```

Implementing `__str__()` lets us control what is displayed.

Example:

```python
def __str__(self):
    return f"<{self.x}, {self.y}>"
```

Now:

```python
print(coord)
```

outputs:

```text
<3,4>
```

instead of the default object address.

---

## Operator Overloading

Python operators are actually method calls.

Example:

```python
a * b
```

is equivalent to:

```python
a.__mul__(b)
```

or even:

```python
Fraction.__mul__(a, b)
```

Python hides these method calls behind familiar operators, making code easier to read.

---

## Returning Objects

Instead of returning primitive values, methods can return entirely new objects.

Example:

```python
def __mul__(self, other):
    top = self.num * other.num
    bottom = self.denom * other.denom
    return Fraction(top, bottom)
```

Multiplying two Fraction objects produces another Fraction object.

---

## Casting Objects

Implementing:

```python
def __float__(self):
```

allows:

```python
float(fraction)
```

to automatically convert a Fraction into a decimal value.

---

## Reducing Fractions

A `reduce()` method simplifies fractions using the Greatest Common Divisor (GCD).

Example:

```text
2/12
```

becomes

```text
1/6
```

---

## Type Consistency

Methods should consistently return the same type whenever possible.

Instead of returning an integer for `5/1`, it is better to return:

```text
5/1
```

as a Fraction object so all Fraction methods continue to work.

---

## Finger Exercises
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

    def __add__(self, c):
        """ c is a Circle object 
        Returns a new Circle object whose radius is 
        the sum of self and c's radius """
        # your code here
        return Circle(self.radius + c.radius)

    def __str__(self):
        """ A Circle's string representation is the radius """
        # your code here
        return "Your radius is " + str(self.radius)
```

## Key Takeaways

* Dunder methods allow custom classes to integrate with Python syntax.
* Operators like `+`, `*`, `print()`, and `len()` are implemented as methods.
* `__str__()` controls object printing.
* `__float__()` enables object casting.
* Methods can return new objects.
* Keeping return types consistent makes classes easier to use and maintain.
* Object-oriented programming improves abstraction, organization, and code reuse.
