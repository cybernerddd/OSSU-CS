# Lecture 21 — Timing Programs & Counting Operations

## What I Learned

This lecture introduced the idea of **program efficiency**.

Until now, the focus has been writing **correct programs**. Now the goal is to write programs that are also **efficient**.

Correctness comes first.

Efficiency comes second.

---

# Why Efficiency Matters

Small programs work fine.

Large datasets can make inefficient code extremely slow.

Different algorithms can solve the same problem while taking drastically different amounts of time.

---

# Measuring Performance

There are three common ways to evaluate a program:

- Timing the program
- Counting operations
- Order of Growth (Big-O)

---

# Timing Programs

Python's `time` module can be used to measure execution time.

Example:

```python
import time

start = time.time()

# code

elapsed = time.time() - start
```

Timing works well for large programs but has drawbacks.

It depends on:

- Computer speed
- Operating system
- Background processes
- Programming language
- Hardware

Because of this, timing is **not** the best way to compare algorithms.

---

# Counting Operations

Instead of measuring seconds, we count how many basic operations execute.

Assume these all take constant time:

- Assignment
- Comparison
- Arithmetic
- Memory access

Examples:

### Constant work

```python
def c_to_f(c):
    return c * 9 / 5 + 32
```

Always performs the same number of operations.

---

### Linear work

```python
for i in range(n):
```

Runs `n` times.

Operations grow proportionally with input size.

---

### Nested loops

```python
for i in range(n):
    for j in range(n):
```

Runs approximately `n²` times.

Doubling the input roughly quadruples the work.

---

# Examples

## No loop

```python
def no_loop(n):
    print(n)
```

Operations stay constant.

Growth:

```
O(1)
```

---

## One loop

```python
def one_loop(n):
    for i in range(n):
        print(i)
```

Operations increase linearly.

Growth:

```
O(n)
```

---

## Nested loops

```python
def two_nest(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
```

Operations grow quadratically.

Growth:

```
O(n²)
```

---

# Key Takeaways

- Correct code comes before efficient code.
- Timing depends on the machine.
- Counting operations compares algorithms more fairly.
- Nested loops grow much faster than single loops.
- As input size increases, inefficient algorithms become expensive.

---

# Progress

- ✅ Learned how to time programs.
- ✅ Learned why timing isn't always reliable.
- ✅ Learned how to count operations.
- ✅ Learned constant, linear, and quadratic growth.
- ✅ Prepared for learning Big-O notation.
