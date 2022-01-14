# Pointers

A pointer is an integer that stores a memory address.

Types has nothing to do with pointers. You can assign a pointer a type, but that only says that we assume that the data is the type we give it. A pointer itself does not need a type. A type on the pointer is essentially meaningless to the pointer itself. Assigning a type to a pointer is useful when we need to manipulate the data.

Repeat after me:

- A pointer is an integer that stores a memory address.
- A pointer is an integer that stores a memory address.
- A pointer is an integer that stores a memory address.

## Raw pointers

```cpp
// A void pointer, i.e. no type assigned to the data at the pointer's memory address
void* ptr = 0x80000;
```

It is perfectly valid to assign `0`, `NULL` or `nullptr` (C++ keyword) to a pointer. It just means that the pointer doesn't point to any memory.

We can take the memory address of a variable by using the ampersand `&`:

```cpp
int a = 10;
// Assign 'ptr' with the memory address of variable 'a'
void* ptr = &a;
```

Dereferencing a pointer is used when we need to access the data referenced by the pointer, i.e. reading or writing the data. When dereferencing a pointer it must have a type assigned, otherwise the compiler is clueless on how to interpret the data (how many bytes).

```cpp
int a = 10;
void* ptr = &a;
// Write a new value to 'a' by dereferencing the pointer
*ptr = 25;
```

A pointer is just a variable itself stored in memory. Due to this it's possible to chain pointers, e.g. pointer-to-pointer, a.k.a. double pointer.

```cpp
char* buffer = new char[8];
memset(buffer, 0, 8);
// Assign 'ptr' the address if the pointer 'buffer'
char** ptr = &buffer;
```

## Smart pointers

To be continued...
