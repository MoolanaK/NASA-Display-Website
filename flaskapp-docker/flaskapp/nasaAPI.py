import requests
import datetime
from datetime import date
import random

class API():
    def __init__(self):
        self.key = 'gRXcBRFY5fKOMMezaPhGUmULp5vLCIOxIumUdynP' ##"ADD APIKEY HERE"
    
    def getCuriosity(self):
        key = self.key
        today = date.today()
        yesterday = today - datetime.timedelta(days=1)
        year = str(yesterday.year)
        month = str(yesterday.month)
        day = str(yesterday.day)
        url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={}-{}-{}&api_key='.format(year, month, day) + key 
        r  = requests.get(url=url)
        data = r.json()
        new_data = data['photos']
        pics=[]
        l = len(new_data) - 1

        for i in range(6):
            rand = random.randint(0, l)
            pics.append(new_data[rand]['img_src'])

        return pics

    def getHubble(self):
        url = 'https://images-api.nasa.gov/search?q=hubble&media_type=image'
        r = requests.get(url = url)
        data = r.json()
        new_data = data['collection']['items']
        pics = []

        l = len(new_data) - 1

        for i in range(6):
            rand = random.randint(0, l)
            pics.append(new_data[rand]['links'][0]['href'])
        
        return pics
        
        