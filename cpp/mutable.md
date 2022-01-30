# `mutable` keyword

Declaring a member variable as `mutable` permits it to be modified even though the method is declared as `const`.

```cpp
#include <iostream>
#include <string>

class Entity
{
private:
    std::string m_Name;
    int m_DebugCount = 0;
    mutable int m_DebugCountMutable = 0;
public:
    // we mark method as const...
    const std::string& GetName() const
    {
        m_DebugCount++;  // not allowed
        m_DebugCountMutable++; // allowed, variable is mutable
        return m_Name;
    }
};

int main()
{
    const Entity e;
    // ...to be able to call .GetName() here
    e.GetName();
}
```

## `mutable` and lambdas

Another, more rare, use of `mutable` is with lambda functions:

```cpp
int main()
{
    int x = 8;
    // Lambda function, passing by value -> [=]
    auto f = [=]() mutable
    {
        // by making the lambda mutable, x can be incremented inside it
        x++;
        std::cout << x << std::endl;
    };

    f();
    // x = 8 here, since x was passed by value to lambda
}
```
