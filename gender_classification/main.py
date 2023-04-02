# sklearn - ml model repository
# tree - let us build a ML model called decision tree
from sklearn import tree
# it passes data through various parameters and keep placing it in tree structure and expanding it
#untill a tree appears
# then when unlabled data apperars, it passes that data through all Yes or NO question untill it lables the data

# dataset - [height, weight, shoe size]

X = [[181,80,44],[177,70,43],[160,60,38], [154,54,37],
    [166,65,40],[190,90,47],[174,64,39],[177,70,440],
    [159,55,37],[171,75,42],[181,85,43]]
# data set of 11 people

Y = ["male","female","female","female","male","male","male",'female','male','female','male']

# storing our descision tree classifier
clf = tree.DecisionTreeClassifier()

# training the classifier on our dataset
clf = clf.fit(X,Y)

# defining prediction 
prediction = clf.predict([[190,70,43]])

print(prediction)