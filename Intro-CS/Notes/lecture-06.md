# OSSU CS MIT 6.100L Lecture 6: Bisection Search

## Big Idea

For many problems, finding an exact answer is difficult or impossible.

Instead of checking every possible answer one-by-one, we can use smarter algorithms to find a solution much faster.

---

## Bisection Search

Bisection Search works by repeatedly cutting the search space in half.

Example:

Suppose the answer is between:

```text
0 and 100
```

First guess:

```text
50
```

If the answer is larger:

```text
Search between 50 and 100
```

If the answer is smaller:

```text
Search between 0 and 50
```

Repeat until the answer is found or close enough.

---

## Why It Is Faster

### Guess-and-Check

Checks values one-by-one:

```text
1
2
3
4
5
...
```

Growth:

```text
Linear
```

---

### Bisection Search

Cuts possibilities in half each time:

```text
100
50
25
12
6
3
...
```

Growth:

```text
Logarithmic
```

Much more efficient.

---

## Conditions for Bisection Search

Bisection Search only works when:

### 1. The search space is ordered

Example:

```text
0, 1, 2, 3, 4, ...
```

---

### 2. We can tell whether a guess is:

```text
Too low
Too high
Correct
```

Without this feedback, bisection search cannot work.

---

## Square Root with Bisection Search

Variables:

```python
low
high
guess
epsilon
```

Initial guess:

```python
guess = (low + high) / 2
```

If:

```python
guess**2 < x
```

then:

```python
low = guess
```

Otherwise:

```python
high = guess
```

Repeat until:

```python
abs(guess**2 - x) < epsilon
```

---

## Bisection Search for Numbers Between 0 and 1

Special case:

```python
0 < x < 1
```

Example:

```python
x = 0.5
```

The square root is:

```text
Greater than x
Less than 1
```

Search interval:

```python
low = x
high = 1.0
```

---

## Newton-Raphson Method

Another root-finding algorithm.

Idea:

```text
Start with a guess.
Use a formula to generate a better guess.
Repeat.
```

Usually converges very quickly.

For now, know that it is another approximation technique.

---

## Decomposition

Break a large problem into smaller parts.

Instead of:

```python
# 500 lines in one block
```

Use:

```python
login()
calculate_score()
send_email()
```

Each part solves one problem.

---

## Abstraction

Focus on what something does, not how it works internally.

Example:

```python
print("Hello")
```

We use `print()` without knowing how Python implemented it internally.

That's abstraction.

---

## FINGER EXERCISE
> Assume you are given an integer   . Write a piece of Python code that uses bisection search to guess N. The code prints two lines: count: with how many guesses it took to find N, and answer: with the value of N. Hints: If the halfway value is exactly in between two integers, choose the smaller one.

**ANSWER:**
```py
N = 543 #assume N is 543
epsilon = 1
low = 0
high = 1000
count = 0

guess = (low + high)//2

while guess != N:
    guess = (low + high)//2 # set midpoint
    print(guess)
    count += 1
    if guess > N:
        high = guess
    else:
        low = guess
    
print(f"counted: {count}")
print(guess)
```

## Key Takeaways

- Bisection Search repeatedly cuts the search space in half.
- It is much faster than guess-and-check.
- It only works when values are ordered and feedback is available.
- Approximation algorithms often use epsilon instead of exact equality.
- Decomposition means breaking big problems into smaller ones.
- Abstraction means hiding unnecessary details.
- Good code should be easy to create, modify, maintain, and understand.
