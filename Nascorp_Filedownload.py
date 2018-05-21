import os,zipfile, sys, shutil, time, textwrap, smtplib, email.message
from datetime import date, timedelta
from ftplib import FTP, FTP_TLS


#Date formatting
today = time.strftime("%A")
yesterday = date.today() - timedelta(1)
yestprod = yesterday.strftime('%Y'+'-'+'%m'+'-'+'%d')

#Dated Production Folders
friday = date.today() - timedelta(3) 
friprod = friday.strftime('%Y'+'-'+'%m'+'-'+'%d')
new_prod_yest = time.strftime('%Y')+'-'+time.strftime('%m')+ ' '+time.strftime('%b')
new_prod_fri = friday.strftime('%Y')+'-'+friday.strftime('%m')+ ' '+friday.strftime('%b')


class TheClass():

    def __init__(self):
        print("")

    #Unzip archive folder
    def IMGFILE_UNZIP(imagefile):
        """ Unzip the folder downloaded"""
        for f in os.listdir(chksrc):
                if f.startswith("987654321") and f.endswith(".zip"):
                    zipfile.ZipFile(os.path.join(chksrc,f)).extractall(chksrc)
                    print(f, " unzipped!")
        
    #Copy files within archive folder to nascorp extract
    def IMGFILE_COPY(imagefile):
        """ Copy all files from within new unzipped folder to production extraction folder"""
        list_files = os.walk(vision_root)
        for root, dirs, files in list_files:
            print('Copying...', files)
            for f in files:
                if f.endswith(file_pattern):
                    filename = os.path.join(root,f)
                    filename_prefix = f.split('-')[0]
                    shutil.copy(os.path.join(root,filename_prefix), os.path.join(nascorp,filename_prefix))
                    print(filename_prefix)

    #Move archive folder to daily production folder
    def IMGFILE_MOVE(imagefile):
        """Look for the zip folder and move to previous days' production folder on a specific day"""
        for f in os.listdir(chksrc):
                if f.startswith("987654321") and f.endswith(".zip"):
                    print('Moving ', f)
                    date1 = "Monday"
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
    def SEND_EMAIL(self):
        """Sends an email to myelf """
        sender = 'me@my_email.org'
        receiver = 'me@my_email.org'
        password = 'my_email_pw'
        smtpsrv = 'email.service.com'
        body = '\n\n Could not download nascorp files \n'
        message = 'Subject: Wescorp File download failure'.format()
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
        """Connect to companys's FTP and download the zip folder within"""
        password = 'ftp_password'
        directory = '/folder/'
        ftps = FTP_TLS('123.456.789.000')
        ftps.login(user='user', passwd=password)
        ftps.prot_p()
        cur_dir = ftps.cwd(directory)
        new_files = ftps.nlst()
        print(ftps.pwd())
        for items in new_files:
            if items.startswith('987654321') and items.endswith('.zip'):
                print(items)
                local_file = os.path.join(chksrc, items)
                f = open(local_file, 'wb')
                ftps.retrbinary('RETR %s' % items, f.write)
                f.close()
                return True
        
        
try:
    nascorp_file = TheClass()
    nascorp_file.FTP_DOWNLOAD()
    nascorp_file.IMGFILE_UNZIP()
    nascorp_file.IMGFILE_COPY()
    nascorp_file.IMGFILE_MOVE()
except FileNotFoundError: 
    nascorp_file.send_email()