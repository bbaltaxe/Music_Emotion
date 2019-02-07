Music Therapy
===========

Team: 
----
Leya Breanna Baltaxe-Admony  
Sachet Mittal  
Marco Mazzoni  

The dataset: 
-----------
We will be using the DEAM (Database for Emotional Analysis of Music) as our data set. It includes valence and arousal as well as musical features such as genre, bpm etc. for a large set of songs. These features are given discreetly (per song) and continuously (per second of song). 
Behavior of your system/ System Design:

Goal 1 - Generate Playlist:
--------------------------
Within the dataset each song has features accompanied by the “feeling” it creates (In the form of valence/ arousal ratio which we can determine feeling from).  The system will learn the feeling a new song would create.

Workflow:
--------
A user:
specifies a feeling (happy, sad, angry) 
gives a playlist
The system filters out the songs which evoke this feeling from the playlist
The output will be a subset of songs from the playlist

Goal 2 - Generate Composition (Stretch Goal):
--------------------------------------------
The system will generate a song based on the parts of the songs in the dataset to “evoke” a feeling. This goal requires analyzing specific musical features (bpm, key, voicing, etc.) and their combinations to create a piece from scratch using those features. The dataset has information on the valence/arousal per second in the song so we can see how that changes as the musical features change.

Workflow: 
--------
A user specifies:
a feeling (happy, sad, angry)
a specific genre 
The system creates short musical excerpt that meets the users expectations

Evaluation metric:
------------------
Accuracy and Recall via F1 score. 


Plans:
------
	- Feature extraction on the given dataset
	- Figure out a way to apply to extract these features on a completely new song
	- Train a simple model using Logistic Regression to evaluate a baseline and also the accuracy should be more than 100/no.of feelings %
	- Use a CNN/RNN/TCN model and learn and evaluate models.

