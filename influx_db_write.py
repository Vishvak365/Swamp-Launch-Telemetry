import influxdb_client
from influxdb_client import InfluxDBClient, Point, WritePrecision
import random
import time
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime

import serial
ser = serial.Serial('/dev/cu.usbserial-110', 9600)

bucket = "vishvak1"
org = "vishvak1"
# Token not a secret - only access on local
token = "nyEO6OM0nUBpGdZsJtneUGlEtO2DQknvb7yt9fWBMoa2cuAcqmOIL_nYcE6n6t1IqlL1HeOCgNMRbDVNU-ptVg=="
# Store the URL of your InfluxDB instance
url = "http://localhost:8086"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)
write_api = client.write_api(write_options=SYNCHRONOUS)
while True:
    data = str(ser.readline())[2:][:-5].split(':')
    try:
        point = Point("sensor_data").tag('sensor', data[0].strip()).field(
            "value", float(data[1].strip())).time(datetime.utcnow(), WritePrecision.NS)
        print(data)
        write_api.write(bucket, org, point)
    except:
        print("Error:", data)
