from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from canvas2dropbox import selenium_test
import time
import sys
import requests
import subprocess

access_token = "7~Kh0OqHcSsGIdKIiZHBIxFBv0wwpoZinb1vxicmipU6eG7dlJoRGkzJllTOEEUxCX"
course_id = str(803405)
url="https://canvas.instructure.com/api/v1/courses/{}/folders/root".format(course_id)
urlCourse="https://canvas.instructure.com/api/v1/courses/{}".format(course_id)
params={"access_token": access_token}
reqName=requests.get(urlCourse, params=params)
courseInfo=reqName.json()
courseName=courseInfo['name']

#first call of this should have location be root folder "/", name is the courseName, folder is rootInfo
def loop_through_folders(location, name, folder):
	if folder['files_count']>0:
		reqFiles=requests.get(folder['files_url'], params=params)
		filesInfo=reqFiles.json()
		for item in filesInfo:
			fileAddress=item['url']
			fileName=item['display_name']
			test.download(fileAddress)
			subprocess.call("find_most_recent.sh",shell=True)

	if folder['folders_count']>0:
		reqFolders=requests.get(folder['folders_url'], params=params)
		foldersInfo=reqFolders.json()
		for item in foldersInfo:
			loop_through_folders("{}/{}/".format(location, item['name']), item['name'], item)
	return


r=requests.get(url, params=params)
rootInfo=r.json()
loop_through_folders("/{}/".format(courseName),"", rootInfo)



