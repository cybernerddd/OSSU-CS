# Day 15 - Recursion

## What I Learned

Today I learned one of the most important programming concepts so far: **recursion**.
Instead of solving a problem using loops, recursion solves a problem by calling the same function on a smaller version of the problem until it reaches a simple case that can be solved directly.

---

# What is Recursion?

Recursion is a programming technique where a function calls itself.

Every recursive function has two essential parts:

1. Base Case
2. Recursive Case

Without a base case, recursion never stops and eventually causes a RecursionError.

---

## Base Case

The base case is the stopping condition.

Example:

```python
def fact(n):
    if n == 1:
        return 1
```

When the function reaches this condition, recursion ends.

---

## Recursive Case

The recursive case reduces the problem into a smaller version of itself.

Example:

```python
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
```

Instead of solving the whole problem immediately, it asks a smaller version of itself to solve part of the work.

---

# Recursive Multiplication

Instead of using the `*` operator:

```python
5 * 4
```

Think of multiplication as repeated addition.

```
5 * 4
= 5 + (5 * 3)
= 5 + (5 + (5 * 2))
= 5 + (5 + (5 + (5 * 1)))
```

Python implementation:

```python
def mult_recur(a, b):
    if b == 1:
        return a
    return a + mult_recur(a, b - 1)
```

---

# Factorial Using Recursion

Mathematically:

```
5!
= 5 × 4 × 3 × 2 × 1
```

Recursive definition:

```
n! = n × (n - 1)!
```

Python:

```python
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
```

---

# How Recursion Works

Calling:

```python
fact(4)
```

creates this chain:

```
fact(4)
↓
fact(3)
↓
fact(2)
↓
fact(1)
```

Once the base case is reached:

```
fact(1)
returns 1
```

Then the results are built back up:

```
fact(2)
2 × 1 = 2

fact(3)
3 × 2 = 6

fact(4)
4 × 6 = 24
```

This helped me understand that earlier function calls wait until later calls return their values.

---

# Recursive Function Scope

Every recursive function call has its own independent scope.

Example:

```
fact(4)
fact(3)
fact(2)
fact(1)
```

Each call has its own variable `n`.

They do not share variables with each other.

Each function call is completely independent.

---

# Iteration vs Recursion

Iteration:

```python
for
while
```

Recursion:

```python
function()
    function()
        function()
```

Iteration usually uses less memory.

Recursion often produces simpler and cleaner solutions for naturally recursive problems.

---

# When Should Recursion Be Used?

Good use cases:

- Factorials
- Mathematical definitions
- Tree traversal
- File system traversal
- Divide-and-conquer algorithms

Not every problem should be solved recursively.

If a loop is simpler, a loop is usually the better choice.

---

# Key Takeaways

- Recursion is when a function calls itself.
- Every recursive function needs a base case.
- The recursive case should make the problem smaller.
- Every recursive call has its own scope.
- Earlier function calls wait until later calls return.
- Infinite recursion happens when no base case is reached.
- Recursion can produce elegant solutions but uses more memory than iteration.

---

# Reflection

Recursion felt strange at first because the function appears to call itself over and over.

After tracing examples like multiplication and factorial step by step, I understood that each function call simply waits for the next one to finish before continuing.

The biggest lesson from today is that recursion is not magic—it is just a function solving a smaller version of the same problem until it reaches a stopping condition.
