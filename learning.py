import pandas as pd

from sklearn import metrics
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from data_cleanup import feature_extraction


import keras
from keras.models import Sequential
from keras.layers import Input, Dense
from keras.optimizers import Adam
"""
Try SVM/Random Forests/ or fully connected NN
another baseline Naive Bayes
"""
def main():
    # Get X and y on which we will be learning
    data = feature_extraction.get_data()
    y = data.Feeling
    X = data.drop("Feeling", axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    # We will use logistic regression as a base line
    model = LogisticRegression()

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = metrics.accuracy_score(y_test, y_pred)
    print("accuracy of Logistic Regrssion =", accuracy)

    model = svm.SVC(gamma='scale', decision_function_shape='ovo')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = metrics.accuracy_score(y_test, y_pred)
    print("accuracy of multiclass SVM =", accuracy)

    model = svm.LinearSVC()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = metrics.accuracy_score(y_test, y_pred)
    print("accuracy of Linear SVM =", accuracy)

    model =  RandomForestClassifier(n_estimators=100, oob_score=True, random_state=1)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = metrics.accuracy_score(y_test, y_pred)
    print("accuracy of Random Forest =", accuracy)


    """
    vgg16_model = keras.applications.vgg16.VGG16()
    model = Sequential()
    #model.add(Input(X_test.shape))
    for layer in vgg16_model.layers[:-1]:
        model.add(layer)
    
    for layer in model.layers:
        layer.trainable = False

    model.add(Dense(4, activation="softmax"))
    import pdb; pdb.set_trace()
    model.compile(Adam(lr=0.0001), loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit(X_test, y_test, batch_size=1, epoch=20, shuffle=False, verbose=2)
    """
    
main()