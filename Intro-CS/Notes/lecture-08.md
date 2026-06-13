# OSSU CS - Day 8: Functions as Objects

---

## Functions are First-Class Objects

In Python, functions are objects.

This means they can:

- Be assigned to variables

- Be passed as arguments

- Be returned from other functions

Example:

```python

def add(a, b):

    return a + b

operation = add

print(operation(2, 3))

```

Output:

```text

5

```

---

## Functions as Parameters

A function can be passed into another function.

Example:

```python

def add(a, b):

    return a + b

def calc(op, x, y):

    return op(x, y)

print(calc(add, 2, 3))

```

Output:

```text

5

```

Explanation:

1. `add` is passed into `calc`

2. Inside `calc`, `op` refers to `add`

3. `op(x, y)` becomes `add(2, 3)`

4. Result is `5`

---

## Function Scope

Variables created inside a function belong only to that function.

Example:

```python

def greet():

    message = "Hello"

```

`message` only exists inside `greet()`.

This is called **local scope**.

---

## Global Scope

Variables created outside functions belong to the global scope.

Example:

```python

name = "Cybernerddd"

```

This variable can be accessed from the main program.

---

## Return Values

Functions can send values back using `return`.

Example:

```python

def square(x):

    return x * x

```

```python

result = square(4)

print(result)

```

Output:

```text

16

```

---

## Print vs Return

### Print

Displays something on the screen.

```python

def greet():

    print("Hello")

```

### Return

Sends a value back to the caller.

```python

def greet():

    return "Hello"

```

---

## Functions Without Return

If a function does not explicitly return a value, Python returns:

```python

None

```

Example:

```python

def test():

    print("Hello")

print(test())

```

Output:

```text

Hello

None

```

---

## Key Takeaways

- Functions are first-class objects.

- Functions can be assigned to variables.

- Functions can be passed as arguments.

- Functions can return values.

- Variables inside functions are local.

- Variables outside functions are global.

- Functions without a return statement return `None`.

- Understanding scope helps avoid bugs and confusion.

---

## Personal Notes

This lecture helped me understand that functions are more than reusable code blocks. They are actual objects that can be passed around like data.

The biggest takeaway was understanding the difference between:

```python

print(...)

```

and

```python

return ...

```

because this affects how information flows through a program.
