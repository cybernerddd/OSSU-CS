# OSSU - Lecture 1: Introduction

## Declarative vs Imperative Knowledge

- Declarative = facts (what is true)
- Imperative = instructions (how to do something)
Programming in Imperative
---

## Algorithms

An algorithm must have:

1. Sequence of steps
2. Flow of control
3. Stopping condition

Example:
1. Open browser
2. Go to TryHackMe
3. Complete room
4. Logout

---

## Computers

Computers do two things:

1. Perform operations
2. Store results

Important:
> A computer only does what you tell it to do.

---

## Python Objects

Objects are values stored in memory.

Common types:

- int -> 5, -10
- float -> 3.14, 2.0
- bool -> True, False
- NoneType -> None

Check type:

```python
type(5)
```

---

## Expressions

Expressions evaluate to a single value.

Examples:

```python
3 + 2
# 5

2 ** 3
# 8

17 % 5
# 2

17 // 5
# 3
```

---

## Operator Precedence

1. ()
2. ** (exponent)
3. *
4. / division
5. // - Floor division(Just like using the round object)
6. % - modulo (divide and show remainder)
4. + Add
5. - Subtract

Example:

```python
3 + 4 * 2
# 11

(3 + 4) * 2
# 14
```

---

## Variables

Variables bind names to values.

```python
x = 5
```

Means:

- Variable name: x
- Value: 5

Important:

```python
x = 5
x = 10
```

Final value:

```python
10
```

Newest assignment wins.

---

## Assignment

`=` means assignment, NOT equality.

Valid:

```python
x = 6
```

Invalid:

```python
6 = x
```

Reason:
Values cannot receive assignments.

---

## Execution Order

Python executes code top-to-bottom.

```python
meters = 100
feet = 3.2808 * meters
meters = 200
```

Final:

```python
meters = 200
feet = 328.08
```

Python only executes what you tell it to execute.
## EXERCISE
> Assume 3 variables are already defined for you: a, b, and c. Create a variable called total that adds a and b then multiplies the result by c. Include a last line in your code to print the value: print(total)

#### Answer
total = c*(a+b)
