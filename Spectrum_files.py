import datetime, os, shutil, time
from datetime import timedelta


date = datetime.datetime.now()
Yesterday = date.today()-timedelta(1)
yesterdays_folder = Yesterday.strftime('%Y-%m-%d')
Friday = date.today() - timedelta(3) 
friday_folder = Friday.strftime('%Y-%m-%d')
new_prod_yest = time.strftime('%Y')+'-'+time.strftime('%m')+ ' '+time.strftime('%b')
new_prod_fri = Friday.strftime('%Y')+'-'+Friday.strftime('%m')+ ' '+Friday.strftime('%b')


def fics(filename): #Move to yesterdays Production folder
	if files.startswith('DFICSIMP') or files.startswith('DCRESIMP'):
		if yest_prod_folder:
			('Mondays ',files)
			shutil.move(os.path.join(file_src,files),os.path.join(yest_prod_folder,files))
	else:
		print('Error: 666')

def fics_friday(filename): #Move to Friday's production folder
	if files.startswith('MP') or files.startswith('DMP'):
		if fri_prod_folder:
			print('Fridays ',files)
			shutil.move(os.path.join(file_src,files), os.path.join(fri_prod_folder,files))
	else:
			print('Error: 666')



if date.today().weekday() == 0: #If today is Monday ,move files to Fridays Production folder
	for files in os.listdir(file_src):
		fics_friday(files)
else:
	for files in os.listdir(file_src): #If today is Tues-Friday, move files to yesterdays production folder
		fics(files)


