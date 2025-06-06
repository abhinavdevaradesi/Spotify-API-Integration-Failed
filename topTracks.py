#library

from auth import get_spotify_client
import pandas as pd

#main

def main():
    
    #spotify authorization
    
    sp=get_spotify_client()

    #storing results

    results=sp.current_user_top_tracks(limit=20, time_range='medium_term')

    #storing into list

    tracks=[]
    for idx, item in enumerate(results['items']):
        track_info={
            'rank': idx+1,
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'album': item['album']['name'],
            'popularity': item['popularity'],
            'duration_ms': item['duration_ms'],
            'id': item['id']
        }
        tracks.append(track_info)

    #dataframe for storing and to csv

    df=pd.DataFrame(tracks)
    df.to_csv("top_spotify_tracks.csv", index=False)
    print("Top tracks saved to top_spotify_tracks.csv")

#only called if called directly not called when imported

if (__name__=='__main__'):
    main()
