import requests

class OpenWeather():
    def __init__(self):
        pass
            
    def getData(self, apiKey, city):
        params = {"APPID":apiKey,"q":city,"units":"metric","lang":"de"}
        url = "https://api.openweathermap.org/data/2.5/forecast?"
        data = requests.get(url, params=params)

        if data.status_code != 200:
            print("api request error!")
            return dict(temp = -999,
                        temp_min = -999,
                        temp_max = -999,
                        pressure = -999,
                        humidity = -999,
                        wind_speed = -999,
                        clouds_all = -999,
                        description = -999,
                        status = f"api request error - status code: {data.status_code}")

        weather = data.json()
    
        try:
            dictWeather = dict(temp = weather["list"][0]["main"]["temp"], 
                               temp_min = weather["list"][0]["main"]["temp_min"], 
                               temp_max = weather["list"][0]["main"]["temp_max"], 
                               pressure = weather["list"][0]["main"]["pressure"],
                               humidity = weather["list"][0]["main"]["humidity"],
                               wind_speed = weather["list"][0]["wind"]["speed"],
                               clouds_all = weather["list"][0]["clouds"]["all"],
                               description = weather["list"][0]["weather"][0]["description"],
                               status = f"OK - status code: {data.status_code}")
            return dictWeather
        except:
            return dict(temp = -999,
                        temp_min = -999,
                        temp_max = -999,
                        pressure = -999,
                        humidity = -999,
                        wind_speed = -999,
                        clouds_all = -999,
                        description = -999,
                        status = f"data decrypt error - status code: {data.status_code}")
    