# Hash Tables

Hash tables are a data structure that stores key-value pairs. They allow for fast insertion and retrieval of data by using a hash function to map keys to indexes in an array.

## Hash Functions

A hash function is a function that takes an input (or "key") and returns
an index in an array. The hash function should be deterministic, meaning
that the same input will always return the same output.

A good hash function will

- be fast to compute
- evenly distribute keys across the array
- minimize collisions
- be deterministic

### Example

```python
def some_hash_function(key):
    return len(key) % 10
```

## Collision Resolution

A collision occurs when two keys map to the same index in the array. There are
several ways to resolve collisions:

1. **Open Addressing**: When a collision occurs, the hash table will search for
   the next available slot in the array. This can be done using linear probing,
   plus 3 rehashing, quadratic probing, or double hashing.

    1. **Linear Probing**: When a collision occurs, the hash table will search
        for the next available slot in the array by incrementing the index by 1.

    2. **Plus 3 Rehashing**: When a collision occurs, the hash table will search
        for the next available slot in the array by incrementing the index by 3.

    3. **Quadratic Probing**: When a collision occurs, the hash table will search
        for the next available slot in the array by incrementing the index by 1 $(1^2)$, 4 $(2^2)$, 9 $(3^2)$, 16 $(4^2)$, etc.

    4. **Double Hashing**: When a collision occurs, the hash table will search
        for the next available slot in the array by incrementing the index by a
        second hash function.

2. **Closed Addressing (Chaining)**: When a collision occurs, the hash table will store multiple
    key-value pairs at the same index in the array. This can be done using a linked list, binary search tree, or other data structure.

## Time Complexity

The time complexity of hash tables is `O(1)` for insertion, deletion, and retrieval in the average case. However, the time complexity can be `O(n)` in the worst case if there are many collisions.

## Space Complexity

The space complexity of hash tables is `O(n)` where n is the number of key-value pairs stored in the hash table.

## Applications

Hash tables are used in many applications, including databases, caches, and sets.

## Implementation

Hash tables can be implemented using arrays, linked lists, and other data structures. This folder contains examples of a hash table implemented using an array and linked list in Python using different hashing functions.
