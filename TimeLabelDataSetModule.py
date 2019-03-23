#from sets import Set
from TimeLabelDataModule import TimeLabelData
from TimeLabelDataModule import printList
import os
import pickle
import datetime 
#item_collection = Set()

class TimeLabelDataSet:

    def __init__(self):
        self.dataSets = []

    def __len__(self):
    	return len(self.dataSets)

    def importFromFile(self,file):
        if os.path.exists(file):
            with open(file,'rb') as handle:
                self.dataSets = pickle.load(handle)

    def saveToFile(self):
    	DEST_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__)) +"\\"+str(datetime.date.today())
    	now = datetime.datetime.now()
    	curtime = str(now.hour) + "-" + str(now.minute) + "-" + str(now.second)
    	if not os.path.isdir(DEST_FOLDER_PATH):
    		os.mkdir(DEST_FOLDER_PATH)
    	with open(DEST_FOLDER_PATH + "\\"+ curtime + ".tlds" ,"wb") as handle:
                 pickle.dump(self.dataSets, handle)

    def addTimeLabelData(self, *args):
    	for arg in args:
    		if type(arg).__name__ == "TimeLabelData" :
    			self.dataSets.append(arg)

    def printData(self):
    	for TimeLabelData in self.dataSets:
    		TimeLabelData.printData()

    def printNames(self):
    	printList([TimeLabelData.name for TimeLabelData in self.dataSets])



