from ModelEvaluation import Evaluator
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
import numpy as np

data = load_iris()
x = data.data
y = data.target
xtrain,xtest,ytrain,ytest = train_test_split(x,y)
model = SVC()
model.fit(x,y)
ytest = np.random.randint(0,2,100)
y_pred = np.random.randint(0,2,100)
Eval = Evaluator(ytest,y_pred,model)
print Eval.sklearnMetrics()
print Eval.customMetrics()
