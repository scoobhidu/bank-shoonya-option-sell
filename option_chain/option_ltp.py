from login.init import finvasia
from option_chain.oc_data import get_option_token_from_strike

def get_nifty_price():
    res = finvasia.get_quotes(exchange="NSE", token="26009")
    print(res)

    return res['lp']

def get_option_ltp(ltp, call: bool):
    res = finvasia.get_quotes(exchange="NFO", token=str(get_option_token_from_strike(ltp, call=call)))

    print(res)
    return float(res['lp'])
