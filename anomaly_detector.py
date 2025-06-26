import datetime
import time
import pandas as pd
from influxdb_client import InfluxDBClient, Point, WriteOptions
from sklearn.ensemble import IsolationForest
import os

# Setup CSV Log Path (for local file fallback)
log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "anomalies_log.csv")
if not os.path.exists(log_file):
    pd.DataFrame(columns=["cpu", "memory", "_time", "anomaly"]).to_csv(log_file, index=False)

# InfluxDB Setup
bucket = "system-metrics"
org = ""
token = ""
url = ""

client = InfluxDBClient(url=url, token=token, org=org)
query_api = client.query_api()
write_api = client.write_api(write_options=WriteOptions(batch_size=1))

def fetch_metrics():
    query = f'''
    from(bucket: "{bucket}")
      |> range(start: -30m)
      |> filter(fn: (r) => r._measurement == "system_metrics")
      |> filter(fn: (r) => r._field == "cpu" or r._field == "memory")
      |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
      |> keep(columns: ["_time", "cpu", "memory"])
    '''
    tables = query_api.query_data_frame(org=org, query=query)
    if isinstance(tables, list):
        df = pd.concat(tables)
    else:
        df = tables
    return df

def detect_anomalies(df):
    model = IsolationForest(contamination=0.1)
    X = df[['cpu', 'memory']]
    df['anomaly'] = model.fit_predict(X)
    return df

while True:
    print(f"[{datetime.datetime.now()}] 🔍 Checking for anomalies...")
    try:
        df = fetch_metrics()
        if df.empty or len(df) < 10:
            print("📫 Not enough data yet...")
        else:
            df = detect_anomalies(df)
            anomalies = df[df['anomaly'] == -1]
            if not anomalies.empty:
                print("🚨 Anomaly detected!")
                print(anomalies[['cpu', 'memory', '_time']].tail())

                # Write to InfluxDB instead of CSV
                for _, row in anomalies.iterrows():
                    point = Point("anomaly_events") \
                        .tag("host", "local") \
                        .field("cpu", row['cpu']) \
                        .field("memory", row['memory']) \
                        .time(row['_time'])
                    write_api.write(bucket=bucket, org=org, record=point)
                print("🚨 Anomaly written to InfluxDB under 'anomaly_events'.")

            else:
                print("✅ All systems normal.")
    except Exception as e:
        print(f"❌ Error: {e}")
    time.sleep(30)
