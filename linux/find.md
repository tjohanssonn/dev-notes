# find

Utility tool to find files and directories in a path.

Synopsis:
`find [-H] [-L] [-P] [-Olevel] [-D debugopts] [path...] [expression]`

Or more human readable:
`find [how to treat symbolic links and other options] [where to start the search] [what to find]`

The expression is typically a space separated list of `-<option> <value>`.

## Often used commands

This tool has an enourmous amount of options for every possible niche use case. However, there are a few variants I frequently use.

`find -L /path/to/start/search -type f -name "my_file.txt"`
Search for a regular file `-type f`, named `my_file.txt` in the provided path. Option `-L` means to follow symbolic links. Enclose the pattern in quotes to prevent shell expansion.

`find /path/to/start/search -perm 644`
Find all files in path with `644` permissions.

`find /path/to/start/search -user tobias`
Find all files in path owned by the user `tobias`.
