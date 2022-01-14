# Visibility

There's three visibility modifiers in C++ related to object-oriented programming:

1. `public`
2. `private`
3. `protected`

`public` and `private` are exactly what they mean; `public` makes a member or method of a class accessible from outside the class, while `private` makes it inaccessible.

`protected` is a variant of `private` in that something is inaccessible from outside the class apart from classes that inherits from it, i.e. children / subclasses.

## Default visibility setting

If you don't specify a visibility modifier, a default one will be used:

- A class has `private` as the default visibility setting.
- A struct has `public` as the default visibility setting.

## `friend` keyword

Everything stated above is valid as long as a class is not specified as a `friend` to another class. The `friend` keyword makes private members and methods in the other class accessible.

## Notes

These keywords does not affect performance in any way. It is purely a construct within the language that is enforced by the compiler. The generated **machine code is not affected**.
