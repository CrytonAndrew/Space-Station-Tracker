import requests
import datetime as dt
import smtplib

lat = -26.20227
lng = 28.04363

MY_EMAIL = "@gmail.com"
MY_PASSWORD = ""


response = requests.get(url="http://api.open-notify.org/iss-now.json", )
response.raise_for_status()

data = response.json()
coordinates = data["iss_position"]
latitude = coordinates["latitude"]
longitude = coordinates["longitude"]


now = dt.datetime.now()

daytime_response = requests.get("https://api.sunrise-sunset.org/json?lat=-26.20227&lng=28.04363&formatted=0")
daytime_response.raise_for_status()
date = daytime_response.json()
sunset = date["results"]["sunset"].split("T")[1].split(":")[0]
sunrise = date["results"]["sunrise"].split("T")[1].split(":")[0]

current_hour = now.time().hour

if current_hour + 1 == int(sunset):
    if latitude == lat and longitude == lng:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="",
                msg=f"Subject: Space Station Passing\n\n Coordinates:\nLat->{latitude} \nLong:{longitude}")






