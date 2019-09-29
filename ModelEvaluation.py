import os
import numpy as np
from sklearn.metrics import roc_curve,auc
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier

class Evaluator:

	def __init__(self,xtest,ytest,y_pred,LearningModel):
		self.xtest = xtest
		self.ytest = ytest
		self.y_pred = y_pred
		self.model = LearningModel

	def confusion_matrix(self):

		self.confusion_matrix = np.array([[0,0],[0,0]])
		self.ytest[self.ytest == -1] = 0
		self.y_pred[self.y_pred == -1] = 0
		for x,y in zip(self.ytest,self.y_pred):
			self.confusion_matrix[x][y] += 1

	def getPerformanceMetrics(self):

		self.confusion_matrix()

		accuracy = (
					float((self.confusion_matrix[0][0]+self.confusion_matrix[1][1]))/
					(self.confusion_matrix[0][0]+self.confusion_matrix[0][1]+self.confusion_matrix[1][0]+self.confusion_matrix[1][1])
			)
		precision = (
					float((self.confusion_matrix[1][1]))/
					(self.confusion_matrix[1][1] + self.confusion_matrix[0][1])
			)
		recall = (
				float((self.confusion_matrix[1][1]))/
				(self.confusion_matrix[1][1]+self.confusion_matrix[1][0])
			)
		specificity = (
				float((self.confusion_matrix[0][0]))/
				(self.confusion_matrix[0][0] + self.confusion_matrix[0][1])
			)

		return accuracy, recall, precision, specificity

	def drawROC(self):
	
		base_dir = os.path.dirname
		abspath = os.path.abspath
		dir_name =  base_dir(base_dir(base_dir(abspath(__file__))))
		savepath = os.path.join(dir_name,"static_in_pro","our_static","img","roc.png")

		y_prob = self.model.predict_proba(self.xtest)
		true_probability_estimate = y_prob[:,1]
	
		fpr,tpr,threshold = roc_curve(self.ytest,true_probability_estimate)
		area = auc(fpr,tpr)
		plt.plot(fpr,tpr,linewidth = 2.0,label = "ROC curve (Area= %0.2f)" % area)
		plt.plot([0,1],[0,1],"r--")
		plt.xlabel("False Postive Rate")
		plt.ylabel("True Positive Rate")
		plt.legend(loc = "lower right")
		plt.show()
		#plt.savefig(savepath)
		#plt.close()

	def oob_vs_n_trees(self,max_trees,Xtrain, ytrain):

		number_of_trees = range(2,max_trees + 1)
		oob_errors = []
		for i in xrange(2,max_trees + 1):
			model = RandomForestClassifier(warm_start = True, 
				oob_score = True, 
				n_estimators = i)
			model.fit(Xtrain,ytrain)
			oob_error = 1 - model.oob_score_
			oob_errors.append(oob_error)
			print i,oob_error
		plt.plot(number_of_trees, oob_errors, linewidth = 2.0)
		plt.xlabel("Number of trees")
		plt.ylabel("OOB error rate")
		plt.show()




