# Day 11 - Aliasing, Cloning, Shallow Copy & Deep Copy

## What I Learned

Today I learned how Python stores lists in memory and why mutable objects can sometimes behave unexpectedly.

The biggest lesson was understanding the difference between:

- Aliasing
- Cloning
- Shallow Copy
- Deep Copy

---

## Lists in Memory

A list is an object stored somewhere in memory.

Variables don't contain the list itself.

They point to the list.

Example:

```python
a = [1, 2, 3]
b = a
```

Both `a` and `b` point to the exact same list.

---

## Aliasing

```python
warm = ['red', 'yellow']
hot = warm

hot.append('orange')

print(warm)
```

Output:

```python
['red', 'yellow', 'orange']
```

Even though we changed `hot`, `warm` changed too.

Why?

Because both names point to the same list object.

This is called **aliasing**.

---

## Side Effects

A side effect occurs when modifying an object unexpectedly affects another variable.

Example:

```python
a = [1, 2, 3]
b = a

b[0] = 100

print(a)
```

Output:

```python
[100, 2, 3]
```

Changing `b` also changed `a`.

---

## Cloning a List

To create an independent copy:

```python
a = [1, 2, 3]
b = a[:]
```

Now:

```python
b[0] = 100
```

does not affect `a`.

---

## Shallow Copy

Using:

```python
import copy

new_list = copy.copy(old_list)
```

creates a new top-level list.

However, nested mutable objects are still shared.

Example:

```python
old = [[1, 2], [3, 4]]
new = copy.copy(old)

old[0][0] = 99
```

Both lists see the change because the inner lists are shared.

---

## Deep Copy

Using:

```python
import copy

new = copy.deepcopy(old)
```

creates completely independent copies of everything.

Changes to nested structures do not affect the copied version.

---

## Lists of Lists

Python allows nested lists.

Example:

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

These structures can create unexpected side effects if aliases exist.

---

## Key Takeaways

- Variables point to objects in memory.
- Assignment creates aliases.
- Lists are mutable.
- Aliases share the same object.
- Cloning creates a new list.
- Shallow copies only copy the top level.
- Deep copies copy every level.
- Mutable nested structures require extra care.

---

## Reflection

This lecture completely changed how I think about variables.

Before, I thought assigning one variable to another created a new object.

Now I understand that Python often creates another reference to the same object, which can lead to unexpected side effects when working with mutable data structures.

Understanding aliasing and copying feels like learning what's happening behind the scenes in memory.
