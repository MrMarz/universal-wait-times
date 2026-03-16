import requests
import pandas as pd
from datetime import datetime
import os

URL = "https://queue-times.com/parks/64/queue_times.json"

response = requests.get(URL)
data = response.json()

timestamp = datetime.utcnow()

rows = []

for land in data["lands"]:
    for ride in land["rides"]:
        rows.append({
            "timestamp": timestamp,
            "ride": ride["name"],
            "wait_time": ride["wait_time"],
            "is_open": ride["is_open"]
        })

df = pd.DataFrame(rows)

file = "wait_times.csv"

if os.path.exists(file):
    df.to_csv(file, mode="a", header=False, index=False)
else:
    df.to_csv(file, index=False)
