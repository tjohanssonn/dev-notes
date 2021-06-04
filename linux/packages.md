# Packages

In Ubuntu you install packages with `apt` or the lower-level `apt-get`.

The recommended tool nowadays is `apt` if you don't require some of the specific functionality in `apt-get`.

## Using apt

### Installing

To install a package:

```bash
# Latest
apt install my-package
# Specific version
apt install my-package=x.y.z
```

### Removing

To remove a package:

```bash
apt remove my-package
```

Removing always leaves some residues (config files) in case that the removal was accidental. To restore the package to its former state, just install it again. If you really want to uninstall everything, use `purge` afterwards:

```bash
apt purge my-package
```

Note that `purge` _does not_ remove configuration files in the `$HOME` directory, e.g. `/home/tobias`.

To uninstall dependencies that were installed together with a previously installed package, use `autoremove`:

```bash
apt autoremove
```

### Updating and upgrading

Update in the world of `apt` means: "Update (download) _information_ about packages".  
It doesn't actually update any software on the computer.

Upgrade however, actually means: "Install newer version of the package/software".

So a typical update/upgrade sequence is:

```bash
# Update package information, i.e. look for updates.
apt update
# Install newer version
apt upgrade
```

### Searching for packages

```bash
apt search <regex>
```

### Listing packages

```bash
apt list [--installed|--upgradeable|--all-versions]
# or
dpkg -l
```

## To-Do

- [ ] Write a section about `dpkg`
