from datetime import datetime
from pytz import timezone

from NorenRestApiPy.NorenApi import PriceType

import wallet.get_margin
from config import USER
from login.init import finvasia
from option_chain.oc_data import get_option_sym_from_strike
from option_chain.option_ltp import get_option_ltp
from txn.get_order_margin import get_order_margin


def place_order(ltp, call: bool):
    option_ltp = get_option_ltp(ltp, call)
    required_margin = get_order_margin({
        'tsym': get_option_sym_from_strike(ltp, False if call else True),
        'prc': option_ltp,
    })
    qty = (wallet.get_margin.m // required_margin) * 75

    print(f"Qty: {qty}")

    while qty > 450:
        if call:
            res = finvasia.place_order(
                buy_or_sell='S',
                product_type="M", exchange="NFO", tradingsymbol=get_option_sym_from_strike(ltp, False),
                quantity= 450, price_type=PriceType.Market, retention='DAY', remarks='call-sell', discloseqty=0,
            )

            print(res)

        else:
            res = finvasia.place_order(
                buy_or_sell='S',
                product_type="M", exchange="NFO", tradingsymbol=get_option_sym_from_strike(ltp, True),
                quantity= 450, price_type=PriceType.Market, retention='DAY', remarks='put-sell', discloseqty=0,
            )

            print(res)

        qty -= 450

    if qty > 0:
        if call:
            res = finvasia.place_order(
                buy_or_sell='S',
                product_type="M", exchange="NFO", tradingsymbol=get_option_sym_from_strike(ltp, False),
                quantity=qty, price_type=PriceType.Market, retention='DAY', remarks='call-sell', discloseqty=0,
            )

            print(res)

        else:
            res = finvasia.place_order(
                buy_or_sell='S',
                product_type="M", exchange="NFO", tradingsymbol=get_option_sym_from_strike(ltp, True),
                quantity=qty, price_type=PriceType.Market, retention='DAY', remarks='put-sell', discloseqty=0,
            )

            print(res)