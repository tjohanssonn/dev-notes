# rm

Usage:

```bash
rm [OPTION]... [FILE]...
```

Remove files or directories on system.

## Useful options

`-f` ignore nonexistent files and arguments, never prompt

`-i` always prompt before removal

`-r, -R` recursively delete (must be used to remove directories)

`-v` verbose output

## Remove list of files

A handy way to remove multiple files is to combine `find`, `xargs` and `rm`:

```bash
find . -type f -name '*.txt' | xargs rm -rf
```

Find files matching _pattern_, pipe them to `xargs`, which in turn passes them as arguments to `rm`.
