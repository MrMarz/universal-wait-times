import pandas as pd
import glob
import os

# Specify the rides you want to analyze
rides_to_track = [
    "Jurassic Park River Adventureâ„¢",
    "Jurassic World VelociCoaster",
    "Skull Island: Reign of Kongâ„¢",
    "Doctor Doom's FearfallÂ®",
    "The Amazing Adventures of Spider-ManÂ®",
    "The Incredible Hulk CoasterÂ®",
    "The Cat in The Hatâ„¢",
    "Hagrid's Magical Creatures Motorbike Adventureâ„¢",
    "Hogwartsâ„¢ Express - Hogsmeadeâ„¢ Station",
    "Popeye & Bluto's Bilge-Rat BargesÂ®",
    "Despicable Me Minion Mayhemâ„¢",
    "Revenge of the Mummyâ„¢",
    "Hollywood Rip Ride Rockitâ„¢",
    "Harry Potter and the Escape from Gringottsâ„¢",
    "Curse of the Werewolf",
    "Monsters Unchained: The Frankenstein Experiment",
    "Dragon Racer's Rally",
    "Hiccup Wing Glider",
    "Meet Toothless and Friends",
    "Bowser Jr. Challenge",
    "Mario Kartâ„¢: Bowser's Challenge",
    "The Wizarding World of Harry Potter — Ministry of Magic"
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
