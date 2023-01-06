######################Last Update 12/23/16, WORKS#############################
import os, glob, zipfile, sys, shutil, fnmatch, time
from datetime import date, timedelta

os.chdir("C:\\download\\")
#File source & destinations
coopex = "\\\\corp1\\COLD\\COOP"
rootpath = "\\\\corp2\\data\\Apps\\DGData\\EXTRACT\\FX01004\\"
destpath = "\\\\corp2\\data\\Apps\\DGData\\EXTRACT\\FX01004\\"
srcpath = "C:\\download\\"
srcfiles = os.listdir(srcpath)
destdir = list(set([filename[0:7] for filename in srcfiles]))
pattern = "*.ZIP"
pattern2 = "*.TXT"
#Date times
yesterday = date.today() - timedelta(1)
daybefore1 = date.today() -timedelta(2)
daybefore2 = date.today() -timedelta(3)
daybefore3 = date.today() -timedelta(4)

yes = set(['yes','y'])
no = set(['no','n'])

#Function to create folder using dest path & dir name
def create(dirname, destpath):
    full_path = os.path.join(destpath, dirname)
    os.mkdir(full_path)
    return full_path

#Moves files into directory from downloads folder
def move(filename, destpath):
    shutil.copy(os.path.join(srcpath, filename), destpath)

#Sorts files based on dates, then renames files
def files_to_folders(filename):
    if f.endswith(".TXT"):
        ff = f[1:7]
        if ff == yesterday.strftime("%y%m%d"):
            fnew = f[13:]
            os.rename(os.path.join(root,f), os.path.join(root, fnew))

        elif ff == daybefore1.strftime("%y%m%d"):
            fnew = f[13:]
            os.rename(os.path.join(root,f), os.path.join(root, fnew))

        elif ff == daybefore2.strftime("%y%m%d"):
            fnew = f[13:]
            os.rename(os.path.join(root,f), os.path.join(root, fnew))

        elif ff == daybefore3.strftime("%y%m%d"):
            fnew = f[13:]
            os.rename(os.path.join(root,f), os.path.join(root, fnew))

    return filename


#Create directories based on ZIP folder
targets = [(folder, create(folder, destpath)) for folder in destdir]###HOW TO DETECT HIS AND SKIP IF EXISTS
if targets != True:
    for dirname, full_path in targets:
        for filename in srcfiles:
            if dirname == filename[0:7]:
                shutil.copy(filename, full_path)

        #Extract all files within folders to new directory root
        for root, dirs, files in os.walk(os.path.join(rootpath, full_path)):
            for files in fnmatch.filter(files,pattern):
                zipfile.ZipFile(os.path.join(root,files)).extractall(root)
                os.remove(os.path.join(root,files))

        #Rename extracted files in new direct root with end of filename
        #Creates directory based on filename characters[1:7]
        walkpath = os.path.join(rootpath,full_path)
        for root, dirs, files in os.walk(walkpath):
            for f in files:
                files_to_folders(f)

#Below: Gets created time of new directory folder, if created today, extracts
# files to wescorp extract folder one set at a time. If more than 1 set detected user must intervene for
# script to continue.
    created = time.strftime("%Y-%m-%d", time.gmtime(os.path.getmtime(rootpath)))
    today = date.today().strftime("%Y-%m-%d")
    for dirname, full_path in targets:
        if created >= today:    #creation date is today/this morning
            #print(dirname, created)
            dirfiles = os.path.join(root,full_path)
            for files in os.listdir(dirfiles):
                print(dirname,"'s file: ",files)
                shutil.copy(os.path.join(dirfiles,files), coopex)
        print("")
        print(dirname, "'s files have been moved to CO-OP extract folder.")
        print("")
        print("Extract files before continuing: [ENTER] To continue.")
        answer = input()   #Pause, print: please extract files before continuing


else: #if directories exist skip mkdir, copy files to dirc.
    for dirname, full_path in targets:
        for filename in srcfiles:
            if dirname == filename[0:7]:
                shutil.copy(filename, full_path)

        # Extract all files within folders to new directory root
        for root, dirs, files in os.walk(os.path.join(rootpath, full_path)):
            for files in fnmatch.filter(files,pattern):
                zipfile.ZipFile(os.path.join(root,files)).extractall(root)
                os.remove(os.path.join(root,files))
        #Rename extracted files in new direct root with end of filename
        walkpath = os.path.join(rootpath,full_path)
        for root, dirs, files in os.walk(walkpath):
            for f in files:
                files_to_folders(f) #Creates directory based on filename characters[1:7]
