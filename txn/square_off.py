from NorenRestApiPy.NorenApi import PriceType
from datetime import datetime
from pytz import timezone
from login.init import finvasia

def squareoff():
    ret = finvasia.get_positions()

    print(ret)
    if ret is not None:
        for position in ret:
            if position['netqty'] == '0':
                pass
            elif "NIFTY" in position['tsym']:
                qty = int(position['netqty'])
                while qty > 450:
                    finvasia.place_order(buy_or_sell="B", product_type=position['prd'], exchange=position['exch'],
                         tradingsymbol=position['tsym'], quantity=450,
                         price_type=PriceType.Market,
                         retention='DAY', remarks='squaring-off', discloseqty=0)

                    qty -= 450

                if qty > 0:
                    finvasia.place_order(buy_or_sell="B", product_type=position['prd'], exchange=position['exch'],
                                 tradingsymbol=position['tsym'], quantity=qty, price_type=PriceType.Market,
                                 retention='DAY', remarks='squaring-off', discloseqty=0)

                print(position)
