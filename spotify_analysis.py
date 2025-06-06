import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    df=pd.read_csv(file_path)
    return df

def explore_data(df):
    print("===DATA INFO===") #for columns, datatypes, memory use
    print(df.info())
    print("===DATA HEAD===") #for peeking top 5 data rows
    print(df.head())
    print("===DESCRIPTIVE STATISTICS===") #for stats like mean, max, avg
    print(df.describe())
    print("===MISSING VALUES===") #counts number of missing values
    print(df.isnull().sum())

def visualize_top_artists(df):
    top_artists=df['artist'].value_counts().head(10) #return top 10 artists with number of tracks
    sns.barplot(x=top_artists.values, y=top_artists.index)
    plt.title("Top 10 Artists in your Top Tracks")
    plt.xlabel("Number of Tracks")
    plt.ylabel("Artist")
    plt.tight_layout()
    plt.show()

def visualize_popularity_distribution(df):
    sns.histplot(df['popularity'], bins=10, kde=True) #divide data into 10 bins which is 10 groups and kde adds a smooth curve to the plot
    plt.title("Popularity Distribution")
    plt.xlabel("Popularity Score")
    plt.tight_layout()
    plt.show()

def main():
    file_path='top_spotify_tracks.csv'
    df=load_data(file_path)
    explore_data(df)
    visualize_top_artists(df)
    visualize_popularity_distribution(df)

if __name__=='__main__':
    main()
