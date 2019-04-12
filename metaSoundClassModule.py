import numpy as np
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
			pp.plot(ar)
		else:
			ar = self.data
			for dp in ar:
				pp.plot(ar)
		printList(ar)
		
		pp.show()
		
	