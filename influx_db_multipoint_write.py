from influxdb import InfluxDBClient
import time
# client = InfluxDBClient('localhost', 8086, 'vishvak1', 'vishvak1', 'vishvak1')
client = InfluxDBClient('localhost', 8086, 'vishvak1', 'vishvak1', 'vishvak1')

print(time.time_ns())
json_body = [
    {
        "measurement": "cpu_load_short",
        "time": time.time_ns(),
        "fields": {
            "value": 0.64
        }
    }
]
client.write_points(json_body)
