import os,zipfile, sys, shutil, time, textwrap, pysftp
from datetime import date, timedelta
import smtplib
import email.message
from ftplib import FTP, FTP_TLS



date1 = ("Monday") #needs to be Monday on prod

today = time.strftime("%A")
yesterday = date.today() - timedelta(1)
yestprod = yesterday.strftime('%Y'+'-'+'%m'+'-'+'%d')
friday = date.today() - timedelta(3) #Change to (4) if holiday on Monday
friprod = friday.strftime('%Y'+'-'+'%m'+'-'+'%d')
new_prod_yest = time.strftime('%Y')+'-'+time.strftime('%m')+ ' '+time.strftime('%b')
new_prod_fri = friday.strftime('%Y')+'-'+friday.strftime('%m')+ ' '+friday.strftime('%b')


imgfiledst = "\\\\corp\\data\\Apps\\DGData\\OPERATIONS\\DailyProduction\\"+new_prod_yest+"\\"+yestprod+"\\" #Moves to yesterdays production folder
lastweekIMGfiledst = "\\\\corpapps02\\data\\Apps\\DGData\\OPERATIONS\\DailyProduction\\"+new_prod_fri+"\\"+friprod+"\\"
chksrc = "\\\\corp\\coftp\\"
vision_yesterday = "\\\\corpiis01\\coftp\\vision\\bank\\path\\data\\"+yesterday.strftime("%m%d%Y")+"\\COF\\10362\\00001\\"
vision_friday = "\\\\corpiis01\\coftp\\vision\\bank\\path\\data\\"+friday.strftime("%m%d%Y")+"\\COF\\10362\\00001\\"
corp = "\\\\corp\\cold\\corp\\"
vision_root = "\\\\corp\\coftp\\vision\\"
wespat = ('.NDX','.dbf', '.TXT', '.IMG')

class Corp():

    def __init__(self):
        print("")


    #Unzip archive folder
    def IMGFILE_UNZIP(imagefile):
        """ Unzip the folder downloaded"""
        for f in os.listdir(chksrc):
                if f.startswith("123465789_") and f.endswith(".zip"):
                    zipfile.ZipFile(os.path.join(chksrc,f)).extractall(chksrc)
                    print(f, " unzipped!")
        
    #Copy files within archive folder to corp extract
    def IMGFILE_COPY(imagefile):
        """ Copy all files from within new unzipped folder to production extraction folder"""
        list_files = os.walk(vision_root)
        for root, dirs, files in list_files:
            print('Copying...', files)
            for f in files:
                if f.endswith(wespat):
                    filename = os.path.join(root,f)
                    filename_prefix = f.split('-')[0]
                    shutil.copy(os.path.join(root,filename_prefix), os.path.join(corp,filename_prefix))
                    print(filename_prefix)

    #Move archive folder to daily production folder
    def IMGFILE_MOVE(imagefile):
        """Look for the zip folder and move to previous days' production folder on a specific day"""
        for f in os.listdir(chksrc):
                if f.startswith("123465789_") and f.endswith(".zip"):
                    print('Moving ', f)
                    if today == date1: #If today = monday: If today is monday, look for 3 days ago prod folder (friday)
                        shutil.move(os.path.join(chksrc,f),lastweekIMGfiledst)
                        print(f, " moved to Friday's production folder")
                    else:   #If today is Tuesday-Friday look for yesterday's production folder
                        shutil.move(os.path.join(chksrc,f), os.path.join(imgfiledst, f))
                        print(f, " moved to yesterdays production folder")
        shutil.rmtree(vision_root)
        print("")
        print("Vision folder has been moved to trash")

    #Send failure email
    def send_email(self):
        """Sends an email to myelf """
        sender = 'myemail@emaildomain.org'
        receiver = 'myemail@emaildomain.org'
        password = 'qwerty'
        smtpsrv = 'smtp.office365.com'
        body = '\n\n Could not download corp files \n'
        message = 'Subject: corp File download failure'.format()
        header = "To: "+ receiver +" \n " #+ " From: " + sender
        msg = header +'\n'+ message +'\n'+ body
        smtpserver = smtplib.SMTP(smtpsrv,587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.login(sender,password)
        smtpserver.sendmail(sender, receiver, msg )
        smtpserver.close()

    #Download zip file from FTP
    def FTP_DOWNLOAD(self):
        """Connect to Cataylst's FTP and download the zip folder within"""
        cnopts = pysftp.CnOpts(knownhosts=None)
        cnopts.hostkeys = None
        directory = '/Pickup/'
        with pysftp.Connection(host='123.465.789.125',username='user', password='pw', cnopts=cnopts) as sftp:
        
            sftp.listdir()
            
            #for items in new_files:
             #   if items.startswith('123465789_') and items.endswith('.zip'):
              #      print(items)
               #     local_file = os.path.join(chksrc, items)
                #    f = open(local_file, 'wb')
                 #   sftp.retrbinary('RETR %s' % items, f.write)
                  #  f.close()
                   # return True
        sftp.close()
        
        
#try:
corp_file = corp()
corp_file.FTP_DOWNLOAD()
#    corp_file.IMGFILE_UNZIP()
#    corp_file.IMGFILE_COPY()
#    corp_file.IMGFILE_MOVE()
#except FileNotFoundError: 
 #   corp_file.send_email()
