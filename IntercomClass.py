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

	global eventsUrl
	eventsUrl = 'https://api.intercom.io/events'

	def create_event(self,data) :		
		headerData = {"Content-Type": "application/json"}
		response = requests.post(eventsUrl,auth=(username, password),data=data,headers=headerData)
		return response.text
