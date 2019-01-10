import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import f1_score

# Importing the dataset
dataset = pd.read_csv('nonbooleanfeatures.csv')
X = dataset.iloc[:, 2:].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.5, max_depth=1, random_state=0).fit(X_train, y_train)
score = clf.score(X_test, y_test)

featuresImp = clf.feature_importances_
headers = ["top1Sim","top2Sim","top3Sim","top4Sim","top5Sim","numberOfTitle","numberOfBody","numberOfCap","numberOfAcronym","isExclm","numberOfExclm","isQues","numberOfQues","isStartNum","hasNumber",
           "isSuperlative","isQuote","numberOfQuote","isStart5W1H","isNeg","numberOfNeg","isPos","numberOfPos","isBaity","numberOfBaity","hasParenthesis","hasMoney","avgWordSent","isForwardReference",
           "numberOfForwardReference","CLScore","rixScore","lixScore","formalityMeasure"]



result = clf.predict(X_test)
f1 = f1_score(y_test, result, average='weighted')
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


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def saveHistogram(data, name, save):
    n, bins, patches = plt.hist(x=data, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title(name)
    plt.text(23, 45, r'$\mu=15, b=3$')
    maxfreq = n.max()
    # Set a clean upper y-axis limit.
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    if save:
        plt.savefig(name)
    else:
        plt.show()
    plt.cla()
    plt.clf()

#saveHistogram(asd, "qwe", False)
#saveHistogram(asd, "qwe", False)

def graph(feature_importance):
    import matplotlib.pyplot as plt
    feature_importance = 100.0 * (feature_importance / feature_importance.max())
    sorted_idx = pd.np.argsort(feature_importance)
    pos = pd.np.arange(sorted_idx.shape[0]) + .5
    plt.subplot(1, 2, 2)
    plt.barh(pos, feature_importance[sorted_idx], align='center')
    plt.yticks(pos, sorted_idx)
    plt.xlabel('Relative Importance')
    plt.title('Variable Importance')
    plt.show()


#graph(clf.feature_importances_)
