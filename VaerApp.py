import requests
url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
parametre = {"lat": 59.91, "lon": 10.75}   # Oslo sine koordinater
headers = {"User-Agent": "min-vaerapp/1.0 Sanchay.thaya@outlook.com"}

svar = requests.get(url, params=parametre, headers=headers)

print("Statuskode:", svar.status_code)
print(svar.text[:1000])