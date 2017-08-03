import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_logstash_config_file_exists(File):
    config = File('/etc/logstash/conf.d/logstash.conf')
    assert config.exists
    assert config.is_file


def test_logstash_service_is_running_and_enabled(Service):
    service = Service("logstash")
    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize("filter", [
    ("01-syslog.conf"),
    ("02-nginx.conf"),
    ("03-apache.conf"),
    ("04-beats.conf")
])
def test_logstash_filters(File, Command, filter):
    if "centos-7-logstash-grok-ready" in Command("hostname").stdout:
        filter_conf = File("/etc/logstash/conf.d/" + filter)
        assert filter_conf.is_file
