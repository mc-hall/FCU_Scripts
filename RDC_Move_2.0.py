
import shutil, os, datetime, time, glob, sys
from datetime import date

today = date.today()
todaysprod = today.strftime("%a")[:3]+today.strftime("%m%d")
now = datetime.datetime.now()

rdc_file_src = "\\\\corp1\\ftp\\mobile1"
rrm_file_src = "\\\\corp1\\ftp\\rrm"
crypt_src = "\\\\corp1\\ftp\\"
mobile_exists = "\\\\corp1\\ftp\\"+todaysprod+"\\mobile1_1"
rrm_exists = "\\\\corp1\\ftp\\"+todaysprod+"\\rrm_1"

file_dst = "\\\\corp1\\ftp\\"+todaysprod+"\\"

def first_mobile(): #If first mobile1 file, this function is run. Renames to mobile1_1 and moves
    shutil.move(rdc_file_src, os.path.join(file_dst,'mobile1_1'))
    print("First mobile file. File renamed to mobile1_1")
    print("mobile1_1 moved to "+ todaysprod)

def mobile1(): #finds mobile1, checks for previous verisons, appends next available number to end
    for files in os.listdir(file_dst):
         if files.startswith('mob') or files.startswith('MOB'):
            moblist.append(files)           #files matching mobile1 = list
            newmob = int(moblist[-1][8:9])  #
            n = newmob + 1
            newfile = 'mobile1_' + str(n)
    shutil.move(rdc_file_src, os.path.join(file_dst,newfile))
    print('mobile1 has been renamed to: '+newfile)
    print(newfile +" has been moved to "+ todaysprod)

def first_RRM(): #If first rrm file, this function is run. Renames to rrm_1 and moves
    shutil.move(rrm_file_src, os.path.join(file_dst,'rrm_1'))
    print("\nFirst rrm file. File renamed to rrm_1")
    print("rrm_1 moved to "+ todaysprod)


def RRM(): #finds rrm file, checks for previous verisons, appends next available number to end
    for files in os.listdir(file_dst):
         if files.startswith('RRM'):
            rrmlist.append(files)#files matching rrm = list
            newrrm = int(rrmlist[-1][9:10])
            n = newrrm + 1
            updatedfile = 'rrm_' + str(n)
    shutil.move(rrm_file_src, os.path.join(file_dst,updatedfile))
    print('\nrrm has been renamed to: '+updatedfile)
    print(updatedfile +" has been moved to "+ todaysprod)

def cryptfile(): #Finds downoaded encrypted AmericanFirst pgp file. Moves to daily production folder
    for files in os.listdir(crypt_src):
        if files.startswith('am_mobile'):
            shutil.move(os.path.join(crypt_src,files), os.path.join(file_dst,files))
            print('\n'+ files +" was moved to "+ todaysprod)


os.chdir(file_dst)
moblist=[]
rrmlist=[]

if not os.path.exists(mobile_exists):
        first_mobile()
else:
    while os.path.exists(rdc_file_src):
        mobile1()

if not os.path.exists(rrm_exists):
        first_RRM()
else:
    while os.path.exists(rrm_file_src):
        RRM()

cryptfile()

time.sleep(5)
