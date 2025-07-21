from fastapi import Request, FastAPI

from login.init import login
from option_chain.oc_data import init_oc
from option_chain.option_ltp import get_nifty_price
from txn.place_order import place_order
import txn.square_off
from txn.square_off import squareoff

app = FastAPI()

login()
init_oc()

@app.get("/login")
async def root():
    login()
    init_oc()
    return {"message": "login request placed"}

@app.post("/call")
async def call(req: Request):
    txn.square_off.squareoff()

    ltp = get_nifty_price()
    if ltp is not int:
        ltp = int(ltp[:5])

    place_order(ltp, True)

    return {"message": f"action -- buy"}


@app.post("/put")
async def put(req: Request):
    txn.square_off.squareoff()

    ltp = get_nifty_price()
    if ltp is not int:
        ltp = int(ltp[:5])

    place_order(ltp, False)

    return {"message": f"action -- sell"}

@app.post("/decide")
async def call(req: Request):
    txn.square_off.squareoff()
    ltp = get_nifty_price()
    if ltp is not int:
        ltp = int(ltp[:5])

    if (await req.json()['action']) == "B":
        place_order(ltp, True)
        return {"message": f"action -- buy"}
    else:
        place_order(ltp, False)
        return {"message": f"action -- sell"}


@app.get("/square_off")
async def square_off():
    squareoff()
    return {"message": f"squared off open NIFTY* positions"}
