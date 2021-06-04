# SSH

There's lots of things to know about SSH. These are the first notes about it. If this text becomes too long, create its own directory.

These notes only contain the most common commands that I use.

## Configuration

Configuration is split in two parts; server and client.

Server configuration is done in `/etc/ssh/sshd_config`.

Client configuration is obtained from multiple sources in the following order:

1. command-line options
2. user's configuration in `~/.ssh/config`
3. system-wide configuration in `/etc/ssh/ssh_config`

## Tools/utilities

### ssh-keygen

#### Finding entry for a known hostname

```bash
ssh-keygen [-H] -F [hostname|IP]
```

Adding the `-H` option removes the hostname information if the entry has been hashed.

#### Remove entries in known hosts

To remove all keys belonging to a hostname:

```bash
ssh-keygen -R [hostname|IP]
```

### ssh-keyscan

Utility to collect public SSH host keys. Typically used when adding SSH keys to `known_hosts`.

To collect the default keys from a host:

```bash
ssh-keyscan [-H] [hostname|IP] >> ~/.ssh/known_hosts
```

Option `-H` hashes the identifiable information (hostname) so the host cannot be identified if the contents would leak.

To only collect a specific type of key, use `-t` option:

```bash
# Only collect RSA and ED25519 keys
ssh-keyscan -t rsa,ed25519 [hostname|IP] >> ~/.ssh/known_hosts
```

### ssh-copy-id

Utility to copy public keys to a remote machine. By default it adds the keys by appending them to the remote user's `~/.ssh/authorized_keys`.

```bash
ssh-copy-id [-i identity_file] user@hostname
```

If not providing the `-i` option, it defaults to the _newest_ file matching `~/.ssh/id*.pub`.

### ssh-agent

_TBD_
