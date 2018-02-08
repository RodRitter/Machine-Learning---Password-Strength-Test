from sklearn import tree
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import re

def makeTokens(f):
    tokens = []
    for i in f:
        tokens.append(i)
    return tokens

def parseFile(file):
    featureList = list()
    labelList = list()
    with(open(file)) as f:
        for line in f:
            feat = line.replace('\n', '').split('|')

            # labels
            feat[1] = int(feat[1])
            labelList.append(feat[1])

            # features
            featureList.append(feat[0])

    return [featureList, labelList]

trainingData = parseFile('training.txt')

#labels
y = trainingData[1]

# features
allFeatures = trainingData[0]
vectorizer = TfidfVectorizer(tokenizer=makeTokens)
X = vectorizer.fit_transform(allFeatures)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)


# fit
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

# predict
X_predict = ['eUj+v']
X_predict = vectorizer.transform(X_predict)
prediction = clf.predict(X_predict)
print(prediction)
