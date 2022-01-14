# Compiler and linker

Our source code is just text, that needs to be transformed into an executable binary.

To achieve this two things must happen - compiling and linking.

## Compiler

The compiler takes source code as input and outputs _object files_. Each `.cpp` file is compiled into an object file, which is basically containing constant data and instructions. This code is what the target processor will actually execute.

This transformation is made in multiple steps:

1. Preprocessing
2. Transform the source into an [abstract syntax tree (AST)](https://en.wikipedia.org/wiki/Abstract_syntax_tree)
3. Generate machine code (create object files)

### Preprocessing

Preprocessing is done before compilation and basically does a translation of the statements starting with `#` (the `#include`, `#define`, `#if`, `#ifdef`, `#pragma` etc.).

#### A note on `#include`

`#include` does exactly what it says, it _includes_ the contents of the file starting at the line with the `#include` statement. Nothing else happens, it is just a simple _copy and paste_ of the contents.

### Linker

Each object file that is created by the compiler have no relation to one another.

The purpose of the linker is to find where each symbol and function is in these objects and link them together into one executable binary.

## Errors when building a project

Since "building the project" always involves compiling and linking, there two primary types of errors; errors when compiling and errors when linking. These errors are differentiated in the output window by looking at the error code; compiler errors start with `C` and linker errors start with `LNK`:

```bash
# Example error during compilation
error C2143: syntax error: <some syntax error message>
# Example error during linking
fatal error LNK1561: entry point must be defined
```
