import pandas as pd
import time
from auth import get_spotify_client

# Get authorized Spotify client
sp = get_spotify_client()

# Read top tracks CSV
df = pd.read_csv('top_spotify_tracks.csv')

# Confirm 'id' column exists
if 'id' not in df.columns:
    raise Exception("Column 'id' not found in CSV.")

# Extract all track IDs
track_ids = df['id'].dropna().tolist()

# Helper to split into safe chunks
def chunk(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

# Store all feature data
all_features = []

# Chunk + delay to avoid 403
for batch in chunk(track_ids, 50):  # safer than 100
    try:
        features = sp.audio_features(batch)
        features = [f for f in features if f is not None]
        all_features.extend(features)
        time.sleep(1.2)  # avoid getting rate-limited
    except Exception as e:
        print("❌ Error with batch:")
        print(batch)
        print("Error:", e)

# Convert to DataFrame
features_df = pd.DataFrame(all_features)

# Merge original data with audio features using 'id'
merged_df = df.merge(features_df, on='id')

# Save to CSV
merged_df.to_csv('spotify_audio_features.csv', index=False)
print("✅ Audio features saved to spotify_audio_features.csv")
