# Special variables in Ansible

There's lots of special variables that can be accessed during tasks. Unfortunately they are littered across the documentation, so I'll list some of the common ones.

## List of special variables

`hostvars` contains information for any host in the play at any point in the playbook.

`groups` contains a list of all the groups, and hosts in each group, in the inventory.

`group_names` contains a list of all the groups the current host is in.

`inventory_hostname` contains the name of the current host.

## hostvars

`hostvars` contains all facts/variables on all hosts. It is structured as `hostvars["hostname"]["my-variable"]`. If the play has gathered facts on all hosts, these are accessible via `hostvars["hostname"]["ansible_facts"]`.

A typical construct is for example to loop through hosts not targeted by the current play, e.g.

```yaml
- debug:
    msg: "{{ hostvars[item]["an-interesting-variable"] }}"
  loop: "{{ groups["another-group"] }}
```

## Resources

- <https://docs.ansible.com/ansible/latest/user_guide/playbooks_vars_facts.html>
