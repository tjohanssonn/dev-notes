# Stack and heap

Application memory can be split in two variants - stack and heap. Both are stored in RAM.

**TL;DR: If you can create an object on the stack, do it.**

## Stack

Stack objects have an automatic lifespan. They only live within the scope where they are declared. As soon as the variable goes out of scope the memory is freed (= the stack frame is destroyed).

Stack memory is quite small, usually 1-2 MB. However, you get better performance when working towards the stack than the heap.

Creating/instantiating an object on the stack is as simple as this:

```cpp
class Entity:
{
public:
    Entity(){}
};

int main()
{
    // Creation of an Entity object on the stack
    Entity entity;
}
```

## Heap

Heap objects do not have an automatic lifespan. They live on until _you_ free up the memory by destroying the object. If a heap object is not deleted a memory leak is created.

An object is created on the heap with the `new` keyword:

```cpp
int main()
{
    // Creation of an Entity object on the heap
    Entity* entity = new Entity();
}
```

### Reasons for allocating on the heap

There's a few reasons why you would want to allocate objects on the heap:

- You want the object to live outside the scope where it's declared
- Stack memory is not large enough, due to:
  - Class is too large to allocate on the stack
  - Too many instances of the class may be created to fit on the stack

## Side track - scoped pointer

Unique pointer in C++ is what is known as a _scoped pointer_. At the very basic level it uses the scope characteristics of heap and stack to automatically clean up the memory when the pointer goes out of scope.

At its core it can be illustrated like this:

```cpp
class ScopedPtr
{
private:
    Entity* m_Ptr;
public:
    ScopedPtr(Entity* ptr)
        : m_Ptr(ptr)
    {
    }

    ~ScopedPtr()
    {
        delete m_Ptr;
    }
}

int main()
{
    {
        // Create e, which is allocated on the stack and use it as a wrapper
        // around the pointer to heap-allocated memory.
        ScopedPtr e = new Entity();
        // Can also be written as (equivalent):
        // ScopedPtr e(new Entity());
    }
    // Here, e is destroyed since it goes out of scope.
    // Allocated heap memory is cleaned in its destructor.
}
```
