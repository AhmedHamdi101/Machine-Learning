from sklearn import svm
from sklearn import tree
from TestData import Test
from ReadData import Read
from CountData import Count
from ValidateData import Validate
from prettytable import PrettyTable
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

# Read Files and construct 2 lists of sentences and labels
Train_Texts, Train_Labels = Read("formatted-train/*.deft")
Test_Texts, Test_Labels = Read("formatted-test/*.deft")

Count(Train_Texts, Train_Labels, Test_Texts, Test_Labels)

TfidfObject = TfidfVectorizer(stop_words='english')
# learns the vocabulary (mean and standard deviation) and build matrix with it
TrainMatrix = TfidfObject.fit_transform(Train_Texts)
# build matrix with same vocabulary from the training data neglecting any new vocabulary in testing data
TestMatrix = TfidfObject.transform(Test_Texts)

t = PrettyTable(['Model', 'Confusion Matrix', 'Accuracy', 'Precision', 'Recall', 'F-Measure', 'Cross-Validation F1-Score'])

Model = "Naive Bayes"
model = MultinomialNB(alpha=0.1, fit_prior=True)
FitModel = model.fit(TrainMatrix, Train_Labels)
predictions = model.predict(TestMatrix)
CVScore = Validate(TrainMatrix, Train_Labels, FitModel)
Test(predictions, Test_Labels, Model, t, CVScore)

Model = "Logistic Regression"
model = LogisticRegression(penalty='l2', C=10, solver='lbfgs', max_iter=1000)
FitModel = model.fit(TrainMatrix, Train_Labels)
predictions = model.predict(TestMatrix)
CVScore = Validate(TrainMatrix, Train_Labels, FitModel)
Test(predictions, Test_Labels, Model, t, CVScore)

Model = "K-Nearest Neighbors"
model = KNeighborsClassifier(n_neighbors=1)
FitModel = model.fit(TrainMatrix, Train_Labels)
predictions = model.predict(TestMatrix)
CVScore = Validate(TrainMatrix, Train_Labels, FitModel)
Test(predictions, Test_Labels, Model, t, CVScore)

Model = "Support Vector Machine"
model = svm.SVC(C=1, kernel='linear', gamma=1)
FitModel = model.fit(TrainMatrix, Train_Labels)
predictions = model.predict(TestMatrix)
CVScore = Validate(TrainMatrix, Train_Labels, FitModel)
Test(predictions, Test_Labels, Model, t, CVScore)

Model = "Decision Tree"
model = tree.DecisionTreeClassifier(criterion='gini')
FitModel = model.fit(TrainMatrix, Train_Labels)
predictions = model.predict(TestMatrix)
CVScore = Validate(TrainMatrix, Train_Labels, FitModel)
Test(predictions, Test_Labels, Model, t, CVScore)

Model = "Random Forest"
model = RandomForestClassifier(n_estimators=100)
FitModel = model.fit(TrainMatrix, Train_Labels)
predictions = model.predict(TestMatrix)
CVScore = Validate(TrainMatrix, Train_Labels, FitModel)
Test(predictions, Test_Labels, Model, t, CVScore)

print(t)
