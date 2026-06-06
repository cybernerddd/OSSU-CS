# OSSU / MIT 6.100L - Lecture 2: Strings, Input, Output And Branching.

## Strings

Strings are sequences of characters.

```python
s = "hello"
```

### Operations

```python
"hi" + "there"
# "hithere"

"ha" * 3
# "hahaha"
```

### Length

```python
len("abc")
# 3
```

---

## String Indexing

First character is at index 0.

```python
s = "abc"

s[0]  # "a"
s[1]  # "b"
s[2]  # "c"
```

Negative indexing starts from the end.

```python
s[-1] # "c"
```

---

## String Slicing
The format goes by: `[start:stop:step]`, but when 2 inputs are given python sets `step=1` which is default.

```python
s = "abcdefgh"

s[3:6]
# "def"
# The stop index is not included.

s[::-1]
# reverse string
```

Rule:

```python
[start:stop:step]
```

---

## Strings are Immutable

Cannot modify characters directly.

Invalid:

```python
s = "car"
s[0] = "b"
```

Valid:

```python
s = "b" + s[1:]
```

---

## Output

Use print().

```python
print("hello")
```

---

## Input

Use input().

```python
name = input("Name: ")
```

Important:

```python
input()
```

always returns a string.

Convert when expecting numbers.

```python
age = int(input("Age: "))
```

---

## F-Strings

Cleaner way to format output.

```python
name = "Emmanuel"

print(f"Hello {name}")
```

---

## Comparison Operators

```python
>
>=
<
<=
==
!=
```

Examples:

```python
5 > 3
# True

5 == 5
# True
```

---

## Boolean Values

```python
True
False
```

---

## Logical Operators

```python
and
or
not
```

Examples:

```python
True and False
# False

True or False
# True

not True
# False
```

---

## Assignment vs Equality

Assignment:

```python
x = 5
```

Equality test:

```python
x == 5
```

Remember:

- = assigns
- == compares

---

## Branching

### if

```python
if condition:
    code
```

### if / else

```python
if condition:
    code
else:
    code
```

### if / elif / else

```python
if condition:
    code
elif condition:
    code
else:
    code
```

Rule:

First True condition wins.

---

## Indentation

Indentation defines code blocks.

```python
if x > 5:
    print("big")
```

Bad indentation causes errors.

---
## Finger Exercise:
> Assume you are given a variable named number (has a numerical value). Write a piece of Python code that prints out one of the following strings:
> - positive if the variable number is positive
> - negative if the variable number is negative
> - zero if the variable number is equal to zero

#### Answer
```py
if number > 0:
    print("positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```



## Key Takeaways

- Strings are sequences of characters.
- Strings can be indexed and sliced.
- Strings are immutable.
- input() returns a string.
- print() displays output.
- = assigns, == compares.
- Conditions evaluate to True or False.
- Branching controls program flow.
- Indentation matters.
