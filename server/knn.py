import pandas as pd
import numpy as np

def init():
    dataset = pd.read_csv('nonbooleanfeatures.csv')
    X = dataset.iloc[:, 2:].values
    y = dataset.iloc[:, 1].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    from sklearn.neighbors import KNeighborsClassifier
    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(X, y)
    #KNeighborsClassifier(...)
    return neigh

def test(neigh, data):
    return neigh.predict(np.array([data]).reshape(1, -1))
