# systemd

Does a lot of things, but the main purpose is to manage services and their configuration.

## System and user services

`systemd` differentiates _system_ and _user_ services.

System services can only started, stopped and modified by an administrator with `sudo` privilege.

User services runs in the context of a user, and can be started, stopped and modified by that user.

## systemctl

Command used to control the state of `systemd`.

`systemctl status my.service`: Print status of service
`systemctl enable my.service`: Enable service to start at boot
`systemctl daemon-reload`: Reloads daemon. Required after a unit file was edited.

## Configuration

All configuration of services is done in configuration files called _unit files_. Some of the most common types are:

- `.service`
- `.path`
- `.target`

`.service` files defines the service, such as executable to run, service run-time behaviour (simple, fork, one-shot ...) restart behaviour, user to run the executable as, etc.

`.path` files are used to monitor paths on the system. Can for example be used to trigger a service when a file changes.

## Paths

Unit files are loaded from several paths. If running the system-wide `systemd`:

- `/etc/systemd/system`
- `/run/systemd/system`
- `/usr/lib/systemd/system`

If creating system services manually, they shall be put in `/etc/systemd/system`. The other paths I've never touched.

For more info on paths, see the [man pages](https://www.freedesktop.org/software/systemd/man/systemd.unit.html#Unit%20File%20Load%20Path).
