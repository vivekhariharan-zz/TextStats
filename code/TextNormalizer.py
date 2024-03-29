
#! /usr/bin/env python
# Normalizes text case, removes punctuation, and tokenizes word wise
# author: Vivek Hariharan 

from nltk import WordPunct_Tokenize

class TextNormalizer:
	
	inputTextFile=""
	outputTextFile=""
	tokenizedWords=[]#stores the tokens without punctuation
	normalizedWords=[]
	
	
	#parameterized constructor
	def __init__(self,inputTextFile):
		self.inputTextFile=inputTextFile
		self.outputTextFile=inputTextFile+".normalized"
		
		
	#uses nltk workpuncttokenizer
	def tokenize(self):
		inputFile=open(self.inputTextFile,"r")
		fileText=""
		for line in inputFile:
			fileText+=line+" "
		self.tokenizedWords=WordPunctTokenizer().tokenize(fileText)
		
		
	def normalizeCase(self):
		for word in self.tokenizedWords:
			self.normalizedWords.append(word.lower())
	
	def writeToOutputFile(self):
		outputFile=open(self.ouputTextFile,"w")	
		for word in self.normalizedWords:
			outputFile.write(word+" ")
