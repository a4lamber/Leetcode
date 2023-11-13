# Python DS

## Chapter 1. Collections

### 1.1 Collection Types
**Collection** (A.K.A. abstract data types ADTs) is defined as a group of zero or more items can be treated as a conceptual unit. 

Some categorization of collection is:
- `static` or `dynamic`
- `homogeneous` or `heterogeneous`
- `mutable` or `immutable`
- the manner in which they are organized
  - linear collections
  - hierarchical collections
  - graph collections
  - unordered collections


Let's see a diagram with different abstract data type with some implementation.

- Collection Types
  - Graph Collection
  - Hierarchical collection
    - Binary search tree
    - Heap
  - Linear collection
    - List
      - Sorted list
    - Queue
      - Priority queue
    - Stack
    - String
  - Unordered collection
    - Bag
      - Sorted bag
    - Dictionary
      - Sorted dictionary
    - Set
      - Sorted set


## Chap 2. Arrays and Linked Structures

Outline:
- implement an `Array` concrete data structure
- implement an `Grid` concrete data structure

### 2.1 The Array

> dunder method: dunder is short for double under score method such as ``__init__`` and ``__setitem__``. It doesn't explicitly call the method but implicitly called by other ways.

### 2.2 Two-Dimensional Arrays (Grids)

### 2.3 Linked Structures

If you recall operation on arrays are already index-based. It is a popular and more human-friendly way of organizing things. Therefore, we need to implement index-based operation like traversal, search 


## Chapter 5 Interfaces, Implementations and Polymorphism

Well-designed software is the clean separation of interfaces from implementations to serves the following purposes:
- flattens the learning curve for a resource's users (Kinda like API)
- Allows users to quickly glue resources together in a plug-and-play fashion

> `Polymorphism`: a concept in software design, polymorphism is just the idea that multiple implementations of a resource conform to the same interface or set of methods.


### 5.1 Developing an interface

In this section, we are gonna learn a simple collection type called **bag**.

#### Designing the Bag Interface

**Step 1: List its features**

A bag in real-life has the following features:
- check whether its empty
- to empty a bag
- to determine whether a given item is in a bag
- to view each item in a bag without emptying it
  - give ur access to a bag's content
  - give u a printable version of a bag's contents - string
- Whether two bags contain the same objects
- combine the contents of two bags into a third bag (concatenation)
- how to create a bag

**Step 2: draw up a list of names**

You need to come up with a list of function names, method names and operator symbols that meets the above feature described in step 1.









