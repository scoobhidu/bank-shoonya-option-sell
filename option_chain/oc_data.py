from login.init import finvasia

oc_call = {}
oc_put = {}

def init_oc():
    data = finvasia.get_quotes(exchange="NSE", token="26009")
    ret = finvasia.get_option_chain(exchange="NFO", tradingsymbol="BANKNIFTY27NOV24P50300", count=40, strikeprice=data['lp'])

    print(ret)

    for option in ret['values']:
        if option['optt'] == "PE":
            global oc_put
            oc_put[int(option['strprc'][:5])] = option

        else:
            global oc_call
            oc_call[int(option['strprc'][:5])] = option

def get_option_sym_from_strike(ltp, call: bool):
    if ltp % 100 != 0:
        if call:
            ltp = ltp - (ltp % 100) + 200
        else:
            ltp = ltp + (100 - (ltp % 100)) - 200

    if call:
        global oc_call
        return oc_call[ltp]['tsym']
    else:
        global oc_put
        return oc_put[ltp]['tsym']

def get_option_token_from_strike(ltp, call: bool):
    if ltp % 50 != 0:
        if call:
            ltp = ltp - (ltp % 100) + 200
        else:
            ltp = ltp + (100 - (ltp % 100)) - 200

    if call:
        global oc_call
        print(oc_call[ltp]['token'])
        return oc_call[ltp]['token']
    else:
        global oc_put
        print(oc_put[ltp]['token'])
        return oc_put[ltp]['token']
