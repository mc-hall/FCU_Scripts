import os, glob, zipfile, sys, shutil, time, fnmatch, datetime, textwrap
from datetime import date, timedelta

yes = set(['yes','y',])
no = set(['no','n'])
wespat = ('.NDX','.dbf', '.TXT', '.IMG')

def IMGFILE_UNZIP(imagefile):
    zipfile.ZipFile(os.path.join(chksrc,f)).extractall(chksrc)
    print(f, " unzipped!")
    

def IMGFILE_MOVE(imagefile):
    if today == date1: #If today = monday: If today is monday, look for 3 days ago prod folder (friday)
        shutil.move(os.path.join(chksrc,f),lastweekIMGfiledst)
        print(f, " moved to Friday's production folder")
    else:
        shutil.move(os.path.join(chksrc,f), os.path.join(imgfiledst, f))
        print(f, " moved to yesterdays production folder")



try:
    for f in os.listdir(chksrc):
        if f.startswith("ImgFile") and f.endswith(".ZIP"):
            IMGFILE_UNZIP(f)
except(OSError):
    print("Error while trying to unzip file")


try:
    for f in os.listdir(chksrc):
        if f.startswith("ImgFile") and f.endswith(".ZIP"):
            print(f)
            IMGFILE_MOVE(f)
except(OSError):
    print("Error while trying to move file")


#try:
if today == date1:
    print("Looking for Friday's ImgFile.zip...")
    for files in os.listdir(vision_friday):
        if files.endswith(".dbf"):
            print("")
            print("Creating .XLS copy of ", files, "...")
            filesnew = os.path.join(vision_friday,files+"-copy")
            shutil.copy(os.path.join(vision_friday, files), os.path.join(vision_friday,filesnew))
            oldbase = os.path.splitext(filesnew)
            newname = filesnew.replace('.dbf-copy', '.xls')
            output = os.rename(filesnew, newname)
            shutil.copy(os.path.join(vision_yesterday, newname),chksrc)


            print("")
            strs = "Check Excel file! Do the Excel lines match previous nights' count on daily schedule?"
            print(textwrap.fill(strs,50))
            print("'y' to continue, 'n' to abort")
            answer = 'yes' #Set to 'input()' for user intervention

            if answer in yes:
                print("")
                print("Files will now be moved...")
                print("")
                try:
                    for files in os.listdir(vision_friday):
                        if files.endswith(wespat):
                            shutil.copy(os.path.join(vision_friday,files),wescorp)
                            print(files, " moved to wescorp folder")
                except(OSError):
                    print("Error trying to copy or move files in their folders")
                    print("Check file source and destination folders, or script for errors")
            elif answer in no:
                print("You have chosen 'No'. Operation will abort in 5 seconds...")
                for files in os.listdir(imgfiledst):
                    if files.startswith("ImgFile") and files.endswith(".ZIP"):
                        shutil.move(os.path.join(imgfiledst,files), chksrc)
                        print("")
                        print("ImgFile.Zip has been moved back to it's original folder.")
else: #else if not Monday, check for rest of week (tues-fri)
    for files in os.listdir(vision_yesterday):
        if files.endswith(".dbf"):
            print("")
            print("Creating .XLS copy of ", files)
            filesnew = os.path.join(vision_yesterday,files+"-copy")
            shutil.copy(os.path.join(vision_yesterday, files), os.path.join(vision_yesterday,filesnew))
            oldbase = os.path.splitext(filesnew)
            newname = filesnew.replace('.dbf-copy', '.xls')
            output = os.rename(filesnew, newname)
            shutil.copy(os.path.join(vision_yesterday, newname),chksrc)

            print("")
            strs = "Check Excel file! Do the Excel lines match previous nights' count on daily schedule?"
            print(textwrap.fill(strs,40))
            print("'y' to continue, 'n' to abort")
            answer = input()

            if answer in yes:
                print("")
                print("Files will now be moved...")
                print("")
                try:
                    for files in os.listdir(vision_yesterday):
                        if files.endswith(wespat):
                            shutil.copy(os.path.join(vision_yesterday,files),wescorp)
                            print(files, " moved to wescorp folder")
                except(OSError):
                    print("Error trying to copy or move files in their folders")
                    print("Check file source and destination folders, or script for errors")
            elif answer in no:
                print("You have chosen 'No'. Operation will abort in 5 seconds...")
                for files in os.listdir(imgfiledst):
                    if files.startswith("ImgFile") and files.endswith(".ZIP"):
                        shutil.move(os.path.join(imgfiledst,files), chksrc)
                        print("")
                        print("ImgFile.Zip has been moved back to it's original folder.")
