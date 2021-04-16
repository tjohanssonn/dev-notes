# Auto login

Run command `systemctl edit getty@tty1`

Paste this into the file and save:

```text
[Service]
ExecStart=
ExecStart=-/sbin/agetty --skip-login --nonewline --noissue --autologin {{ user }} --noclear %I $TERM
Type=simple
```

This will override the default `getty@tty1` service by creating an override configuration at `/etc/systemd/system/getty@tty1.service.d/override.conf`
