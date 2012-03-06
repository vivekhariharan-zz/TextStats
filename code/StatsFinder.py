

#! /usr/bin/env python
# Computes the statistics of keywords:stopwords ratio and pretty prints a dictionary of words used in the text 
# author: Vivek Hariharan

from nltk.corpus import stopwords

class StatsFinder:

	inputFileName=""
	outputFileName=""
	numberOfStopWords=0
	numberOfKeywords=0
	percentStopWords=0.0
	percentKeywords=0.0
	wordDictionary={}
	
	#parameterized constructor
	def __init__(self,inputFileName):
		self.inputFileName=inputFileName
		self.outputFileName=inputFileName+".stats"
		
		
	def computeStopWordsKeywords(self):
		inputFile=open(self.inputFileName,"r")
		
		listOfStopWords=stopwords.words('english')
		for line in inputFile:
			splitwords[]=line.split(" ")
			for word in splitwords:
				if word not in listOfStopWords:
					self.numberOfKeywords+=1
				else:
					self.numberOfStopWords+=1
		
		self.percentStopWords=float(numberOfStopWords)/float(splitwords.len())
		self.percentKeywords=float(numberOfKeywords)/float(splitWords.len())
		
	def computeDictionary(self)
