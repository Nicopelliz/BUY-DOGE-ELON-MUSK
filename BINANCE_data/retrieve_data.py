import websocket, json, pprint
from datetime import datetime
import os.path
import telegram
from decouple import config

#notifica telegram
def notify_ending(message):
     
    token = config('TOKEN')
    chat_id = config('CHAT_ID')  
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)

SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m/ethusdt@kline_1m/xrpusdt@kline_1m/zecusdt@kline_1m/dogeusdt@kline_1m/ltcusdt@kline_1m/zrxusdt@kline_1m"

data = []
current_day = datetime.now().day
current_month = datetime.now().strftime('%B')
os.makedirs(f'DATA_new/{current_month}', exist_ok=True)


def on_open(ws):
    print('connection is on')


def on_close(ws):
    message = 'raccogli dati dal binance websocket CLOSED'
    notify_ending(message)
    print('close connection')


def on_message(ws, message):
    global data
    global current_day
    global current_month
    json_data = json.loads(message)
    
    is_candle_close = json_data['k']['x']

    if is_candle_close:

        if current_day != datetime.now().day:

            with open(f'DATA_new/{current_month}/json_data-{current_day}.json', 'w') as json_file:
                json.dump(data, json_file)

            if current_month != datetime.now().strftime('%B'):
                current_month = datetime.now().strftime('%B')
                os.makedirs(f'DATA_new/{current_month}')

            current_day = datetime.now().day
            data = []
            
        data.append(json_data)


ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()


