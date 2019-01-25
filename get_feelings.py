import pandas as pd

# Data source
filename = r"data\static_annotations_averaged_songs_2000_2058.csv"

df = pd.read_csv(filename)

# Remove unneccesay columns
col_info = list(enumerate(df.columns))
df.drop(columns=[col_info[i][1] for i in range(2,7)], inplace=True)

col_info = list(enumerate(df.columns))
df.drop(columns=[col_info[i][1] for i in range(3,8)], inplace=True)

# Rename columns
df.rename(columns = {' valence_mean':'valence'}, inplace = True)
df.rename(columns = {' arousal_mean':'arousal'}, inplace = True)

# Mean Normalize values
df['valence'] = df['valence'] - 5
df['arousal'] = df['arousal'] - 5

# Add a new column
Feelings = {0:"Happy", # Valence > 0 and Arousal >0 
        1: "Sad",  # Valence > 0 and Arousal < 0
        2: "Angry",  # Valence <0 and Arousal > 0
        4: "Calm"   # Valence < 0 and Arousal < 0
}
df["Feeling"] = 1
df["Feeling"] = df['valence'] > 0 & df['arousal'] > 0 
df.head()
import pdb; pdb.set_trace()