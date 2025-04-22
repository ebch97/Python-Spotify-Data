import matplotlib.pyplot as plt
from collections import (Counter)# Imports Counter, which helps count how often each item appears in a list
from datetime import datetime
import csv

track_name_list = [] # Creates an empty list to store track + artist names
with open('C:/Users/ebony/Downloads/spotify_history.csv', 'r', encoding='utf-8', errors='replace') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        for row in spreadsheet: # Loops through each row in the CSV
                track = row['track_name'] # Gets the track name from the current row
                track_name_list.append(f"{row['track_name']} - {row['artist_name']}")
                # Appends a formatted string with both track name and artist to the list

track_counts = Counter(track_name_list)
top_5 = track_counts.most_common(5)
print("My Partner's Top 5 Most Streamed Songs on Spotify:")
for track, count in top_5:
        print(f"{track}: {count} streams")

songs = [song for song, count in top_5]
counts = [count for song, count in top_5]

plt.figure(figsize=(10, 6))
plt.barh(songs[::-1], counts[::-1], color='orchid')  # Horizontal bar chart, reversed for highest at top
plt.xlabel('Play Count')
plt.title('Top 5 Most Streamed Songs')
plt.tight_layout()
plt.show()