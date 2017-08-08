Logstash 5.x
=========

[![Build Status](https://travis-ci.org/tonyganga/ansible-logstash.svg?branch=master)](https://travis-ci.org/tonyganga/ansible-logstash)

This role will install and configure Logstash 5.x tailored to consumer/produce to RabbitMQ.

Supported Platforms
-------------------

This role has been tested on CentOS 7.

Requirements
------------

The role has been tested with the following on Mac and Linux.

* [Docker](https://www.docker.com/) >= 17.06.0-ce
* [Molecule](https://github.com/metacloud/molecule) >= 1.25.0
* [Ansible](https://www.ansible.com/) >= 2.3.1.0

Dependencies
------------

* [EPEL](https://galaxy.ansible.com/geerlingguy/repo-epel/)
* [Java](https://galaxy.ansible.com/geerlingguy/java/)

Role Variables
--------------

```yaml
---
logstash_listen_port_beats: 5044

logstash_elasticsearch_hosts:
  - http://my_elasticsearch.domain.com

logstash_local_syslog_path: /var/log/syslog
logstash_monitor_local_syslog: true
logstash_ssl_dir: /etc/pki/logstash
logstash_ssl_certificate_file: ""
logstash_ssl_key_file: ""
logstash_enabled_on_boot: yes

logstash_install_plugins:
  - logstash-input-beats
  - logstash-input-rabbitmq
  - logstash-output-rabbitmq
  - logstash-output-elasticsearch

rabbitmq_hostname: rabbit.domain.com
rabbitmq_username: logstash
rabbitmq_password: sekretpw
rabbitmq_vhost: logstash
rabbitmq_port: 5672
rabbitmq_durable: true
rabbitmq_ack: true
rabbitmq_prefetch_count: 50
```

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - geerlingguy.java
    - geerlingguy.repo-epel
    - ansible-logstash
  vars:
    java_packages: java-1.7.0-openjdk

```

Tests
-----

Use molecule to run tests.

```bash
molecule test
```
