# References

References are an extension of pointers and can be seen as syntactic sugar on top of pointers. There is nothing you can do with a reference that you can't do with a pointer.

Semantically though - how we write and use them - are different.

References are not new variables like pointers, hence they don't occupy memory. A reference can't be `null`, it always reference a variable.

A reference is created with the ampersand `&` added after the type (it is NOT the same as using `&` with pointers):

```cpp
int a = 10;
// Create a reference to 'a'
int& ref = a;
```

The "variable" `ref` only exists in the source code, it will not exist in the compiled code. It can be seen as an alias of the variable `a` and can be used to manipulate `a`. `ref` _is_ `a`.

Typical use case of a reference is to pass a variable _by reference_ to a function:

```cpp
void increment(int& value)
{
    value++;
}

int main()
{
    int a = 5;
    // Passing 'a' by reference to increment()
    increment(a);
    // a = 6
    std::cout << a << std::endl;
}
```

Remember that a reference is _constant_, it can't be changed to reference something else.
