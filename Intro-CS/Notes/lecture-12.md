# Day 12 - Testing and Debugging

## What I Learned

Today I learned that writing code is only half the job.

The other half is making sure the code actually works.

This lecture introduced testing and debugging, two essential skills every programmer needs.

---

## Testing

Testing is the process of checking whether a program behaves as expected.

The goal is to discover bugs before users do.

A bug is an error in a program that causes incorrect behavior.

---

## Black Box Testing

Black box testing focuses on the specification of the program rather than the code itself.

The tester does not look at the implementation.

Instead, they ask:

"What inputs should this program handle?"

Example:

```python
def sqrt(x, eps):
```

Possible test cases:

- x = 0
- Perfect squares
- Numbers less than 1
- Irrational square roots
- Very large numbers
- Very small numbers

The idea is to test different categories of input and important boundary conditions.

---

## Boundary Cases

Boundary cases are values at the edges of expected input.

Examples:

```python
[]
```

Empty list

```python
[5]
```

Single-element list

```python
0
```

Smallest valid number

Testing boundaries often reveals hidden bugs.

---

## Glass Box Testing

Glass box testing looks directly at the code.

Instead of testing the specification, we test program paths.

Questions include:

- Did every branch execute?
- Did every loop run?
- Did every condition get tested?

Example:

```python
if x > 0:
    ...
else:
    ...
```

Both branches should be tested.

---

## Path Testing

A path-complete test suite attempts to execute every possible path through the code.

However, even path-complete testing can miss bugs.

Example:

```python
def abs(x):
    if x < -1:
        return -x
    else:
        return x
```

Testing:

```python
abs(2)
abs(-2)
```

covers both paths.

But:

```python
abs(-1)
```

reveals a bug.

This shows why boundary testing is important.

---

## Debugging

Debugging is the process of finding and fixing bugs.

Typical process:

1. Identify the bug
2. Isolate the bug
3. Fix the bug
4. Retest

Repeat until the program behaves correctly.

---

## Common Python Errors

### IndexError

```python
L = [1,2,3]
print(L[4])
```

Trying to access an index that does not exist.

---

### TypeError

```python
"3" / 4
```

Using incompatible types together.

---

### NameError

```python
print(x)
```

Variable does not exist.

---

### SyntaxError

```python
print("hello"
```

Missing closing bracket or quote.

---

## Logic Errors

The hardest bugs.

The program runs successfully but produces incorrect output.

Example:

```python
def add(a, b):
    return a - b
```

No crash.

Wrong answer.

These bugs require careful thinking and testing.

---

## Debugging Strategies

### Use Print Statements

Print useful information:

```python
print("x =", x)
```

Helpful places to print:

- Function entry
- Function parameters
- Loop variables
- Function results

---

### Use the Scientific Method

1. Observe the problem
2. Form a hypothesis
3. Test the hypothesis
4. Repeat

---

### Simplify Inputs

When debugging:

Use the smallest possible input that reproduces the bug.

Simple inputs are easier to reason about.

---

## Key Takeaways

- Testing finds bugs.
- Debugging fixes bugs.
- Black box testing focuses on specifications.
- Glass box testing focuses on code paths.
- Boundary testing is extremely important.
- Logic errors are harder than syntax errors.
- Print statements are powerful debugging tools.
- Good programmers spend a lot of time debugging.

---

## Reflection

This lecture made me realize that programming is not just about writing code.

A huge part of software development is testing assumptions, finding mistakes, and systematically debugging problems.

The biggest takeaway was that even code that runs successfully can still be wrong.

Learning how to test and debug effectively is just as important as learning syntax.
