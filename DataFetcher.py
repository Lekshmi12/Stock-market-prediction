import yahoo_finance
import urllib
from datetime import datetime
import os
import mechanize
import requests

class DataFetcher:

	def __init__(self):
		pass

	def getHistoricalData(self,StockSymbol):

		currentDay = datetime.now().day 
		currentMonth = datetime.now().month
		currentYear = datetime.now().year
		url = "http://real-chart.finance.yahoo.com/table.csv?s="+StockSymbol+"&d="+str(currentMonth-1)+"&e="+str(currentDay)+"&f="+str(currentYear)+"&g=d&a=0&b=1&c=1900&ignore=.csv"		
	
		dir_name = os.path.dirname(os.path.abspath(__file__))

		outputfile = os.path.join(dir_name,"Dataset",StockSymbol+".csv")
		
		if os.path.isfile(outputfile):
			timestamp = os.path.getmtime(outputfile)
			lastmodifiedtime = datetime.fromtimestamp(timestamp)
			if (currentDay == lastmodifiedtime.day and 
				currentMonth == lastmodifiedtime.month and 
				currentYear == lastmodifiedtime.year):
				return 1 
		try:
			browser = mechanize.Browser()
			browser.retrieve(url,outputfile)
		except:
			return -1




