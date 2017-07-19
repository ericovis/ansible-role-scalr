Scalr
=========

This Ansible Role installs Scalr Open Source on Ubuntu

Role Variables
--------------

The default values are described in the **defaults/main.yml** file.

To change the default admin password you must change the following variable:
~~~
admin_password: Scalr
~~~

To install Scalr from a different repo (For example to install enterprise Scalr) set the url in this variable:
~~~
deb_source_repo: https://packagecloud.io/install/repositories/scalr/scalr-server-oss/script.deb
~~~

To set a custom endpoint host set this variable:
~~~
endpoint_host: "{{ inventory_hostname }}"
~~~

In order to install Azure's credentials during setup you need to define the following variables:

~~~
setup_azure: true
azure_client_id: your-id
azure_secret_key: your-secret-key
~~~


Example Playbook
----------------

~~~
- hosts: all
  roles:
     - role: ericovis.scalr
~~~

License
-------

GPLv3

Author Information
------------------

Created by [Eric Magalhães](https://emagalha.es).
