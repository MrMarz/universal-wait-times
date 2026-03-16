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
df.to_csv("wait_times.csv", mode='a', header=not __import__('os').path.exists("wait_times.csv"), index=False)
