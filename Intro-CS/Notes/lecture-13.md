# Day 13 - Exceptions and Assertions

## What I Learned

Today I learned how Python handles unexpected situations using exceptions and how programmers can enforce assumptions using assertions.
This lecture focused on making programs more robust and preventing bad data from silently causing problems.

---

## Exceptions

An exception occurs when Python encounters an unexpected condition during execution.

Examples:

### IndexError

```python
test = [1, 7, 4]
print(test[4])
```

Trying to access an index that does not exist.

### TypeError

```python
"a" / 4
```

Using incompatible types together.

### NameError

```python
print(x)
```

Variable does not exist.

---

## Handling Exceptions

Normally an exception stops program execution.
Python allows us to catch and handle exceptions using:

```python
try:
    # risky code
except:
    # handle error
```

Example:

```python
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except:
    print("Invalid input")
```

This prevents the program from crashing.

---

## Specific Exceptions

Instead of catching every error, we can handle specific exceptions.

```python
try:
    a = int(input())
    b = int(input())
    print(a / b)

except ValueError:
    print("Not a number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

This gives more precise error handling.

---

## Raising Exceptions

Sometimes we want to stop execution ourselves.

```python
raise ValueError("Something is wrong")
```

This allows us to signal that invalid data was provided.

Example:

```python
def sum_digits(s):
    total = 0

    for char in s:
        try:
            total += int(char)
        except:
            raise ValueError("String contained a non-digit")

    return total
```

---

## Assertions

Assertions are used to verify assumptions.

Syntax:

```python
assert condition, "error message"
```

If the condition is False, Python raises an AssertionError.

Example:

```python
assert len(s) != 0, "String is empty"
```

If s is empty:

```python
AssertionError: String is empty
```

---

## Why Assertions Are Useful

Assertions help:

- Validate inputs
- Validate outputs
- Catch bugs early
- Prevent invalid program states
- Document assumptions

Example:

```python
def avg(grades):
    assert len(grades) != 0, "No grades available"
    return sum(grades) / len(grades)
```

Without the assertion:

```python
avg([])
```

would cause a division by zero.

---

## Exceptions vs Assertions

### Exceptions

Use when:

- Users may provide bad input
- The program can recover
- You want to handle the problem gracefully

Example:

```python
try:
    num = int(input())
except ValueError:
    print("Invalid number")
```

---

### Assertions

Use when:

- A condition should never be violated
- A programmer assumption must be true
- Execution should stop if the assumption fails

Example:

```python
assert age >= 0, "Age cannot be negative"
```

---

## FINGER EXERCISE
```python

def sum_str_lengths(L):
    """
    L is a non-empty list containing either: 
    * string elements or 
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and 
    lengths of strings in the sublists of L. If L contains an 
    element that is not a string or a list, or L's sublists 
    contain an element that is not a string, raise a ValueError.
    """
    # Your code here  
    assert len(L) != 0
    total = 0
    for i in L:
        if type(i) == str:
            total += len(i)
        elif type(i) == list:
            for e in i:
                if type(e) == str:
                    total += len(e)
                else:
                    raise ValueError(e, "Not a string")
        else:
            raise ValueError()
    return total
            

# Examples:
print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError
```


## Key Takeaways

- Exceptions occur when unexpected conditions arise.
- try/except prevents programs from crashing.
- Specific exceptions are better than generic except blocks.
- raise allows programmers to create their own exceptions.
- Assertions verify assumptions.
- Assertions are a defensive programming tool.
- Exceptions handle bad input.
- Assertions enforce programmer contracts.

---

## Reflection

This lecture changed how I think about errors.

Previously I saw errors as things to avoid.

Now I understand that good programs expect things to go wrong and handle them appropriately.

Exceptions help manage unexpected situations, while assertions help catch programmer mistakes early.

Together they make software more reliable and easier to debug.
