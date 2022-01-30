# Strings and string literals

## Common types when working with strings

### Character arrays

```cpp
// character type (8 bits), is possible to prepend 'u8' to enforce 8 bit char.
char* s = "Lorem";
// wide character type (16/32 bits, depending on compiler), note the prepended 'L'
wchar_t* s2 = L"Ipsum";

// C++11

// 16 bit character type, note the prepended 'u'
char16_t* s3 = u"Dolor";
// 32 bit character type, note the prepended 'U'
char32_t* s4 = U"Sit";
```

### Strings

```cpp
// <string>
#include <string>
std::string s = "Normal string";
std::wstring s2 = L"Wide string";
std::u16string s3 = u"16 bit string";
std::u32string s3 = U"32 bit string";

// std::string_literals has the 's' operator, useful when concatenating strings
using namespace std::string_literals;
std::string s2 = "Concatenate"s + "strings";
```

## String literals

String literal is basically a string defined inside double quotes:

```cpp
int main()
{
    "I am a string literal";
}
```

Assigning string literals to variables can be done in a couple of ways:

```cpp
// Assigning to array
const char my_string[21] = "I am a string literal";
char my_string[] = "I am a string literal";
// Assigning to pointer
const char* my_string_ptr = "I am a string literal";
```

An important note is that string literals are _always_ stored in _read-only memory_ (const segment in assembly). This is why a pointer must point to `const char` data, and not only `char`. When assigning a string literal to an non-const array however, the string literal is actually copied into the array's allocated memory. Which is why it works to modify the array later on if it is not `const`.

Hence, when using pointers, the following assignment is **undefined behavior**:

```cpp
// Undefined behavior!! (but e.g. MSVC may allow this depending on the compiler settings)
char* my_string = "I am a string literal";
```

More info about this and MSVC [here](https://docs.microsoft.com/en-us/cpp/error-messages/compiler-errors-1/compiler-error-c2440?view=msvc-170#c-string-literals-are-const).

### Raw string literal

There is also the _raw string literal_, defined by starting the string with `R`:

```cpp
const char* ex = R"(My\n
happy
place)";
```

Output:

```shell
My\n
happy
place
```

It prints the text _exactly_ as written, ignoring escape characters (`\n` etc.). Often useful when writing several lines of text.

## `null` termination character

`null` is the termination character, which serves the purpose of telling where the string ends.

```cpp
"I am a string literal\0"; // '\0' is the literal null termination char
```

It is seen in memory as `00` (hex dump):

```text
ASCII:  I     a  m     a     s  t  r  i  n  g     l  i  t  e  r  a  l  \0
Memory: 49 20 61 6d 20 61 20 73 74 72 69 6e 67 20 6c 69 74 65 72 61 6c 00
```

The `null` termination is always added implicitly in _string literals_ so it doesn't have to be added manually. If assigning chars to an array manually, then the `null` character must be added manually as well:

```cpp
char s[] = "Hello";
char s2[] = { 'H', 'e', 'l', 'l', 'o', '\0' };
```

## Useful functions when using strings

```cpp
// Length of string (excludes null termination)
strlen("My string");
```
