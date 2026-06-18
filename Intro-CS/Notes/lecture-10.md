# Day 10 - Lists, Mutability & Higher-Order Functions

## What I Learned

Today I learned about Python lists and how they differ from tuples.

Unlike tuples, lists are mutable, meaning their contents can be changed after creation.

```python
L = [1, 2, 3]
L[0] = 100

print(L)
# [100, 2, 3]
```

---

## Lists vs Tuples

### Tuple (Immutable)

```python
t = (1, 2, 3)
```

Cannot modify elements after creation.

### List (Mutable)

```python
L = [1, 2, 3]
```

Can add, remove, or modify elements.

---

## Common List Operations

### Append

```python
L = [1, 2]
L.append(3)

# [1, 2, 3]
```

Adds an item to the end of the list.

### Remove

```python
L.remove(2)

# [1, 3]
```

Removes the first occurrence of an item.

### Delete

```python
del L[0]
```

Deletes an item by index.

---

## Iterating Through Lists

```python
numbers = [1, 2, 3, 4]

for num in numbers:
    print(num)
```

Output:

```text
1
2
3
4
```

---

## Aliasing

One of the most important concepts from this lecture.

```python
a = [1, 2, 3]
b = a

b[0] = 100

print(a)
```

Output:

```text
[100, 2, 3]
```

Why?

Because both variables point to the same list in memory.

---

## Cloning Lists

To create an independent copy:

```python
a = [1, 2, 3]
b = a[:]

b[0] = 100

print(a)
```

Output:

```text
[1, 2, 3]
```

Using slicing creates a new list.

---

## Functions as Parameters

Functions can be passed into other functions.

Example:

```python
def add_one(x):
    return x + 1

def apply_twice(f, x):
    return f(f(x))
```

Calling:

```python
apply_twice(add_one, 5)
```

Produces:

```text
7
```

---

## Practice Exercises Completed

### contains_char()

Checks whether a character exists in a string.

### apply_twice()

Applies a function twice to a value.

### biggest_result()

Finds the largest result produced by a function between 0 and n.

### apply_all()

Applies multiple functions to numbers from 0 to n and returns the maximum result.

### all_true()

Checks whether all functions in a list return True for a given value.

## FINGER EXERCISES
**Question 1: Implement the function that meets the specifications below:**
```python
def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    # Your code here
    for func in Lf:     
        if not func(n):
            return False
    
    return True   


# Examples:
def positive(x):
    return x > 0

def even(x):
    return x % 2 == 0

def less_than_100(x):
    return x < 100

Lf = [positive, even, less_than_100]
# print(all_true(7, Lf))

# print(all_true(4, [lambda x: x > 0, lambda x: x % 3 == 0]))
```

---

## Key Takeaways

- Lists are mutable.
- Tuples are immutable.
- Aliasing can cause unexpected changes.
- Cloning creates independent copies.
- Functions can be passed as arguments.
- Higher-order functions allow powerful and reusable code.

## Reflection

This lecture was challenging at first because functions were being passed into other functions. After practicing exercises like `apply_twice`, `apply_all`, and `all_true`, I started understanding how Python treats functions as objects that can be stored, passed around, and called dynamically.

Definitely one of the more interesting lectures so far.
