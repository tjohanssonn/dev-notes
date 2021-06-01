# xargs

Usage:

```bash
xargs [OPTIONS] [COMMAND [INITIAL ARGS]]
```

Reads items from standard input or file, and converts these into arguments passed to the given command.

## Examples

```bash
find /tmp -name core -type f -print | xargs /bin/rm -f
```

Find files named _core_ in or below the directory _/tmp_ and delete them. Note that this will work incorrectly if there are any filenames containing newlines or spaces (pass `-print0` to `find` to solve that).
