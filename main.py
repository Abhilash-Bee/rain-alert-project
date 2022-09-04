# import requests
# import smtplib
# import os
#
# USER_NAME = os.environ.get("USER_NAME")
# PASSWORD = os.environ.get("PASSWORD")
# MY_LAT = 12.9762
# MY_LNG = 77.6033
#
# parameters = {
#     "q": "Bangalore,India",
#     "appid": "cce28d0a7e58f87a14f071af8aef2bbd",
# }
#
# response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
# response.raise_for_status()
# data = response.json()
# if int(data["weather"][0]["id"]) < 700:
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=USER_NAME, password=PASSWORD)
#         connection.sendmail(
#             from_addr=USER_NAME,
#             to_addrs=USER_NAME,
#             msg="Subject: Bee Alert\n\n""Take the Umbrella Bee!!!")
#         print("Sent Successful")
#

import requests
from twilio.rest import Client
MY_LAT = 12.9762
MY_LNG = 77.6033

account_sid = "AC7673838147a32dec9453c2b1ad8c3779"
auth_token = "b50da18f8e5b58abc3c3a27ec5216c8b"

parameters = {
    "q": "Bangalore,India",
    "appid": "cce28d0a7e58f87a14f071af8aef2bbd",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = response.json()
if int(data["weather"][0]["id"]) < 700:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body="It's going to rain. Please take the umbrella",
                         from_="+19094871753",
                         to="+919066569822"
                     )

    print(message.sid)
