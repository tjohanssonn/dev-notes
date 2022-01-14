# Constructors and destructors

When an object is instantiated, a special function named _constructor_ is called.

When an object is destroyed, a special function called _destructor_ is called.

## Constructor

An important thing to know about C++ is that the default constructor **does not** initialize any variables, not even primitive types such as integers or floats. This differs from most other languages such as Java. You get no help here. If you forget to initialize the variables they will just get whatever value already stored in the allocated memory.

```cpp
class MyClass
{
    MyClass()
    {
        // The default constructor used when not specifying one yourself.
    }
}
```

You can use multiple constructors if you provide different parameters:

```cpp
class MyClass
{
    MyClass()
    {
        // The default constructor used when not specifying one yourself.
    }

    MyClass(int x)
    {
        // Do something with 'x'
    }
}
```

## Destructor

Uninitializes and cleans memory used by the object. E.g. if memory is allocated manually on the heap in the constructor, it must be cleaned manually in the destructor. Otherwise we will get a memory leak.

```cpp
class MyClass
{
    ~MyClass()
    {
        // The default destructor used when not specifying one yourself.
    }
}
```
