# OSSU / MIT 6.100L - Lecture 4: Guess-and-Check Algorithms

A guess-and-check algorithm systematically tries possible solutions until it finds one that works.

General pattern:

```python

for guess in possible_values:

    if solution_found:

        print(guess)

```

---

## Exhaustive Enumeration

Exhaustive enumeration means checking every possible value in a search space.

Example:

```python

cube = 27

for guess in range(cube + 1):

    if guess ** 3 == cube:

        print(guess)

```

Output:

```text

3

```

---

## Boolean Flags

A Boolean flag is a variable used to signal whether something happened.

Example:

```python

found = False

for i in range(1, 11):

    if i == 7:

        found = True

print(found)

```

Output:

```text

True

```

Common values:

```python

True

False

```

---

## break

`break` immediately exits the current loop.

Example:

```python

for i in range(10):

    if i == 5:

        break

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

## Looping Through Strings

A `for` loop can iterate through characters in a string.

Example:

```python

word = "Cyber"

for letter in word:

    print(letter)

```

Output:

```text

C

y

b

e

r

```

---

## Guess-and-Check Cube Root

Example:

```python

cube = 27

for guess in range(cube + 1):

    if guess ** 3 == cube:

        print(guess)

```

Output:

```text

3

```

---

## Binary Numbers

Computers store information using binary digits:

```text

0

1

```

Binary uses base 2 instead of base 10.

Example:

```text

Decimal: 13

Binary: 1101

```

Because:

```text

8 + 4 + 1 = 13

```

---

## Decimal to Binary Conversion

Useful operators:

```python

%

```

Remainder operator.

```python

//

```

Integer division operator.

Example:

```python

13 % 2

```

Output:

```text

1

```

Example:

```python

13 // 2

```

Output:

```text

6

```

---

## Floating-Point Numbers

Python stores decimal numbers using floating-point representation.

Example:

```python

0.1

0.2

0.3

```

Important:

Floating-point calculations may contain tiny rounding errors.

Example:

```python

x = 0

for i in range(10):

    x += 0.1

```

`x` may not be exactly equal to `1.0` due to floating-point precision limitations.

---

## Key Takeaways

- Guess-and-check is a simple problem-solving algorithm.

- Exhaustive enumeration checks every possible solution.

- Boolean flags track whether something happened.

- `break` exits a loop immediately.

- `for` loops can iterate through strings.

- Computers use binary (base 2) internally.

- `%` gives the remainder.

- `//` performs integer division.

- Floating-point numbers are approximations and may introduce small errors.