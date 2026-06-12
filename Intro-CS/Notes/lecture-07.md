# OSSU CS - Day 08

## MIT 6.100L Lecture 7: Decomposition, Abstraction, and Functions

## Core Ideas

This lecture introduced functions and showed how programmers solve larger problems by breaking them into smaller pieces.

---

## Decomposition

Decomposition means breaking a large problem into smaller, manageable parts.

Instead of solving everything at once:

```python

# huge messy program

```

Break it into pieces:

```python

login()

calculate_total()

generate_report()

```

Each piece focuses on a single task.

### Benefits

- Easier to understand

- Easier to debug

- Easier to maintain

- Easier to reuse

---

## Abstraction

Abstraction means focusing on what something does instead of how it works internally.

Example:

```python

print("Hello")

```

I know what `print()` does.

I do not need to know how Python implemented it internally.

Functions act like black boxes.

Input goes in.

Output comes out.

---

## Function Structure

Basic syntax:

```python

def function_name():

    # code

```

Example:

```python

def greet():

    print("Hello")

```

Calling the function:

```python

greet()

```

Output:

```text

Hello

```

---

## Parameters

Functions can accept inputs called parameters.

Example:

```python

def greet(name):

    print("Hello", name)

```

Usage:

```python

greet("Cybernerddd")

```

Output:

```text

Hello Cybernerddd

```

---

## Return Values

Functions can send a value back using `return`.

Example:

```python

def square(x):

    return x * x

```

Usage:

```python

result = square(4)

print(result)

```

Output:

```text

16

```

---

## Problem Solving Process

MIT emphasized:

### 1. Understand the problem

Identify:

- Inputs

- Outputs

Example:

```python

def sum_odd(a, b):

```

Input:

```text

a, b

```

Output:

```text

sum of odd numbers between a and b

```

---

### 2. Use simple test cases

Example:

```text

a = 2

b = 4

```

Expected result:

```text

3

```

---

### 3. Solve a simpler problem first

Before summing odd numbers:

Solve:

```text

Sum ALL numbers first.

```

Then add the odd-number logic later.

---

### 4. Test frequently

Use:

```python

print()

```

to inspect variables and program flow.

Example:

```python

print(i, sum_of_odds)

```

This helps reveal bugs.

---

## Debugging

MIT's debugging strategy:

1. Run small tests.

2. Add print statements.

3. Observe variable values.

4. Fix the issue.

5. Test again.

---

## Key Takeaways

- Functions package logic into reusable blocks.

- Functions support decomposition and abstraction.

- A function only runs when called.

- Parameters provide input to functions.

- Return values provide output from functions.

- Start with a simple version of the problem.

- Test code often.

- Use print statements for debugging.

- Don't rush into coding before understanding the problem.

---

## Memorable Lesson

> Don't write code right away.

Think first.

Solve on paper.

Then code the solution.