import numpy as np

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
	