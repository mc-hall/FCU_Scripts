import requests, time, datetime, urllib, bs4, shutil, os, re, zipfile


def AM():
	if 'AMACH' in a_files.text:
		ach = urllib.parse.urljoin(site_url,ach_files['href'])
		req5 = s.get(ach)
		output = open('\\\\Directory\\file','wb')
		output.write(req5.content)
		output.close()
		print('AMACH downloaded.')

def PM():
	if 'PMACH' in ach_files.text:
		ach = urllib.parse.urljoin(site_url,ach_files['href'])
		req6 = s.get(ach)
		output = open('\\\\Directory\\file','wb')
		output.write(req6.content)
		output.close()
		print('PMACH downloaded.')

def all_files():
	if 'all-files.zip' in ach_files.text:
		ach = urllib.parse.urljoin(site_url,ach_files['href'])
		req7 = s.get(ach)
		output = open('\\\\Directory\\file','wb')
		output.write(req7.content)
		output.close()
		print('All_files.zip downloaded.')

def unzip():
	unzip_dir = '\\\\Directory\\file\\'
	zipped = '_Files.zip'
	if zipped in os.listdir(unzip_dir):
		zipfile.ZipFile(os.path.join(unzip_dir,zipped)).extractall(unzip_dir)

#Log into website
with requests.Session() as s:
	login_page = s.get(site_url,headers=headers)
	soup = bs4.BeautifulSoup(login_page.text,'html.parser')
	s.post(site_url+soup.form['action'],data=payload)
	
	#Find file daily link for FEDLINE files
	req2 = s.get(browse_asp)
	soup3 = bs4.BeautifulSoup(req2.text,'html.parser')
	for link in soup3.findAll('a'):
		if '_FILES' in link.text:
			fedach_url = urllib.parse.urljoin(site_url,link['href'])
			req3 = s.get(fedach_url)
			soup4 = bs4.BeautifulSoup(req3.text,'html.parser')
			
			#Search FEDACH filepage page for date links
			for ach_link in soup4.findAll('a'):
				if todays_date in ach_link.text:
					todays_ach = urllib.parse.urljoin(site_url,ach_link['href'])
					req4 = s.get(todays_ach)
					soup5 = bs4.BeautifulSoup(req4.text,'html.parser')

					#Search date links for todays files, download & save to text file
					for ach_files in soup5.findAll('a'):
						all_files()

unzip()


	

	
