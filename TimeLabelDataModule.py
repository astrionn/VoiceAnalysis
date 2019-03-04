import pickle
import inspect
import os
class TimeLabelData:
    
    def __init__(self,filename):
        self.name = filename
        self.labels = []
        self.pauses = []

    def printList(self,list_):
        print("#"*64)
        print(inspect.stack()[1].function)
        print("#"*64)
        for _ in list_:
            print(str(_))
        print("#"*64)

    def addLabelPair(self,start,stop):
        self.labels.append((float(start),float(stop)))

    def getData(self):
        return self.labels

    def printData(self):
        self.printList(self.labels)

    def getLength(self):
        if not self.labels: return 0
        return  max(max(self.labels,key=lambda x:x[1]))
    
    def saveToFile(self):
        file = self.name[:len(self.name)-4] +".pickle"
        if not os.path.exists(file):
            with open(file ,"wb") as handle:
                 pickle.dump(self.labels, handle)
        else:
            print("File already exists")
            return

    def importFromFile(self,file):
        if os.path.exists(file):
            with open(file,"rb") as handle:
                self.labels = pickle.load(handle)
        else:
            print("File not found")
    
    def getSilence(self):
        sound = 0
        for l in self.labels:
            sound+=l[1]-l[0]

        return self.getLength()-sound

    def getAvgSilDur(self):
        if not self.labels : return 0
        silence = self.getSilence()
        silences = len(self.labels)+1
        return silence/silences

    def SoundToPauses(self):
        """generates start and end of pauses from time labelled sound """
        if not self.labels : return 0
        self.pauses = [0]*len(self.labels)
        for i in range(len(self.labels)):
            if not i == 0 :
                self.pauses[i] = (self.labels[i-1][1] , self.labels[i][0])
            else:
                self.pauses[0] = (0,self.labels[0][0])
        return self.pauses                

    def printPauses(self):
        self.printList(self.pauses)

    #def medianPause
    #plotted ??
    

    

def printList(list_):
        print("#"*64)
        print(inspect.stack()[1].function)
        print("#"*64)
        for _ in list_:
            print(str(_))
        print("#"*64)