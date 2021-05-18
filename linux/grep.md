# grep

Synopsis: `grep [OPTIONS] PATTERN [FILE...]`

Utility tool to print lines matching a pattern. Typically used in pipes for filtering the results if a previous command.

`PATTERN` can be provided as a regular expression if required.

## Often used commands

This tool has an enourmous amount of options for every possible niche use case. However, there are a few variants I frequently use.

`grep PATTERN [FILE]`
Search for pattern in the provided file, or if file is not provided, reads standard input (equivalent to `grep PATTERN -`). A typical variant I often see is to write `cat /path/to/file | grep PATTERN`, which is equivalent to `grep PATTERN /path/to/file`.

`grep -v PATTERN`
Invert match, i.e. print everything not matching the provided pattern.

`grep -E PATTERN`
Interpret the pattern as an extended regular expression, e.g. `"(MyString1|MyString2)`. If not using extended mode, the characters '?', '+', '{', '|', '(', and ')' lose their special meaning in the world of regular expressions.
