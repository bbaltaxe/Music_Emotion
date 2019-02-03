import pandas as pd


def main():
    # Data source
    filename = r"data\static_annotations_averaged_songs_2000_2058.csv"
    df = pd.read_csv(filename)

    # Remove unneccesay columns
    col_info = list(enumerate(df.columns))
    df.drop(columns=[col_info[i][1] for i in range(2,7)], inplace=True)  # Valence related columns

    col_info = list(enumerate(df.columns))
    df.drop(columns=[col_info[i][1] for i in range(3,8)], inplace=True)  # Arousal related columns

    # Rename columns
    df.rename(columns = {' valence_mean':'valence'}, inplace = True)
    df.rename(columns = {' arousal_mean':'arousal'}, inplace = True)

    # Mean Normalize values
    df['valence'] -= - 5
    df['arousal'] -= - 5

    def feeling_map(s):
        '''Refer: https://stackoverflow.com/questions/49586471/add-new-column-to-python-pandas-dataframe-based-on-multiple-conditions
        open to new ideas for this'''
        if s['valence'] >= 0 and s['arousal'] >= 0:
            return 0 
        if s['valence'] >= 0 and s['arousal'] < 0:
            return 1
        if s['valence'] < 0 and s['arousal'] >= 0:
            return 2 
        if s['valence'] < 0 and s['arousal'] < 0:
            return 3

    Feelings = ["Happy", # Valence > 0 and Arousal >0 
        "Calm"   # Valence > 0 and Arousal < 0
        "Angry",  # Valence <0 and Arousal > 0
        "Sad",  # Valence < 0 and Arousal < 0
    ]

    # Add a new column
    df["Feeling"] = df.apply(feeling_map, axis=1)
    print(df.head())


if __name__ == "__main__":
    main()