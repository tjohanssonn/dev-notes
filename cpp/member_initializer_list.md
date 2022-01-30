# Member initializer lists

**TL;DR: Always use member initializer lists.**

When initializing a class, the member variables can either be initialized inside the constructor's angle brackets `{}`, or with an _initializer list_:

```cpp
class Entity
{
private:
    std::string m_Name
    int x;
public:
    Entity()
        : m_Name("Unknown"), x(0)
    {
    }
}
```

**Note!** It is important that the members are _in the same order_ in the list as they are declared in the class. Some compilers let this through, can be it can cause strange bugs.

There's two reasons for using initializer lists: cleaner code and performance.

An initializer list can make the code less cluttered and make is easier to see the important stuff happening in the constructor (e.g. calling init methods).

Initializer lists are also more performant since the variables are only initialized once, not twice. When assigning values inside the constructor's `{}`, the variable is first assigned a default value in the default constructor. This value is discarded when the variable is assigned a new value in the "custom" constructor (this does not apply to primitive types, but just adopt the habit of using initializer lists everywhere).
