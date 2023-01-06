###################LAST UPDATED 12/7/16 - WORKING#########################

import os, zipfile, sys, shutil, time, datetime
from datetime import date, timedelta

os.chdir("\\\\corp1\\ftp1\\")

yesterday = date.today() - timedelta(1)
misc = "\\\\corp1\\ftp1\\Notes MG\\"
zipdir = "\\\\corp1\\ftp1\\"
pattern = "amsurvey"
zipme = "\\\\corp1\\ftp1\\"

today = date.today()
todaysprod = today.strftime("%A")[:3]+today.strftime("%m%d")


try:
    for files in os.listdir(zipdir):
        if files.startswith(pattern):
            s = os.path.getsize(os.path.join(zipme,files))
            if s > 0:
                zipname = zipfile.ZipFile("amsurvey"+files[-6:]+".zip", 'a') #new name to give new zipped folder
                zipname.write("amsurvey"+files[-6:], compress_type=zipfile.ZIP_DEFLATED) #what to add to new zip folde
                zipname.close() #close & write to zipfolder
                shutil.move(os.path.join(zipme,files), misc)
                print(files," Kbytes: ",s," have been zipped and is ready.")
                time.sleep(2)
            elif s == 0:
                shutil.move(os.path.join(zipme,files), misc)
                print(s, " Had no data and was not zipped.")

    try:
        for files in os.listdir(zipdir):
            shutil.move(os.path.join(zipdir, "file1"), todaysprod)
            shutil.move(os.path.join(zipdir, "file2"), todaysprod)
    except(FileNotFoundError):
        print("file1 & file2 not found.")

except(IOError):
    pass
