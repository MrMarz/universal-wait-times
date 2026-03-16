import requests
import pandas as pd
from datetime import datetime
import os

parks = {
    "Islands of Adventure": "https://queue-times.com/parks/64/queue_times.json",
    "Universal Studios Florida": "https://queue-times.com/parks/65/queue_times.json",
    "Epic Universe": "https://queue-times.com/parks/83/queue_times.json"
}

timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

rows = []

for park, url in parks.items():

    response = requests.get(url)
    data = response.json()

    for land in data.get("lands", []):
        for ride in land.get("rides", []):

            rows.append({
                "timestamp": timestamp,
                "park": park,
                "ride": ride.get("name"),
                "wait_time": ride.get("wait_time"),
                "is_open": ride.get("is_open")
            })

df = pd.DataFrame(rows)

file = "wait_times.csv"

if os.path.exists(file):
    df.to_csv(file, mode="a", header=False, index=False)
else:
    df.to_csv(file, index=False)
