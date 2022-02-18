"""
This file will write incoming data from the streamer to a file.
"""
import time
from datetime import datetime
from pytz import timezone

def processor(data):
    """
    This function will write the data to a file.
    Args:
        api_key (str): The Kite Trade API key
        data: The data to be written to a file

    Raises:
        Exception: In case the data is not in the correct format

    Returns:
        
    """
    times = [(time.time()-40000)]
    # make the string format for the date
    strdate = datetime.now(timezone('UTC')).astimezone(timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S")
    print(data)

    for i in data:
        # print(f'{strdate}:{i["instrument_token"]}:{i["last_price"]}')
        with open(f'./realtime/prices/{i["instrument_token"]}.csv', 'a+') as f:
            f.write(f"{strdate},{i['last_price']},{i['last_quantity']},{i['buy_quantity']},{i['sell_quantity']},{i['average_price']},{i['volume']},{i['change']}\n")
        with open(f'./realtime/depth/{i["instrument_token"]}.csv', 'a+') as f:
            try: 
                for j in i['depth']['sell']:
                    f.write(f"{strdate},S,{j['price']},{j['orders']},{j['quantity']}\n")
            except:
                pass
            try:
                for j in i['depth']['buy']:
                    f.write(f"{strdate},B,{j['price']},{j['orders']},{j['quantity']}\n")
            except:
                pass

