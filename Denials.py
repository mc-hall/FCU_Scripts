import datetime, os, shutil, zipfile, requests, urllib, bs4, re, glob
from datetime import timedelta



def write_countfile(file):
	print('Writing to file count.txt ...')
	count_text = open('count.txt','w')
	count_text.write('Total items count = '+str(pdf_total))
	count_text.close()
	print('Writing done.')

def zip_files(files):
	today_zip = zipfile.ZipFile('AFC_Denial_Letters.zip','a')
	today_zip.write(files,compress_type=zipfile.ZIP_DEFLATED)
	today_zip.close()

#Get total number of PDFs in directory
pdf_total = len([file for file in os.listdir('.') if file.endswith('.PDF')])

#Change count in text file, 'count',  to reflect PDF count
write_countfile(pdf_total)
print('Total PDFs: ', pdf_total)

#Zip PDF and text file to folder: AFC_Denial_Letters.zip. Sat/Sun/Monday files together in same zip folder
print('Zipping files...')
for files in os.listdir('.'):
	if files.endswith('PDF') or files.startswith('count.txt'):
		zip_files(files)
print('Zipping Done.')

#Delete existing PDFs that were zipped up.
print('Removing files...')
for files in os.listdir('.'):
	if files.endswith('.PDF'): #files.startswith('count.txt')
		os.remove(files) 
print('Finished.')
