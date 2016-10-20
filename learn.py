from sklearn import tree
import re

# Returns feature & label arrays [ feature, label ]
def parseData(data):
	features = list()
	labels = list()
	passwords = list()

	with open(data) as f:
		for line in f:
			if line != "":

				both = line.replace('\n', '').split("|")
				password = both[0]
				label = both[1]

				feature = [0,0,0,0,0]

				# FEATURES
				lenMin = False; # more than 8 chars
				specChar = False # special character
				ucChar = False # uppercase character
				numChar = False # numeric character

				# More than 8 characters
				if len(password) > 8:
					lenMin = True

				# Special
				specialMatch = re.search(r'([^a-zA-Z0-9]+)', password, re.M)
				if specialMatch:
					specChar = True

				# Uppercase
				ucMatch = re.search(r'([A-Z])', password, re.M)
				if ucMatch:
					ucChar = True

				# Numeric
				numMatch = re.search(r'([0-9])', password, re.M)
				if numMatch:
					numChar = True

				# Create rules
				if lenMin:
					feature[0] = 1

				if specChar and ucChar and numChar:
					feature[1] = 3

				if ucChar and numChar:
					feature[2] = 1

				if specChar and numChar:
					feature[3] = 2

				if specChar and ucChar:
					feature[4] = 2

				features.append(feature)
				labels.append(int(label))
				passwords.append(password)

	return [ features,  labels, passwords]


# Prepare the data
trainingData = parseData('training.txt')
testingData = parseData('testing.txt')

# #The classifier that we're using. A simple decision tree.
clf = tree.DecisionTreeClassifier()

#Training the classifier with the passwords and their labels.
clf = clf.fit(trainingData[0], trainingData[1])

#Predicting a password Strength
prediction = clf.predict(testingData[0])

target = len(testingData[1])
current = 0

for index in range(target):
	if(prediction[index] == testingData[1][index]):
		current += 1
		print 'Correct! [Prediction: ' + str(prediction[index]) + '] [Actual: ' + str(testingData[1][index]) + '] [Password: \''+testingData[2][index]+'\']'

print ' '
print 'Result: ' + str(current) + '/' + str(target)


