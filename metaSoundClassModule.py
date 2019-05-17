import numpy as np
from math import log
import matplotlib.pyplot as pp
from TimeLabelDataModule import printList

class SoundStatistic:
	"""docstring for metaSound"""
	def __init__(self, data):
		self.data = np.array(data)
		self.pauses = np.array([l[1]-l[0] for lst in data for l in lst])

	def __repr__(self):
		return self.data

	def stdDev(self):
		return self.pauses.std()
	
	def median(self):
		return np.median(self.pauses)

	def mean(self):
		return self.pauses.mean()

	def plot(self, what=0):
		if what == 0:
			ar = self.pauses
			printList(ar)

			pp.plot('x','y1',ar)
			pp.axhline(y=self.mean(), color='r', linestyle='-')
			pp.axhline(y=self.median(), color='b', linestyle='-')
			pp.xlabel('Zeit')
			pp.ylabel('Pausenlänge')
			pp.legend()
			pp.show()

		else:
			ar = self.data
			printList(ar)

			for dp in ar:
				pp.plot(*zip(*[(elem1, elem2) for elem1, elem2 in dp]))
			
			pp.xlabel('zeit')
			pp.ylabel('dunno')
			pp.legend()
			pp.show()
				
		
		
	