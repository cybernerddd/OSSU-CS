# OSSU CS — Day 05 Notes
## MIT 6.100L Lecture 5: Floating Point Numbers & Approximations

## Big Idea

Computers store numbers using **binary (base 2)**, not decimal (base 10).

Some decimal fractions can be represented exactly in binary, while others cannot.

When a number cannot be represented exactly, the computer stores the **closest approximation**.

This is why floating-point arithmetic can sometimes produce unexpected results.

---

## Floating Point Numbers (Floats)

A float is a number with a decimal point.

Examples:

```python
3.14
0.5
-2.75
```

---

## Decimal Fractions

In decimal (base 10):

```text
0.375
```

means:

```text
3 × 10⁻¹ + 7 × 10⁻² + 5 × 10⁻³
```

because:

```text
10⁻¹ = 0.1
10⁻² = 0.01
10⁻³ = 0.001
```

So:

```text
0.375 = 0.3 + 0.07 + 0.005
```

---

## Binary Fractions

Binary uses powers of 2.

For digits after the binary point:

```text
2⁻¹ = 0.5
2⁻² = 0.25
2⁻³ = 0.125
2⁻⁴ = 0.0625
2⁻⁵ = 0.03125
```

### Example

Binary:

```text
0.011₂
```

becomes:

```text
0 × 0.5 + 1 × 0.25 + 1 × 0.125
```

```text
0.25 + 0.125
```

```text
= 0.375
```

Therefore:

```text
0.011₂ = 0.375₁₀
```

---

## Why Some Fractions Cannot Be Represented Exactly

Some decimal fractions have an exact binary representation:

```text
0.5
0.25
0.125
```

Others do not:

```text
0.1
0.2
0.3
```

The binary representation continues forever, so the computer must cut it off and store an approximation.

Example:

```python
0.1 + 0.2
```

may produce:

```python
0.30000000000000004
```

instead of:

```python
0.3
```

---

## Comparing Floats

Avoid checking floats with:

```python
==
```

Example:

```python
answer = 0.30000000000000004

if answer == 0.3:
    print("Equal")
```

This may fail because of approximation errors.

Instead, check whether the values are close enough.

---

## Absolute Value

```python
abs(x)
```

returns the positive distance from zero.

Examples:

```python
abs(5)     # 5
abs(-5)    # 5
abs(-10)   # 10
```

---

## Approximation Method

Instead of checking for exact equality:

```python
guess == answer
```

use:

```python
abs(guess - answer) < epsilon
```

where `epsilon` is a very small value.

Example:

```python
abs(guess - answer) < 0.01
```

Meaning:

```text
The guess is close enough.
```

---

## Accuracy vs Efficiency

Smaller step size:

```python
0.00001
```

Pros:

```text
More accurate
```

Cons:

```text
Slower
```

Larger step size:

```python
0.1
```

Pros:

```text
Faster
```

Cons:

```text
Less accurate
```

---

## Key Takeaways

- Computers store numbers in binary.
- Floats are approximations.
- Some decimal fractions cannot be represented exactly in binary.
- Floating-point arithmetic may contain small errors.
- Avoid using `==` when comparing floats.
- Use `abs(guess - answer) < epsilon` for comparisons.
- Smaller approximation steps increase accuracy but reduce speed.

---

## Finger Exercise
> Assume you are given a string variable named my_str. Write a piece of Python code that prints out a new string containing the even indexed characters of my_str. For example, if my_str = "abcdefg" then your code should print out aceg. 

##### ANSWER
**Using while loop**
```py
my_str = "abcdefghi"

i = 0
while i < len(my_str):
    print(my_str[i], end="")
    i += 2

```
**Using For Loop:**
```py
my_str = "abcdefghi"

for i in range(0, len(my_str), 2):   # step by 2
    print(my_str[i], end="")   # print without newline
```

## Things That Finally Clicked

- `1 bit` stores either `0` or `1`.
- `8 bits = 1 byte`.
- `32 bits = 4 bytes`.
- `64 bits = 8 bytes`.
- `n bits` can represent `2ⁿ` possible values.
- `8 bits = 256 possible values (0–255)`.
- Networking values like `255.255.255.0` come directly from binary representation.
