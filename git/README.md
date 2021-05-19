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

If the remote branch does not exist yet, the above command will give an error message:

```text
fatal: The current branch feature-branch has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin feature-branch
```

Solution is to add the `-u`/`--set-upstream` option:

```bash
git push -u origin feature-branch
```

This pushes the local branch to the remote, and adds the remote as the tracked branch. Forgetting the `-u` will push the local branch to the remote, but it will _not_ track it. So the next time I push, the same error message appears. Solution? Push with `-u` option, dummy.

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
