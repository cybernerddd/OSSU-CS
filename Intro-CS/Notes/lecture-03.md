# OSSU / MIT 6.100L - Lecture 3: Iteration

Iteration = repeating code.

Python provides:

- while loops

- for loops

---

## while Loops

```python

while condition:

    code

```

The loop continues while the condition is True.

Example:

```python

n = 3

while n > 0:

    print(n)

    n -= 1

```

Output:

```text

3

2

1

```

---

## Infinite Loops

Example:

```python

while True:

    print("hello")

```

The condition never becomes False.

Use Ctrl+C to stop it.

---

## Loop Variables

A variable often tracks loop progress.

Example:

```python

i = 0

while i < 5:

    print(i)

    i += 1

```

---

## for Loops

```python

for variable in sequence:

    code

```

Example:

```python

for i in range(5):

    print(i)

```

Output:

```text

0

1

2

3

4

```

---

## range()

Creates a sequence of integers.

Format:

```python

range(start, stop, step)

```

Defaults:

```python

start = 0

step = 1

```

Examples:

```python

range(5)

```

Produces:

```text

0 1 2 3 4

```

---

```python

range(1, 5)

```

Produces:

```text

1 2 3 4

```

---

```python

range(1, 10, 2)

```

Produces:

```text

1 3 5 7 9

```

---

## Important Rule

Just like slicing:

```python

range(start, stop)

```

includes:

```python

start

```

but excludes:

```python

stop

```

---

## Running Sum

```python

mysum = 0

for i in range(10):

    mysum += i

print(mysum)

```

Result:

```python

45

```

---

## Factorial Pattern

```python

x = 4

factorial = 1

for i in range(1, x + 1):

    factorial *= i

```

Result:

```python

24

```

---

## Key Takeaways

- while loops repeat while a condition is True.

- for loops iterate through a sequence.

- range() generates integer sequences.

- stop values are excluded.

- Infinite loops happen when conditions never become False.

- Loop variables track progress through iterations.