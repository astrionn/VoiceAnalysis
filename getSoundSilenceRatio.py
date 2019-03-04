# Make sure Audacity is running first and that mod-script-pipe is enabled
# before running this script.


#imports

import os
import glob
from xml.etree import ElementTree
import TimeLabelDataModule
from TimeLabelDataSetModule import TimeLabelDataSet

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
def aud_processing(file):
    """import samples to audacity and run sound labeling filter and save it to xml(.aup)"""
    from audacityAPI import do #also fires up audacity.exe if in sub dir /AudacityWithPipe w/ 15s delay
    do( 'Import2: Filename='+file )
    do( 'SoundFinder: sil-lev=30 sil-dur=0.1')
    file = file[len(SOURCE_FOLDER_PATH):len(file)-4]
    do( 'SaveProject2: Filename='+DEST_FOLDER_PATH+file+'.aup' )
    do( 'Close:')


def xml_processing(file):
    """Runs trough an xml(.aup file) to get time labels and dump them to .txt"""
    
    e = ElementTree.parse(file).getroot()
    for child in e:
        if child.tag == "{http://audacity.sourceforge.net/xml/}labeltrack": #found timelabel section
            t = TimeLabelDataModule.TimeLabelData(file)
            for label in child:
                t.addLabelPair(label.attrib['t'],label.attrib['t1'])

            return t		
            

                
#/IO

#lööp
def main():
    """sends every sample trough sound filters via audacity API and extracts time label data """
    for file in glob.glob(SOURCE_FOLDER_PATH + "*" + SOUND_FORMAT):
        print(file)
        aud_processing(file)
    print("\n") 
    TimeLabelDataSet_ = TimeLabelDataSet()

    for file in glob.glob(DEST_FOLDER_PATH+"*.aup"):
        print(file)
        t=xml_processing(file)
        TimeLabelDataSet_.addTimeLabelData(t)
        print("\n")
    TimeLabelDataSet_.saveToFile()
#/lööp

#main()

