import json
import requests

from config import USER, jkey


def get_order_margin(order):
    url = "https://api.shoonya.com/NorenWClientTP/GetOrderMargin"

    # prepare the data
    values = {'ordersource': 'API'}
    values["uid"] = USER
    values["actid"] = USER
    values["trantype"] = 'S'
    values["prd"] = 'M'
    values["exch"] = "NFO"
    values["tsym"] = order['tsym']
    values["qty"] = '15'
    values["prctyp"] = 'MKT'
    values['prc'] = f"order['prc']"
    values["ret"] = 'DAY'
    values["remarks"] = "profit"

    payload = 'jData=' + json.dumps(values) + f'&jKey={jkey["key"]}'

    response = requests.post(url, data=payload)

    return float(response.json()['ordermargin'])