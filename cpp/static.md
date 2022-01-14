# `static` keyword

The keyword `static` is used in two contexts in C++.

## `static` on variables and functions

The first use case is to set functions and variables to only be accessible to the local scope, i.e. it should only be accessible within the translation unit (I will somewhat incorrectly refer to it as "source file" from now on) where it is declared. A common case is where we want a global variable in a source file that should be accessible to all functions within that file. If we wouldn't set the variable as `static`, its name cannot be used again when defining another global variable in another source file (duplicate symbols), since it is accessible to the linker in the global scope.

## `static` on member variables and class methods

The second use case is when we set member variables or class methods within a class or struct to `static`. A variable that is set to `static` will be shared across all instances of the class. If one instance changes the variable that change is reflected in all instances. It can be viewed as a global variable within the class. There is no meaning to access the variable through an instance, since it is a global property of the class.

A side-effect of `static` is that the variable is declared inside the class, but must be defined outside of it.

How to use static variables correctly:

```cpp
struct Entity
{
    // Declaring x and y
    static int x, y;
};

// Defining x and y
int Entity::x;
int Entity::y;

int main()
{
    // Manipulate x and y
    Entity::x = 2;
    Entity::y = 3;
}
```

Declaring a method as `static` has a similar effect. It means that the method can be used without an instance. However, it also means that the method cannot manipulate non-static variables.
