import pyotp
from NorenRestApiPy.NorenApi import NorenApi

from config import USER, PASSWORD, VENDOR_CODE, API_KEY, IMEI, AUTH2_TOKEN, jkey

finvasia = NorenApi( host='https://api.shoonya.com/NorenWClientTP/', websocket='wss://api.shoonya.com/NorenWSTP/')


def login():
    totp = pyotp.TOTP(AUTH2_TOKEN).now()

    ret = finvasia.login(userid=USER, password=PASSWORD, twoFA=totp, vendor_code=VENDOR_CODE, api_secret=API_KEY, imei=IMEI)
    print(ret)

    jkey['key'] = (ret['susertoken'])