# `const` keyword

## Variables

`const` keyword is a _promise_ that the constant variable's data will not change during its lifetime.

A misconception though is that `const` directly affects the generated code, which it _does not_. It is not stored in read-only memory just because it is declared as `const`. This means that it may be possible to circumvent this protection, e.g. by using pointers. However, writing to `const` variables are undefined behavior, so what will happen is unknown.

## Classes

Methods in a class can be defined as `const`:

```cpp
class Entity:
{
private:
    int m_X;
public:
    int GetX() const
    {
        return m_X;
    }
}

```

Declaring a method as `const` means that it is read-only. It will not modify member variables (writing) to the class.

Always mark methods as `const` if they only read since it is otherwise not possible to use the method if referring to it via a constant reference. E.g. when passing an object reference to a function, which in turn tries to access the method of the object.
