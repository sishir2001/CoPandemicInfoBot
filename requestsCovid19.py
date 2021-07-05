# https://api.covid19api.com/summary -- is the API used .
import requests
from requests.exceptions import Timeout
from datetime import date
session = requests.Session()
response = session.get('https://api.covid19api.com/summary',timeout=(2,5))
json_response = response.json()
global_data = json_response['Global']
todaysdate = date.today()
today = todaysdate.strftime("%B %d, %Y")
summary_data = f"Covid 19 Summary (as of {today})\nNew Confirmed : {global_data['NewConfirmed']}\nTotal Confirmed : {global_data['TotalConfirmed']}\nNew Deaths : {global_data['NewDeaths']}\nTotal Deaths : {global_data['TotalDeaths']}\nNew Recovered : {global_data['NewRecovered']}\nTotal Recovered : {global_data['TotalRecovered']}"
print(summary_data)
