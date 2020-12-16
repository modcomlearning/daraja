

# here
from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import time
import base64
import json

timestamp = str(time.strftime("%Y%m%d%H%M%S"))
password = base64.b64encode(bytes(u'174379' + 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919' + timestamp, 'UTF-8'))


consumer_key = "TLEbdlzeI1YMFikSnU9YyAxpqzqG4BJG"
consumer_secret = "wFYDiA6LSRyOa6Zv"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

y = json.loads(requests.get(api_URL, auth=HTTPBasicAuth(consumer_key,consumer_secret)).text)
print(y['access_token'])

access_token = "{}".format(y['access_token'])
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = { "Authorization": "Bearer {}".format(access_token)}
request = {
    "BusinessShortCode": "174379",
    "Password": "{}".format(password),
    "Timestamp": "{}".format(timestamp),
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "1",
    "PartyA": "254729225710",
    "PartyB": "174379",
    "PhoneNumber": "254729225710",
    "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
    "AccountReference": "account",
    "TransactionDesc": "account"
}


response = requests.post(api_url, json = request, headers=headers)
print(response.text)

