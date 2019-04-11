from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests, json

class ActionGetWeather(Action):

    def name(self):
        return "action_get_weather"

    def run(self, dispatcher, tracker, domain):
        gpe = tracker.get_slot('GPE')
        api_key = "b8da253123ef38357c4c4f02843e2fc3"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + gpe + "&units=metric"
        response = requests.get(complete_url)
        res = response.json()

        if res["cod"] != "404":
            mainRes = res["products"]
            current_temperature = mainRes["temp"]
            current_pressure = mainRes["pressure"]
            current_humidiy = mainRes["humidity"]

            sysRes = res["sys"]
            country = sysRes["country"]
            name = res["name"]

            z = res["weather"]
            weather_description = z[0]["description"]

            dispatcher.utter_message("Its " + str(current_temperature) + "°c in " + str(name) + "," + str(country) +
                                     " with " + str(weather_description) + " and humidity level of " + str(
                current_humidiy) + "%")
        else:
            dispatcher.utter_message("City Not Found ")
        return
