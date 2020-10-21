from zabbix_api import ZabbixAPI
import ssl
import os
import sys


def get_zabbix_server(hostname):
    """Get Zabbix server hostname based on location of the host"""

    zabbix_server = "toronto.domain.com"

    if hostname[:3] == 'van':
        zabbix_server = 'vancouver.domain.com'
    elif hostname[:3] == 'ber':
        zabbix_server = 'berlin.domain.com'
    elif hostname[:3] == 'tok':
        zabbix_server = 'tokyo.domain.com'

    return zabbix_server


def update_host(hostname, status):
    """Enable or disable monitoring for the host"""

    # Suppress SSL Verification check
    ssl._create_default_https_context = ssl._create_unverified_context

    server = "https://" + get_zabbix_server(hostname)
    zapi = ZabbixAPI(server)

    # Disable SSL certificate verification
    zapi.session.verify = False

    username = os.getenv("RD_CONFIG_USERNAME")
    password = os.getenv("RD_CONFIG_PASSWORD")

    # Specify a timeout (in seconds)
    zapi.timeout = 5
    zapi.login(username, password)

    try:
        hostid = zapi.host.get({"output": ["hostid"],
                                "filter": {"host": [hostname]}})[0]['hostid']
    except Exception as e:
        exit(1)
    try:
        zapi.host.update({"hostid": hostid,
                          "status": status})
    except Exception as e:
        print(e)
        exit(1)


def main():
    if len(sys.argv) != 2:
        print(sys.argv[0], "<host> (Parameter missing)")
        sys.exit(3)

    if os.getenv("RD_CONFIG_STATE") == "enabled":
        status = 0
    else:
        status = 1

    try:
        update_host(sys.argv[1], status)
    except OSError as e:
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    main()