"""
Cleans the dataset so that it can be used for machine learning algorithms
"""
import pandas as pd
import pdb

def get_genres(filename):
    #importing the dataset
    dataset = pd.read_csv(filename).fillna(" ")

    # take all the lines and all the columns except for the last one
    X = dataset.iloc[:, 0:5]  #.value
    #data_X = pd.DataFrame(X)

    # Split the genres except for Hip-Hop using a RegEx
    splitted = X["Genre"].str.split("-(?!Ho)", n = 15, expand = True)

    # Select the unique genres after the splitted table
    genres = splitted.apply(pd.value_counts)
    genres['genre'] = genres.index

    # Create a dictionary with the different genres
    # and for each genre append a column to the dataset
    dict = {}

    for key, val in enumerate(genres['genre']):
        dict[key] = val
        X[val] = pd.Series(0, index=X.index)
        
    def find_values(gen):
        tempCol = []

        for cell in X['Genre']:
            if cell.find(gen) != -1:
                tempCol.append(1)
            else:
                tempCol.append(0)
        return tempCol
    for gen in dict.values():
        tempCol = find_values(gen)
        X.loc[:, gen] = tempCol
    
    X.drop(columns=["title", "artist", "album", "Genre"], inplace=True)

    return X


def get_specteral_data(filename):
    """
    This file takes a large number of csvs. 
    The output is a csv where each row is the columnwise average of each input csv 
    """
    df =  pd.read_csv(filename)
    df.rename(columns={"Unnamed: 0": "song_id"}, inplace=True)
    return df

def get_feelings(filename):
    """
    Parses the file and gets the mapping of songid and feeling
    returns: Pandas DataFrame
    """
    df = pd.read_csv(filename)
     # Remove unneccesay columns
    col_info = list(enumerate(df.columns))
    
    valence_columns_to_remove = [x for x in col_info if "valence" in x[1] and x[1]!= " valence_mean"]
    df.drop(columns=[x[1] for x in valence_columns_to_remove], inplace=True)  # Valence related columns

    arousal_columns_to_remove =  [x for x in col_info if "arousal" in x[1] and x[1]!= " arousal_mean"]
    df.drop(columns=[x[1] for x in arousal_columns_to_remove], inplace=True)  # Arousal related columns

    # Rename columns
    df.rename(columns = {' valence_mean':'valence'}, inplace = True)
    df.rename(columns = {' arousal_mean':'arousal'}, inplace = True)

    # Mean Normalize values
    df['valence'] -= 5
    df['arousal'] -= 5
    #pdb.set_trace()

    def feeling_map(s):
        """Refer: https://stackoverflow.com/questions/49586471/add-new-column-to-python-pandas-dataframe-based-on-multiple-conditions
        open to new ideas for this
        Feelings:
        "Happy", # Valence > 0 and Arousal >0 
        "Calm",   # Valence > 0 and Arousal < 0
        "Angry",  # Valence <0 and Arousal > 0
        "Sad",  # Valence < 0 and Arousal < 0
        ]
        """
        if s['valence'] >= 0 and s['arousal'] >= 0:
            return 0 
        if s['valence'] >= 0 and s['arousal'] < 0:
            return 1
        if s['valence'] < 0 and s['arousal'] >= 0:
            return 2 
        if s['valence'] < 0 and s['arousal'] < 0:
            return 3

    # Add a new column
    df["Feeling"] = df.apply(feeling_map, axis=1)

    # Remove the Arousal and Feeling values
    df.drop(columns=["valence", "arousal"], inplace=True) 
    return df

def get_data():
    """
    Parses data from the csv files and returns a dataframe which can be used for ML algorithms
    """
    files_feelings = ["data\static_annotations_averaged_songs_1_2000.csv","data\static_annotations_averaged_songs_2000_2058.csv"]
    feeling_data = []
    for file in  files_feelings:
        feeling_data.append(get_feelings(file))
    df_1 = pd.concat(feeling_data)

    specteral_data_file = "data\specteral_data.csv"
    df_2 = get_specteral_data(specteral_data_file) 

    genre_files = ["data\metadata_2013.csv", "data\metadata_2014.csv","data\metadata_2015.csv"]
    
    genre_data = []
    for file in genre_files:
        genre_data.append(get_genres(file))
    df_3 = pd.concat(genre_data, sort=True ) 
    df_3.fillna(0, inplace=True)
    df_3[df_3.columns] = df_3[df_3.columns].astype(int)

    df = pd.merge(pd.merge(df_2, df_3, on="song_id"), df_1, on="song_id")
    return df
get_data()
