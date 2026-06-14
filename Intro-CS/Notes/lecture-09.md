# OSSU CS - Day 9

## Lecture 9: Lambda Functions, Tuples, and Lists

---

## Lambda Functions

A lambda function is a small anonymous function that can be written in one line.

Example:

```python

square = lambda x: x**2

print(square(4))

```

Output:

```text

16

```

Lambda functions are useful when a simple function is needed only once.  [oai_citation:1‡mit6_100l_f22_lec09.pdf](sediment://file_000000006cd072438ca6f110ee9506af)

---

## Functions as Arguments

Functions can be passed into other functions.

Example:

```python

def do_twice(n, fn):

    return fn(fn(n))

print(do_twice(3, lambda x: x**2))

```

Step-by-step:

```text

3² = 9

9² = 81

```

Output:

```text

81

```

 [oai_citation:2‡mit6_100l_f22_lec09.pdf](sediment://file_000000006cd072438ca6f110ee9506af)

---

## Tuples

A tuple is an ordered sequence of objects.

Syntax:

```python

t = (2, "mit", 3)

```

Properties:

- Ordered

- Indexable

- Sliceable

- Immutable (cannot be changed)

Examples:

```python

t[0]

```

Output:

```text

2

```

```python

len(t)

```

Output:

```text

3

```

```python

t[1] = 4

```

Output:

```text

Error

```

Tuples cannot be modified after creation.  [oai_citation:3‡mit6_100l_f22_lec09.pdf](sediment://file_000000006cd072438ca6f110ee9506af)

---

## Tuple Indexing and Slicing

Example:

```python

seq = (2, 'a', 4, (1, 2))

```

Examples:

```python

seq[1]

```

Output:

```text

'a'

```

```python

seq[-1]

```

Output:

```text

(1, 2)

```

```python

seq[3][0]

```

Output:

```text

1

```

 [oai_citation:4‡mit6_100l_f22_lec09.pdf](sediment://file_000000006cd072438ca6f110ee9506af)

---

## Swapping Variables with Tuples

Traditional approach:

```python

temp = x

x = y

y = temp

```

Python shortcut:

```python

(x, y) = (y, x)

```

 [oai_citation:5‡mit6_100l_f22_lec09.pdf](sediment://file_000000006cd072438ca6f110ee9506af)

---

## Returning Multiple Values

Functions can return multiple values using a tuple.

Example:

```python

def quotient_and_remainder(x, y):

    q = x // y

    r = x % y

    return (q, r)

```

Usage:

```python

quot, rem = quotient_and_remainder(5, 2)

```

The function returns one tuple containing multiple values.  [oai_citation:6‡mit6_100l_f22_lec09.pdf](sediment://file_000000006cd072438ca6f110ee9506af)

---

## Variable Number of Arguments

Python allows functions to accept any number of arguments using `*args`.

Example:

```python

def mean(*args):

    total = 0

    for num in args:

        total += num

    return total / len(args)

```

Usage:

```python

print(mean(1, 2, 3, 4, 5))

```

 [oai_citation:7‡mit6_100l_f22_lec09.pdf](sediment://file_000000006cd072438ca6f110ee9506af)

---

## Lists

A list is an ordered collection of objects.

Syntax:

```python

L = [2, 'a', 4]

```

Properties:

- Ordered

- Indexable

- Sliceable

- Mutable (can be modified)

Unlike tuples, list elements can be changed.  [oai_citation:8‡mit6_100l_f22_lec09.pdf](sediment://file_000000006cd072438ca6f110ee9506af)

---

## List Examples

```python

L = [2, 'a', 4, [1, 2]]

```

Examples:

```python

L[0]

```

Output:

```text

2

```

```python

L[3]

```

Output:

```text

[1, 2]

```

```python

len(L)

```

Output:

```text

4

```

 [oai_citation:9‡mit6_100l_f22_lec09.pdf](sediment://file_000000006cd072438ca6f110ee9506af)

---

## Iterating Through Lists

Method 1:

```python

for i in range(len(L)):

    print(L[i])

```

Method 2 (preferred):

```python

for item in L:

    print(item)

```

Both iterate through all elements of the list.  [oai_citation:10‡mit6_100l_f22_lec09.pdf](sediment://file_000000006cd072438ca6f110ee9506af)

---

## Summing Elements in a List

```python

def list_sum(L):

    total = 0

    for item in L:

        total += item

    return total

```

Example:

```python

list_sum([1, 3, 5])

```

Output:

```text

9

```

 [oai_citation:11‡mit6_100l_f22_lec09.pdf](sediment://file_000000006cd072438ca6f110ee9506af)

---

## Key Takeaways

- Lambda functions are short anonymous functions.

- Functions can be passed as arguments.

- Tuples use `()` and are immutable.

- Lists use `[]` and are mutable.

- Tuples and lists support indexing and slicing.

- Tuples can be used to return multiple values.

- Lists are commonly used for storing collections of data.

- Lists and tuples can both be iterated with `for` loops.

---

## Personal Notes

The biggest lesson today was understanding the difference between tuples and lists:

```python

(1, 2, 3)   # Tuple

[1, 2, 3]   # List

```

Tuples cannot be changed after creation.

Lists can be modified, making them useful when data needs to change during program execution.