import os, zipfile, sys, shutil, time, datetime, fnmatch
from datetime import date, timedelta

os.chdir("\\\\corp1\\ftp1\\")

#Files to look for
abc_FILES = ('PAIDNT2','UNPAIDNOT1','UNPAIDNOT4',
    'GCONSDAY_','VNGBAL15_','VNGBL15Z_','DXDIPDNT_',
    'DCONSDAY_','LATENOT','DIRAMAT1_','DCRTMAT1_')
DIRA_DCRT = ('DIRAMAT1_','DCRTMAT1_','UNPAIDNOT4')

#Source & Destinations
sent_to_ftp = NOTES = "\\\\corp1\\ftp1\\Notes MG\\" #for files that were zipped up
zipdir = "\\\\corp1\\ftp1\\"
yesterdayprod = yesterday.strftime("%a")[:3]+yesterday.strftime("%m%d")
daybefore1prod = daybefore1.strftime("%a")[:3]+daybefore1.strftime("%m%d")



today = date.today()
todaysprod = today.strftime("%a")[:3]+today.strftime("%m%d")
todaytime = today.strftime("%Y%m%d")
PROD = "\\\\corp1\\ftp1\\"+todaysprod
def abc_today(filename):
    used_abc_today = 'abc_'+todaytime+'_a'
    new_dir = sent_to_ftp + used_abc_today
    if not os.path.exists(sent_to_ftp + used_abc_today):
        os.mkdir(new_dir)
        time.sleep(2)
    todayzip = zipfile.ZipFile("notices"+today.strftime('%m%d%y')+"a"+".zip", 'a')
    if files.startswith(DIRA_DCRT): #if files are DIRAMAT1_','DCRTMAT1, UNPAIDNOT4
        num_lines = sum(1 for line in open(os.path.join(zipdir,files))) #check number of lines
        if num_lines > 100: #if larger than 100 lines
            todayzip.write(os.path.join(zipdir,files), arcname=files,  compress_type=zipfile.ZIP_DEFLATED) #zip to folder by creation date
            shutil.move(os.path.join(zipdir, files), new_dir)
        elif num_lines <= 100:
            shutil.move(os.path.join(zipdir, files), PROD) #Will be todays production
            print(files, " today not used")
    else:
        s = os.path.getsize(os.path.join(zipdir,files))
        if s > 0: #If files have data, zip to appropriate zip folder
            todayzip.write(os.path.join(zipdir,files), arcname=files, compress_type=zipfile.ZIP_DEFLATED) #zip to folder by creation date
            shutil.move(os.path.join(zipdir, files), new_dir)
        else:
            shutil.move(os.path.join(zipdir, files), PROD) #Will be todays production
            print(files, " today not used")
    todayzip.close()

#Yesterday
yesterday = date.today() - timedelta(1)
yesterdayprod = yesterday.strftime("%a")[:3]+yesterday.strftime("%m%d")
y = yesterday.strftime("%Y%m%d")
YESTPROD = "\\\\corp1\\ftp1\\"+yesterdayprod
def abc_yesterday(filename):
    used_abc_yesterday = 'abc_' + y + '_a'
    new_dir = sent_to_ftp + used_abc_yesterday
    if not os.path.exists(sent_to_ftp + used_abc_yesterday):
        os.mkdir(new_dir)
        time.sleep(2)
    yesterdayzip = zipfile.ZipFile("notices"+yesterday.strftime('%m%d%y')+"a"+".zip", 'a')
    if files.startswith(DIRA_DCRT): #if files are DIRAMAT1_','DCRTMAT1
        num_lines = sum(1 for line in open(os.path.join(zipdir,files))) #check number of lines
        if num_lines > 100: #if larger than 100
            yesterdayzip.write(os.path.join(zipdir,files), arcname=files,  compress_type=zipfile.ZIP_DEFLATED) #zip to folder by creation date
            shutil.move(os.path.join(zipdir, files), new_dir)
        elif num_lines < 100:
            shutil.move(os.path.join(zipdir, files), PROD) #Will be todays production
            print(files, " yesterday not used")
    else: #For all other files
        s = os.path.getsize(os.path.join(zipdir,files))
        if s > 0: #If files have data, zip to appropriate zip folder
            yesterdayzip.write(os.path.join(zipdir,files), arcname=files,  compress_type=zipfile.ZIP_DEFLATED) #zip to folder by creation date
            shutil.move(os.path.join(zipdir, files), new_dir)
        else:
            shutil.move(os.path.join(zipdir, files), yesterdayprod) #Will be todays production
            print(files, " yesterday not used")
    yesterdayzip.close()

#Day before yesterday
daybefore1 = date.today() -timedelta(2)
daybefore1prod = daybefore1.strftime("%a")[:3]+daybefore1.strftime("%m%d")
dbefore1 = daybefore1.strftime("%Y%m%d")
DAY1PROD = "\\\\corp1\\ftp1\\"+daybefore1prod
def abc_daybefore1(filename):
    used_abc_daybefore1 = 'abc_' + dbefore1 + '_a'
    new_dir = sent_to_ftp + used_abc_daybefore1
    if not os.path.exists(sent_to_ftp + used_abc_daybefore1):
        os.mkdir(new_dir)
        time.sleep(2)
    daybeforezip1 = zipfile.ZipFile("notices"+daybefore1.strftime('%m%d%y')+"a"+".zip", 'a')
    if files.startswith(DIRA_DCRT): #if files are DIRAMAT1_','DCRTMAT1
        num_lines = sum(1 for line in open(os.path.join(zipdir,files))) #check number of lines
        if num_lines > 100: #if larger than 100
            daybeforezip1.write(os.path.join(zipdir,files), arcname=files,  compress_type=zipfile.ZIP_DEFLATED) #zip to folder by creation date
            shutil.move(os.path.join(zipdir, files), new_dir)
        elif num_lines <= 100:
            shutil.move(os.path.join(zipdir, files), PROD) #Will be todays production
            print(files, " daybefore1 not used")
    else: #For all other files
        s = os.path.getsize(os.path.join(zipdir,files))
        if s > 0: #If files have data, zip to appropriate zip folder
            daybeforezip1.write(os.path.join(zipdir,files), arcname=files,  compress_type=zipfile.ZIP_DEFLATED) #zip to folder by creation date
            shutil.move(os.path.join(zipdir, files), new_dir)
        elif s <= 0:
            shutil.move(os.path.join(zipdir, files), daybefore1prod) #Will be todays production
            print(files, " daybefore1 not used")
    daybeforezip1.close()

#3 days ago
daybefore2 = date.today() -timedelta(3)
daybefore2prod = daybefore2.strftime("%a")[:3]+daybefore2.strftime("%m%d")
dbefore2 = daybefore2.strftime("%Y%m%d")
DAY2PROD = "\\\\corp1\\ftp1\\"+daybefore2prod
def abc_daybefore2(filename):
    used_abc_daybefore2 = 'abc_' + dbefore2 + '_a'
    new_dir = sent_to_ftp + used_abc_daybefore2
    if not os.path.exists(sent_to_ftp + used_abc_daybefore2):
        os.mkdir(new_dir)
        time.sleep(2)
    daybeforezip2 = zipfile.ZipFile("notices"+daybefore2.strftime('%m%d%y')+"a"+".zip", 'a')
    if files.startswith(DIRA_DCRT): #if files are DIRAMAT1_','DCRTMAT1
        num_lines = sum(1 for line in open(os.path.join(zipdir,files))) #check number of lines
        if num_lines > 100: #if larger than 100
            daybeforezip2.write(os.path.join(zipdir,files), arcname=files,  compress_type=zipfile.ZIP_DEFLATED) #zip to folder by creation date
            shutil.move(os.path.join(zipdir, files), new_dir)
        elif num_lines < 100:
            shutil.move(os.path.join(zipdir, files), PROD) #Will be todays production
            print(files, " daybefore2 not used")
    else: #For all other files
        s = os.path.getsize(os.path.join(zipdir,files))
        if s > 0: #If files have data, zip to appropriate zip folder
            daybeforezip2.write(os.path.join(zipdir,files), arcname=files,  compress_type=zipfile.ZIP_DEFLATED) #zip to folder by creation date
            shutil.move(os.path.join(zipdir, files), new_dir)
        else:
            shutil.move(os.path.join(zipdir, files), PROD) #Will be todays production
            print(files, " daybefore2 not used")
    daybeforezip2.close()

#4 days ago
daybefore3 = date.today() -timedelta(4)
daybefore3prod = daybefore3.strftime("%a")[:3]+daybefore3.strftime("%m%d")
dbefore3 = daybefore3.strftime("%Y%m%d")
DAY3PROD = "\\\\corp1\\ftp1\\"+daybefore3prod
def abc_daybefore3(filename):
    used_abc_daybefore3 = 'abc_' + dbefore3 + '_a'
    new_dir = sent_to_ftp + used_abc_daybefore3
    if not os.path.exists(sent_to_ftp + used_abc_daybefore3):
        os.mkdir(new_dir)
        time.sleep(2)
    daybeforezip3 = zipfile.ZipFile("notices"+daybefore3.strftime('%m%d%y')+"a"+".zip", 'a')
    if files.startswith(DIRA_DCRT): #if files are DIRAMAT1_','DCRTMAT1
        num_lines = sum(1 for line in open(os.path.join(zipdir,files))) #check number of lines
        if num_lines > 100: #if larger than 100
            daybeforezip3.write(os.path.join(zipdir,files), arcname=files,  compress_type=zipfile.ZIP_DEFLATED) #zip to folder by creation date
            shutil.move(os.path.join(zipdir, files), new_dir)
        elif num_lines < 100:
            shutil.move(os.path.join(zipdir, files), PROD) #Will be todays production
            print(files, " daybefore3 not used")
    else: #For all other files
        s = os.path.getsize(os.path.join(zipdir,files))
        if s > 0: #If files have data, zip to appropriate zip folder
            daybeforezip2.write(os.path.join(zipdir,files), arcname=files,  compress_type=zipfile.ZIP_DEFLATED) #zip to folder by creation date
            shutil.move(os.path.join(zipdir, files), new_dir)
        else:
            shutil.move(os.path.join(zipdir, files), PROD) #Will be todays production
            print(files, " daybefore3 not used")
    daybeforezip3.close()

for files in os.listdir(zipdir): #Directory - ftp1
    if files.startswith(abc_FILES): #if files match one of the names
        created = time.strftime("%Y%m%d", time.gmtime(os.path.getmtime(os.path.join(zipdir,files)))) # check creation date
        if created == todaytime:
            abc_today(files)
        elif created == y:
            abc_yesterday(files)
        elif created == dbefore1:
            abc_daybefore1(files)
        elif created == dbefore2:
            abc_daybefore2(files)
        elif created == dbefore3:
            abc_daybefore3(files)
