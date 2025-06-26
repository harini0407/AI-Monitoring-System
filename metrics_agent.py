import psutil
import time
import datetime
from influxdb_client import InfluxDBClient, Point, WriteOptions

# Replace with your token
token = "U4UkWBTw_N0yJomTnJG29mcfsVxKsjXa1BX0x8ixsTetG3hUlqu-UcfvBQ2AcRGQJMNMw5UzrU1RioQXG2IWvA=="
org = "Mailam Engineering College"
bucket = "system-metrics"
url = "http://localhost:8086"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=WriteOptions(batch_size=1))

def collect_and_send():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    point = Point("system_metrics") \
        .tag("host", "local") \
        .field("cpu", cpu) \
        .field("memory", memory) \
        .time(datetime.datetime.utcnow())
    write_api.write(bucket=bucket, org=org, record=point)
    print(f"[{datetime.datetime.now()}] Sent CPU: {cpu}%, Memory: {memory}%")

while True:
    collect_and_send()
    time.sleep(10)  # Every 10 seconds
