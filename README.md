# rundeck-zabbix
Simple plugin to disable or enable Zabbix monitoring of the host during publications. 
It is based on zabbix-api, that is, all client calls to the server are performed via Zabbix API, using the Python language.
Depending on your infrastructure zabbix server host can have different URLs. 


## Required libraries

[zabbix-api](https://pypi.org/project/zabbix-api/) - use the latest available version 


## Installation
To build the plugin:

```bash
zip -r zabbix-client-plugin.zip zabbix-client
```

To install plugin: 

```bash
cp zabbix-client-plugin.zip $RDECK_BASE/libext
```

