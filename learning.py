import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from data_cleanup import feature_extraction

def main():
    # Get X and y on which we will be learning
    data = feature_extraction.get_data()
    y = data.Feeling
    X = data.drop("Feeling", axis=1)

    # We will use logistic regression as a base line
    model = LogisticRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = metrics.accuracy_score(y_test, y_pred)
    print(accuracy)

main()