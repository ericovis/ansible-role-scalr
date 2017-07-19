Scalr
=========

This Ansible Role installs Scalr Open Source on Ubuntu

Role Variables
--------------

To change the default admin password you must change the following variable:

~~~
admin_password: Scalr
~~~

Example Playbook
----------------

~~~
- hosts: all
  roles:
     - role: ericovis.scalr
       admin_password: Password
~~~

License
-------

GPLv3

Author Information
------------------

Created by [Eric Magalhães](https://emagalha.es).
