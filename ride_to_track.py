import pandas as pd
import glob
import os

# Specify the rides you want to analyze
rides_to_track = [
    "Hagrid's Magical Creatures Motorbike Adventure",
    "Velocicoaster",
    "Hollywood Rip Ride Rockit"
]

# Load all daily CSVs
all_files = glob.glob("data/wait_times_*.csv")
df = pd.concat([pd.read_csv(f) for f in all_files])

# Filter to only the rides you want
df = df[df["ride"].isin(rides_to_track)]

# Pivot so each ride is a column, timestamp is the row
pivot = df.pivot_table(index="timestamp", columns="ride", values="wait_time")

pivot.to_csv("ride_analysis.csv")
print("Saved to ride_analysis.csv")
