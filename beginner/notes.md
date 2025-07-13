## 1. del keyword
   ```del``` keyword is used for deleting variable references and it would throw NameError when there is a call to a variable after it has been deleted.
## 2. Python vs C/C++ Variables
![   ](./python_vs_c_c++.png)

## 3. Difference Between List and Tuple in Python

Python provides two commonly used sequence types: **lists** and **tuples**. While both can store collections of items, they have important differences:

### 1. Mutability

- **List:** Mutable (can be changed after creation; elements can be added, removed, or modified).
- **Tuple:** Immutable (cannot be changed after creation; elements cannot be added, removed, or modified).


### 2. Syntax

- **List:** Defined using square brackets `[ ]`.
    - Example: `my_list = `
- **Tuple:** Defined using parentheses `( )`.
    - Example: `my_tuple = (1, 2, 3)`


### 3. Methods

- **List:** Has many built-in methods such as `append()`, `remove()`, `pop()`, and `sort()`.
- **Tuple:** Has very few built-in methods (mainly `count()` and `index()`).


### 4. Use Cases

- **List:** Preferred when you need a collection of items that may change during program execution.
- **Tuple:** Preferred for fixed collections of items or when you want to ensure data cannot be modified (e.g., as keys in a dictionary).


### 5. Performance

- **Tuple:** Slightly faster than lists for iteration and access, due to immutability.
- **List:** Slightly slower, as they are mutable and require extra memory for dynamic operations.


### 6. Memory Usage

- **Tuple:** Generally uses less memory than a list of the same size.
- **List:** Uses more memory due to dynamic nature.


### Comparison Table

| Feature | List | Tuple |
| :-- | :-- | :-- |
| Mutability | Mutable | Immutable |
| Syntax | `` | `(1, 2, 3)` |
| Methods | Many | Few |
| Performance | Slower | Faster |
| Memory | More | Less |
| Use as dict key | Not allowed | Allowed (if elements are immutable) |

### Summary

- Use **lists** when you need to modify, add, or remove items.
- Use **tuples** when you need a fixed, unchangeable sequence or want to use the sequence as a dictionary key.

## 4. Data Type Conversion Functions

Read the topic in this link [Data Type Conversion Functions - tutorialspoint](https://www.tutorialspoint.com/python/python_type_casting.htm)