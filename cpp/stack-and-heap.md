# Stack and heap

Memory can be split in two variants - stack and heap.

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
