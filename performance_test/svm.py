import pandas as pd
from sklearn import svm
from sklearn.metrics import f1_score

# Importing the dataset
from sklearn.svm import SVC

dataset = pd.read_csv('nonbooleanfeatures.csv')
X = dataset.iloc[:, 2:].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

clf = svm.SVC(gamma='scale', decision_function_shape='ovo')
clf.fit(X_train, y_train)
score = clf.score(X_test, y_test)
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovo', degree=3, gamma='scale', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

result = clf.predict(X_test)
f1 = f1_score(y_test, result, average='micro')
d = 0
yan = 0
for i in range (0, len(result)):
    if result[i] > 0.5:
        a = 1
    else:
        a = 0
    if a == y_test[i]:
        d += 1
    else:
        yan += 1
print("score:", score)
print("f1 score:", f1)
print(d)
print(yan)
