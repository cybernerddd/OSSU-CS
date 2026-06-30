# Day 14 - Dictionaries

## What I Learned

Today I learned about dictionaries in Python.
A dictionary is a data structure that stores data as key-value pairs.
Ulike lists, which use integer indices, dictionaries allow us to look up values using keys.

---

## Dictionary Syntax

Example:

```python
student = {
    "name": "Michael",
    "age": 25,
    "country": "Ghana"
}
```

Keys map to values using a colon (:).

---

## Accessing Values

```python
student["name"]
```

Returns:

```python
"Michael"
```

Another example:

```python
grades = {
    "Ana": "A",
    "Bob": "B"
}
```

```python
print(grades["Ana"])
```

Output:

```python
A
```

---

## Dictionary vs List

### Lists

```python
L = [10, 20, 30]
```

Access using integer indices:

```python
L[0]
```

Returns:

```python
10
```

---

### Dictionaries

```python
D = {
    "Ana": "A",
    "Bob": "B"
}
```

Access using keys:

```python
D["Ana"]
```

Returns:

```python
"A"
```

Lists are ordered.

Dictionaries store mappings between keys and values. :contentReference[oaicite:1]{index=1}

---

## Nested Dictionaries

Dictionaries can contain other dictionaries.

Example:

```python
grades = {
    "Ana": {
        "mq": [5,4,4],
        "ps": [10,9,9],
        "fin": "B"
    }
}
```

This allows us to organize complex data structures. :contentReference[oaicite:2]{index=2}

---

## Accessing Nested Data

Example:

```python
grades["Ana"]["mq"][0]
```

Returns:

```python
5
```

This accesses:

1. Ana's record
2. mq list
3. First quiz score

:contentReference[oaicite:3]{index=3}

---

## Dictionary Methods

### keys()

Returns all keys:

```python
student.keys()
```

---

### values()

Returns all values:

```python
student.values()
```

---

### items()

Returns key-value pairs:

```python
student.items()
```

Example:

```python
for k, v in student.items():
    print(k, v)
```

---

## Counting Frequencies

One powerful use of dictionaries is counting occurrences.

Example:

```python
song = "rah rah ah ah ah"
```

Create:

```python
{
    "rah": 2,
    "ah": 3
}
```

This maps each word to the number of times it appears. :contentReference[oaicite:4]{index=4}

---

## Updating a Dictionary

```python
if word in word_dict:
    word_dict[word] += 1
else:
    word_dict[word] = 1
```

This is the core pattern used for frequency counting. :contentReference[oaicite:5]{index=5}

---

## Mutating Dictionaries

We can remove entries:

```python
del(word_dict["rah"])
```

After deletion, the key no longer exists. :contentReference[oaicite:6]{index=6}

---

## Why Dictionaries Are Useful

Dictionaries allow:

- Fast lookups
- Storing related data
- Counting frequencies
- Building databases
- Organizing structured information

Examples:

- Student grades
- User accounts
- Configuration settings
- Word counters
- Caches

## FINGER EXERCISE
**Exercise-1**:
```python
def keys_with_value(aDict, target):
    """
    aDict: a dictionary
    target: an integer or string
    Assume that keys and values in aDict are integers or strings.
    Returns a sorted list of the keys in aDict with the value target.
    If aDict does not contain the value target, returns an empty list.
    """
    # Your code here  
    target_keys = []
    
    for k in aDict:
        # k can be [1,2....]
        
        if aDict[k] == target:
            target_keys.append(k)
    target_keys.sort()
    
    return target_keys

# Examples:
aDict = {1:2, 2:4, 5:2}
target = 2   
# print(keys_with_value(aDict, target)) # prints the list [1,5]
```
**Exercise-2:**
```python
def all_positive(d):
    """
    d is a dictionary that maps int:list
    Suppose an element in d is a key k mapping to value v (a non-empty list).
    Returns the sorted list of all k whose v elements sums up to a 
    positive value.
    """
    # Your code here  
    postive_nums = []
    for k in d:
        # k is 5,2...
        
        if sum(d[k]) > 0:
            postive_nums.append(k)
            
    postive_nums.sort()
    return postive_nums

    # Using list compressions and one liner code
    # return sorted([k for k,v in d.items() if sum(v) > 0])


# Examples:
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))   # prints the list [1, 2]
```

---

## Key Takeaways

- Dictionaries store key-value pairs.
- Keys must be unique.
- Keys are immutable/hashable objects.
- Values can be any type.
- Dictionaries are useful for fast lookups.
- Dictionaries can contain other dictionaries.
- Dictionaries are commonly used for counting and organizing data.

---

## Reflection

Today was my first deep dive into dictionaries.

The biggest takeaway was realizing that dictionaries allow me to access information using meaningful keys instead of numeric indices.

I can already see how useful they will be for storing user data, application settings, frequency counters, and structured information in future projects.
