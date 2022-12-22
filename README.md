Prtg-sensor
===========
Simple data generator for advanced PRTG sensors.

It will help you to generate output in JSON format for the Python Script Advanced, EXE/Script Advanced, SSH Script Advanced and HTTP Data Advanced sensors. 

You can refer to the [official PRTG manual](https://www.paessler.com/manuals/prtg/custom_sensors) to figuring out all the features of custom sensors.

Installing
===========
Install with `pip`
```sh
pip install prtg-sensor
```

Example
===========
Executable sensors like `Python Script Advanced sensor` must send the result to the stdout. `HTTP Data Advanced sensor` must send the result in the http response body.


```python
from prtg_sensor import Sensor

sensor = Sensor()
sensor.add_channel('Duration', 32, unit='timeseconds')
sensor.add_channel('Loading', 12.55, unit='percent', float=1, decimal_mode='all')
sensor.add_channel('Status', 0, value_lookup='prtg.standardlookups.aws.status')
sensor.text = 'Everything is ok'
print(sensor.get_result())
```

PRTG interprets this result to sensor by itself

![Sensor screenshot](https://github.com/maymon-max/prtg-sensor/raw/main/imgs/sensor_screenshot.png)