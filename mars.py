import requests 
import json 
import webbrowser

def marsweather():
    f = r"https://api.nasa.gov/insight_weather/?api_key=fFUh6eMbL6vqyXgLPQZ5pfBdgko17upic78Uqwue&feedtype=json&ver=1.0"
    data = requests.get(f)
    API = json.loads(data.text)
    def marsTemruture():
        for i in API:
            return API[i]["AT"]["av"]
    def marsWind():
        for i in API:
            return API[i]["WD"]["most_common"]["compass_point"]
    print(marsTemruture())
    print(marsWind())
print(marsweather())