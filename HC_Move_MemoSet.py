import os, glob, sys, shutil,  fnmatch


memopat = "670_Feedback"


for files in os.listdir(Memosrc):
    if files.startswith("MFBK_91670_Feedback"):
        shutil.move(os.path.join(Memosrc, files), os.path.join(Memodst, files))
        print(files, " Have been moved to Memo's Set folder")
