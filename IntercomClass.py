import requests
import json
import env

global environment
environment = env.environment


class IntercomClass :
	global username,password
	if environment == 'development' :
		username = "hhyy7766"
		password = "fkhsdhguifisdguisduigisdnfvsdhfgsdhgsgus"

	elif environment == 'testing' :
		username = "nbvcxzas"
		password = "fjdsbgjksdjghijsgdgisdgisdiuguidsisisdgi"

	elif environment == 'production' :
		username = "qwertyui"
		password = "dshghfsjdhghsduihgihsdiughsdhuioghsdguu"

	global eventsUrl,usersUrl,headerData
	eventsUrl = 'https://api.intercom.io/events'
	usersUrl = 'https://api.intercom.io/users'
	headerData = {"Content-Type": "application/json"}

	def create_event(self,data) :
		response = requests.post(eventsUrl,auth=(username, password),data=data,headers=headerData)
		return response.text

	def create_user(self,data) :
		response = requests.post(usersUrl,auth=(username, password),data=data,headers=headerData)
		return response.text

	def delete_user(self,data) :
		response = requests.delete(usersUrl,auth=(username, password),data=data,headers=headerData)
		return response.text

