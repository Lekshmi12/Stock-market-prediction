from pandas import read_csv
import numpy as np
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor
from sklearn.cross_validation import train_test_split
from TechnicalAnalysis import *
from DataFetcher import DataFetcher
import os
from datetime import datetime
from matplotlib import pyplot as plt
from DataPreprocessor import DataPreprocessor	
from ModelEvaluation import Evaluator

def getData(CSVFile):

	smoother = DataPreprocessor()
	data = read_csv(CSVFile)
	data = data[::-1] # reverse
	ohclv_data = np.c_[data['Open'],
					   data['High'],
					   data['Low'],
					   data['Close'],
					   data['Volume']]
	smoothened_ohclv_data = smoother.PandaSmoother(ohclv_data)
	return  smoothened_ohclv_data

def getTechnicalIndicators(X,d):

	RSI = getRSI(X[:,3]) 
	StochasticOscillator = getStochasticOscillator(X)
	Williams = getWilliams(X)

	
	MACD = getMACD(X[:,3])
	PROC = getPriceRateOfChange(X[:,3],d)
	OBV = getOnBalanceVolume(X)

	min_len = min(len(RSI),
				  len(StochasticOscillator),
				  len(Williams),
				  len(MACD),
				  len(PROC),
				  len(OBV))

	RSI = RSI[len(RSI) - min_len:]
	StochasticOscillator = StochasticOscillator[len(StochasticOscillator) - min_len:]
	Williams = Williams[len(Williams) - min_len: ]
	MACD = MACD[len(MACD) - min_len:]
	PROC = PROC[len(PROC) - min_len:]
	OBV = OBV[len(OBV) - min_len:]
	close = RSI[:,1]
	
	feature_matrix = np.c_[RSI[:,0],
						   StochasticOscillator[:,0],
						   Williams[:,0],
						   MACD[:,0],
						   PROC[:,0],
						   OBV[:,0],
						   close]

	return feature_matrix

def prepareData(X,d):

	feature_matrix = getTechnicalIndicators(X,d)
	number_of_samples = feature_matrix.shape[0]
	y0 = feature_matrix[:,-1][ :number_of_samples-d]
	y1 = feature_matrix[:,-1][d:]
	feature_matrix = feature_matrix[:number_of_samples-d]
	y = np.sign(y1 - y0)
	return feature_matrix[:,range(6)],y

def regression(data):

	data = np.array(data)
	n = len(data)
	X = data[:n-1]
	regression_result = []
	for i in range(5):
		
		y = data[:,i][1:]
		model = RandomForestRegressor(n_estimators = 30)
		model.fit(X,y)
		y_pred = model.predict(X)
	
		predicted_data = model.predict(data[-1].reshape(1,-1))
		regression_result.append(predicted_data[0])
	print regression_result
	return regression_result
	

def main(Selected_Stock, Trading_Day):

	fetcher = DataFetcher()
	
	fetch_result = fetcher.getHistoricalData(Selected_Stock)
	if fetch_result == -1:
		raise Exception("NO INTERNET CONNECTIVITY OR INVALID STOCK SYMBOL")
	dir_name = os.path.dirname(os.path.abspath(__file__))

	CSVFile = os.path.join(dir_name,"Dataset",Selected_Stock + ".csv")
	
	ohclv_data = list(getData(CSVFile))
	
	#current_data = regression(ohclv_data)
	#ohclv_data.append(current_data)
	ohclv_data = np.array(ohclv_data)

	X,y = prepareData(ohclv_data, Trading_Day)
	Xtrain,Xtest,ytrain,ytest = train_test_split(X,y)
	model = RandomForestClassifier(n_estimators = 35,criterion = "gini")
	model.fit(Xtrain,ytrain)

	y_pred = model.predict(Xtest)
	output = model.predict(X[-1].reshape(1,-1))

	Eval = Evaluator(Xtest,ytest,y_pred,model)
	accuracy, recall, precision, specificity = Eval.getPerformanceMetrics()

	print accuracy
	print recall
	print precision
	print specificity
	raw_input("Press enter to genereate OOB vs Number of estimators graph:")
	Eval.oob_vs_n_trees(100,Xtrain,ytrain)

	

Selected_Stock = raw_input("Enter the correct stock symbol: ")
Trading_Day = input("Enter the trading day: ")
main(Selected_Stock, Trading_Day)
	


	
	


