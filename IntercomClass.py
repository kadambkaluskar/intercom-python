import requests
import json
import os



class IntercomClass :
	global username,password
	#username = os.environ['INTERCOM_USER'] #Deprecated
	#password = os.environ['INTERCOM_PASSWORD'] #Deprecated
	Authorization = os.environ['INTERCOM_AUTH_TOKEN'] ## This will be something like "Bearer dskgjdsgiudv325972ysdhfsdnw98ywefniusfs9gfw="

	global eventsUrl,usersUrl,headerData
	eventsUrl = 'https://api.intercom.io/events'
	usersUrl = 'https://api.intercom.io/users'
	#headerData = {"Content-Type": "application/json"} 
	headerData = {'Content-type': 'application/json', 'Accept': 'application/json','Authorization': Authorization}

	eventsUrl = 'https://api.intercom.io/events'
	usersUrl = 'https://api.intercom.io/users'

	def create_event(self,data) :
		response = requests.post(eventsUrl,auth=(username, password),data=data,headers=headerData)
		return response.text

	def create_user(self,data) :
		response = requests.post(usersUrl,auth=(username, password),data=data,headers=headerData)
		return response.text

	def delete_user(self,data) :
		response = requests.delete(usersUrl,auth=(username, password),data=data,headers=headerData)
		return response.text
