# Network

## Useful tools

`route`: list the IP routing table

```shell
$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref     Use Iface
0.0.0.0         192.168.1.254   255.255.255.255 U     0      0        0 eth0
192.168.1.0     0.0.0.0         255.255.255.0   U     256    0        0 eth0
```

`ip`: list network interfaces and related information such as IP, MAC etc.
`nslookup`: retrieve DNS information from the configured nameserver

## DNS

The old way to edit the DNS resolving was to manually edit `/etc/resolv.conf`.

However, this file is nowadays controlled by `systemd-resolved`. To view nameservers, type `systemd-resolve --status` to view the uplink nameservers.

If you want to configure the nameservers, use `netplan` instead.

## Netplan

Link to webpage: [netplan.io](https://netplan.io)

Netplan is a utility for easily configuring networking on a linux system, using YAML templates.

```shell
$ cat /etc/netplan/my-config.yml
---
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
        addresses:
        - 192.168.0.10/24
    eth1:
        dhcp4: true
```

`netplan generate`: generate the required configuration for the renderer
`netplan apply`: apply the new configuration
`netplan try`: test to apply new configuration. Waits for user input, and if timeout, reverts the changes.

**Warning:** If incorrectly configured, `netplan apply` will make you lose connection to the target machine if connecting through ssh! Use `netplan try` first.
