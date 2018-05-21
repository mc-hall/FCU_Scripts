### Last updated 2/9/2018 ####

import os, glob, zipfile, sys, shutil, time, fnmatch, datetime
from datetime import date, timedelta

curdate = datetime.datetime.now()
date1 = ("Monday")

def find_items(filename): #Will find todays rpt files only
	file_date = time.strftime('%Y-%m-%d',time.gmtime(os.path.getmtime(os.path.join(rptsrc,files))))
	if files.startswith('rpt') and files.endswith('.zip'):
		print("Unzipping file... ",files, file_date)
		zipfile.ZipFile(os.path.join(rptsrc,files)).extractall(rptsrc)   #Unzip files to rptdest

def copy_items(filename):
	print("Copying to TrueCards... ",files)
	shutil.copy(os.path.join(rpt_files,files),os.path.join(rptdest,files))

def old_items(filename):
	print('Archiving files...')
	shutil.move(os.path.join(rptsrc, files), os.path.join(archive,files))

#Find Files
for files in os.listdir(rptsrc):
	find_items(files)
	
#Copy files to TrueCards
for files in os.listdir(rpt_files):
	copy_items(files)

time.sleep(5)

#Move original zip files to archive folder 'Old files'
for files in os.listdir(rptsrc):
	if files.startswith("rpt_"):
		old_items(files)

#Delete extracted folder
print('Removing prod folder...')
shutil.rmtree("\\\\Corpapps02\\Data\\Apps\\DGDATA\\EXTRACT\\FISERV\\prod\\")

