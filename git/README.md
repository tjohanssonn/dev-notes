# Git

A little cheat-sheet of the most common operations I do when working with Git.

## Branch and checkout

```bash
git branch <branch>
git branch feature-branch # Create branch
git checkout feature-branch # Switch to branch
```

A more convenient way is to create the branch directly when switching with the `-b` option:

```bash
git checkout -b feature-branch # Creates and switches branch in one command
```

## Push

```bash
git push [options] <remote> <branch>
git push origin feature-branch
```

Shorthand to push the current branch to the tracked branch on origin:

```bash
git push
```

If the remote branch does not exist yet, the `-u`/`--set-upstream` option must be used:

```bash
git push -u origin feature-branch
```

This pushes your local branch to the remote, and adds the remote as the tracked branch.

If I want to name my remote branch the same as my local branch, a shorthand is:

```shell
git push -u origin HEAD
```

## Moving uncommitted work to another branch

Did you just make changes in `master`? Well, as long as you didn't commit them you can probably just switch branch with `git checkout [-b] other-branch`. The changes will follow as long as `git` doesn't detect a conflicting change in the branch you switch to.

If there is a conflicting change that prevents you from switching branch, one way to solve it is to:

```shell
git stash
git checkout other-branch
git stash pop
```
