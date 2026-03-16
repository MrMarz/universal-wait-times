import requests
import pandas as pd
from datetime import datetime

parks = {
    "Islands of Adventure": "https://queue-times.com/parks/64/queue_times.json",
    "Universal Studios Florida": "https://queue-times.com/parks/65/queue_times.json",
    "Epic Universe": "https://queue-times.com/parks/334/queue_times.json"
}

timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
rows = []

for park_name, url in parks.items():
    response = requests.get(url)
    data = response.json()
    for land in data.get("lands", []):
        for ride in land.get("rides", []):
            if ride.get("is_open"):  # only log open rides
                rows.append({
                    "timestamp": timestamp,
                    "park": park_name,
                    "ride": ride.get("name"),
                    "wait_time": ride.get("wait_time"),
                    "is_open": ride.get("is_open")
                })

if not rows:
    print("No open rides, skipping.")
    exit()

df = pd.DataFrame(rows)

date_str = datetime.utcnow().strftime("%Y-%m-%d")
filename = f"data/wait_times_{date_str}.csv"

import os
os.makedirs("data", exist_ok=True)
df.to_csv(filename, mode='a', header=not os.path.exists(filename), index=False)
