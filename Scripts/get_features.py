import librosa 
import glob 
import pandas as pd

filename = ('audio/2018.mp3')
path = '/Users/breanna/Downloads/MEMD_audio/*.mp3'
#path = '/Users/breanna/Documents/Classes/extract/audio/*.mp3'

def generate_DF(path):
    df = pd.DataFrame(columns=['id','bpm','chromagram'])
    
    files = glob.glob(path)
    
    for i,mp3 in enumerate(files): 
        print(mp3)
        id_ = mp3[len("/Users/breanna/Downloads/MEMD_audio/"):-4]
        tempo,chromagram = get_features(mp3)
        df.loc[i] = [id_,tempo,chromagram]
    print(df)
    return df

def get_features(mp3):
    y, sr = librosa.load(mp3)
    
    #separate harmonic and percussive wavs
    y_harmonic, y_percussive = librosa.effects.hpss(y)

    #get tempo estimation 
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr)

    #get chromagram 
    chromagram = librosa.feature.chroma_cqt(y=y_harmonic,sr=sr)

    return tempo, chromagram

    
if __name__ == '__main__': 
    generate_DF(path)
   
    '''
    y, sr = librosa.load(filename)
    
    #separate harmonic and percussive wavs
    y_harmonic, y_percussive = librosa.effects.hpss(y)

    #get tempo estimation 
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr)
    print(tempo,beat_frames)

    #get chromagram 
    chromagram = librosa.feature.chroma_cqt(y=y_harmonic,sr=sr)
    print(chromagram)    

    librosa.output.write_wav('percussive.wav',y_percussive,sr)
    librosa.output.write_wav('harmonic.wav',y_harmonic,sr)

    '''
