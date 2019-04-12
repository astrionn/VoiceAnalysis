# Make sure Audacity is running first and that mod-script-pipe is enabled
# before running this script.


#imports

import os
import sys
import glob
from xml.etree import ElementTree
import functools
import operator
from TimeLabelDataModule import TimeLabelData, printList
from TimeLabelDataSetModule import TimeLabelDataSet
from metaSoundClassModule import SoundStatistic

#/imports

#globals
SOURCE_FOLDER_PATH = "C:\\Users\\1337\\Desktop\\marie\\Samples\\" # make sure path exists, "\" is an escape char 
DEST_FOLDER_PATH = "C:\\Users\\1337\\Desktop\\marie\\PostProjects\\"
SOUND_FORMAT = ".mp3" #### change this to supported file format from audacity and make sure that there are no spaces in the filename ####

#/globals

#chk folder
if not os.path.isdir(SOURCE_FOLDER_PATH):
	os.mkdir(SOURCE_FOLDER_PATH)#create a folder for the DAU
if not os.path.isdir(DEST_FOLDER_PATH):
	os.mkdir(DEST_FOLDER_PATH)
#/chk folder

#IO
def get3DArrayFromSet(set_):

	TLD = [label.labels for label in set_.dataSets]
	return TLD

def getAvgSilPerTrack(set_):
	
	return functools.reduce(operator.add,[TLD.getAvgSilDur() for TLD in set_.dataSets]) / set_.__len__()

def recordingToAup():
	"""import samples to audacity and run sound labeling filter and save it to xml(.aup)"""
	from audacityAPI import do #also fires up audacity.exe if in sub dir /AudacityWithPipe w/ 15s delay
	for file in glob.glob(SOURCE_FOLDER_PATH + "*" + SOUND_FORMAT):
		print(file)
		do( 'Import2: Filename='+file )
		do( 'SoundFinder: sil-lev=30 sil-dur=0.1')
		file = file[len(SOURCE_FOLDER_PATH):len(file)-4]
		do( 'SaveProject2: Filename='+DEST_FOLDER_PATH+file+'.aup' )
		do( 'Close:')
		print("\n") 


def AupToTLDS():
	"""Runs trough an xml(.aup file) to get time labels and dump them to .txt"""
	
	TimeLabelDataSet_ = TimeLabelDataSet()
	for file in glob.glob(DEST_FOLDER_PATH+"*.aup"):
		print(file)
		e = ElementTree.parse(file).getroot()
		for child in e:
			if child.tag == "{http://audacity.sourceforge.net/xml/}labeltrack": #found timelabel section
				t = TimeLabelData(file)
				for label in child:
					t.addLabelPair(label.attrib['t'],label.attrib['t1'])
		TimeLabelDataSet_.addTimeLabelData(t)
		TimeLabelDataSet_.saveToFile()
		print("\n")		
		   
def TLDSToStatistics():
	#DEST_FOLDER_PATH = input("gimme dem tlds folder") +"\\"
	DEST_FOLDER_PATH = "C:\\Users\\1337\\Desktop\\marie\\2019-03-23\\"
	for file in glob.glob(DEST_FOLDER_PATH+"*.tlds"):
		t = TimeLabelDataSet()
		t.importFromFile(file)
		stats = SoundStatistic(get3DArrayFromSet(t))

		yield stats

#/IO

#lööp
def main():
	"""sends every sample trough sound filters via audacity API and extracts time label data """
	
	
	#recordingToAup()
	#if input() == 0: sys.exit()
	#AupToTLDS()
	#if input() == 0: sys.exit()
	stats = TLDSToStatistics()
	for stat in stats:
		print(stat.median())
		print(stat.mean())
		stat.plot()
		pass
	#if input() == 0: sys.exit()
	
#/lööp

main()
print("done")



