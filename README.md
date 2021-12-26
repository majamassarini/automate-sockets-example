automate-home sockets example project
=====================================

An example project for the [automate-home project](https://github.com/majamassarini/automate-home).

A collection of files which define automation rules for different sockets **Appliances**.

- [socket.presence.Appliance](https://automate-home.readthedocs.io/en/latest/appliances.html#socket-presence-appliance)
- [socket.presence.christmas.Appliance](https://automate-home.readthedocs.io/en/latest/appliances.html#socket-presence-christmas-appliance)
- [socket.energy_guard.Appliance](https://automate-home.readthedocs.io/en/latest/appliances.html#socket-energy-guard-appliance)

Every *Appliance* automates a device, through a *Performer*.
The automated devices are **KNX** switches.

To automate the sockets three sensors, other than the buttons, are used:

- [sensor.powermeter.Appliance](https://automate-home.readthedocs.io/en/latest/appliances.html#sensor-powermeter-appliance); data come from a **KNX** sensor.
- [sensor.luxmeter.Appliance](https://automate-home.readthedocs.io/en/latest/appliances.html#sensor-luxmeter-appliance); data come from a **KNX** sensor.
- [sensor.alarm.Appliance](https://automate-home.readthedocs.io/en/latest/appliances.html#sensor-alarm-appliance); data come from **KNX**.

## Run automate-home docker container using this project files

```shell
export AUTOMATE_HOME_CONFIGURATION=`pwd`
export NETWORK_NAME='qnet-static-eth0-a7611e'
export IP='172.31.10.248'

docker run -dit --privileged --name sockets --network $NETWORK_NAME --ip $IP -p 8181:8181 -v graphite-sockets:/opt/graphite/storage -v redis-sockets:/var/lib/redis -v "$AUTOMATE_HOME_CONFIGURATION:/etc/automate-home" -t majamassarini/automate-home:latest
docker exec -it lights /bin/bash
```

## UI

[GUI example](https://majamassarini.github.io/automate-sockets-example/pages/172.31.10.248/index.html)
