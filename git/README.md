# Git <!-- omit in toc -->

A little cheat-sheet of the most common operations I do when working with Git.

- [Branch and checkout](#branch-and-checkout)
- [Push](#push)
- [Moving uncommitted work to another branch](#moving-uncommitted-work-to-another-branch)
- [Remote](#remote)
  - [Listing remotes](#listing-remotes)
  - [Adding a remote](#adding-a-remote)
  - [Updating remote url](#updating-remote-url)
- [Change author of last commit](#change-author-of-last-commit)
- ["Scratching my head" warnings/errors](#scratching-my-head-warningserrors)
  - [Warning when deleting a local branch](#warning-when-deleting-a-local-branch)

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

## Remote

### Listing remotes

To list all remotes that have been added to the current local repo:

```bash
$ git remote -v
origin  https://github.com/tjohanssonn/dev-notes.git (fetch)
origin  https://github.com/tjohanssonn/dev-notes.git (push)
```

### Adding a remote

To add a new remote repository named `origin`:

```bash
git remote add origin https://github.com/user/repo.git
```

### Updating remote url

Sometimes you wanna rename a project. This breaks the local repos connection to the remote as the URL changes.

To update `origin` to the new remote URL:

```bash
git remote set-url origin https://github.com/user/new-repo.git
```

## Change author of last commit

I often forget to set the "....@users.noreply.github.com" on the few repos I push to my personal Github. If a commit has been made with an incorrect email I can't push, 'cause Github complains that I will expose my private email.

To change author/email on _the last commit_, there's an easy fix:

```bash
# Change email to the correct one
git config user.email ".....@users.noreply.github.com"
# Amend the last commit
git commit --amend --reset-author --no-edit
```

## "Scratching my head" warnings/errors

### Warning when deleting a local branch

```text
git branch -d old_branch
warning: deleting branch 'old_branch' that has been merged to 'refs/remotes/origin/old_branch', but not yet merged to HEAD.
```

Huh?

In plain text:  
This means that the local branch `old_branch` _is_ up to date with its remote `origin/old_branch`, but it _is not_ merged to the current local branch (i.e. `HEAD`, which is probably `master`).

This may be the case, but probably this warning pops up after a merge/rebase has been made in the GUI in Gitlab or Github.

Such an action may either add commits or change the SHA of existing commits, causing `git` to view the original SHA's in the local `old_branch` as different from the ones in `HEAD` (who received the changed SHA's during `git pull`).

[See this Stackoverflow for more info](https://stackoverflow.com/questions/12147360/git-branch-d-gives-warning/12147447).
