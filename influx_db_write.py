import influxdb_client
import time
import random
from influxdb_client.client.write_api import SYNCHRONOUS
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

write_api = client.write_api()
count = 0
while True:
    temp = float(random.randint(0, 100))
    p = influxdb_client.Point("my_measurement").tag(
        "location", "Prague").field("temperature", temp).time(time.time_ns())
        # .tag("timestamp", str(time.time_ns()))
    if(count == 1000):
        
    write_api.write(bucket=bucket, org=org, record=p,write_precision='ns')
    print("wrote temp", temp)
    time.sleep(.2)
