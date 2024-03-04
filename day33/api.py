import requests
import datetime as dt
import smtplib

EMAIL = "deddia.programmer@gmail.com"
PASSWORD = ""

LAT = 0
LONG = 0


def iss_location():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    longitude = float(iss_response.json()["iss_position"]["longitude"])
    latitude = float(iss_response.json()["iss_position"]["latitude"])
    print(longitude)
    print(latitude)

    if LAT-5 <= latitude <= LAT+5 and LONG-5 <= longitude <= LONG+5:
        return True


def night_time():
    parameters = {
        "lat": LAT,
        "lng": LONG,
        "tzid": "Asia/Jakarta",
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)

    now = dt.datetime.now()
    if now.hour >= sunset or now.hour <= sunrise:
        return True


if iss_location() and night_time():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="deddiapermana97@gmail.com",
                            msg="Subject: ISS Notification\n\nLook up! The ISS is above you")
