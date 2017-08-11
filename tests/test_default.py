import testinfra.utils.ansible_runner
import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_logstash_service_is_running_and_enabled(Service):
    service = Service("logstash")
    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize("filter_conf", [
    ("01-syslog.conf"),
    ("02-nginx.conf"),
    ("03-apache.conf"),
    ("04-beats.conf")
])
def test_logstash_filters(File, Command, filter_conf):
    if "centos-7-logstash-grok-ready" in Command("hostname").stdout:
        conf = File("/etc/logstash/conf.d/" + filter_conf)
        assert conf.is_file


def test_logstash_configs(File, Command):
    if "centos-7-logstash-shipper" in Command("hostname").stdout:
        config = File('/etc/logstash/conf.d/shipper.conf')
        assert config.exists
        assert config.is_file

    elif "centos-7-logstash-raw-log" in Command("hostname").stdout:
        config = File('/etc/logstash/conf.d/raw-log.conf')
        assert config.exists
        assert config.is_file

    elif "centos-7-logstash-grok-ready" in Command("hostname").stdout:
        config = File('/etc/logstash/conf.d/grok-ready.conf')
        assert config.exists
        assert config.is_file

    elif "centos-7-logstash-grok-complete" in Command("hostname").stdout:
        config = File('/etc/logstash/conf.d/grok-complete.conf')
        assert config.exists
        assert config.is_file
