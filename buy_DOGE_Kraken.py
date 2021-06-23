# generic imports
import time, requests, datetime
from decouple import config
import urllib.parse, hashlib, hmac, base64,math
# twitter imports 
from tweepy import API
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
# telegram 
import telegram
# binance imports
from binance.client import Client
from binance.enums import *

# lista di costanti utili:
word_to_check = 'doge'
symbol_BTC = 'DOGEBTC'
my_twitter_id = 'your_twitter_ID' # Per fare i test
elon_musk_twitter_id = 44196397
twitter_id = my_twitter_id
seconds_sleep = 40

# TELEGRAM TELEGRAM
def notify_ending(message):
        
    token = config('TOKEN')
    chat_id = config('CHAT_ID')  
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)

################################################################

# KRAKEN KRAKEN KRAKEN KRAKEN KRAKEN KRAKEN KRAKEN KRAKEN KRAKEN

#costanti per l'autenticazione
kraken_api_url = "https://api.kraken.com"
kraken_key = config('kraken_key')
kraken_secret = config('kraken_private_key')


# crea la firma con cui autenticarsi
def get_kraken_signature(urlpath, data, secret):

    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()

    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()

# Attaches auth headers and results of a POST request
def kraken_request(uri_path, data, api_key, api_sec):
    headers = {}
    headers['API-Key'] = api_key
    # get_kraken_signature() as defined in the 'Authentication' section
    headers['API-Sign'] = get_kraken_signature(uri_path, data, api_sec)             
    req = requests.post((kraken_api_url + uri_path), headers=headers, data=data)
    return req

# EFFETTUA UN ORDINE A PREZZO DI MERCATO
def market_order(crypto,type, quantity, symbol):

    if type == 'buy':
        azione="acquisto"
    elif type=='sell':
        azione='vendita'

    order_executed = kraken_request('/0/private/AddOrder', {
        "nonce": str(int(1000*time.time())),
        "ordertype": "market",
        "type": type,
        "volume": quantity,
        "pair": symbol
    }, kraken_key, kraken_secret)
    
    if order_executed.json()['error'] == []:
        message = f'KRAKEN: {azione} {quantity} di {crypto.upper()} con {symbol[-3:].upper()}!!!!!!!!!'
        notify_ending(message)
    
    else:
        print(order_executed.json()['error'])
        message = f"KRAKEN: errore nella {azione} di {crypto.upper()} con {symbol[-3:].upper()}!!!!!!!!!"
        notify_ending(message)

def buy_doge_kraken(crypto, symbol_BTC):

    #CANCELLA TUTTI GLI ORDINI PRESENTI
    cancel_orders = kraken_request('/0/private/CancelAll', {
        "nonce": str(int(1000*time.time())),
        "trades": True
    }, kraken_key, kraken_secret)

    if cancel_orders.json()['error']!=[]:
        notify_ending(cancel_orders.json()['error'])

    # VERIFICA IL SALDO BTC E IL PREZZO DOGE
    balance = kraken_request('/0/private/Balance', {
        "nonce": str(int(1000*time.time())),
    }, kraken_key, kraken_secret)
    balance_btc = float(balance.json()['result']['XXBT'])

    info_dogebtc = requests.get('https://api.kraken.com/0/public/Ticker?pair=DOGEBTC', {})
    PRICE_dogebtc = float(info_dogebtc.json()['result']['XXDGXXBT']['c'][0])

    QUANTITY_dogebtc = round((balance_btc*0.5)/PRICE_dogebtc) 

    type='buy'

    #COMPRA DOGE CON BTC A PREZZO DI MERCATO
    market_order(
        crypto=crypto,
        type=type, 
        quantity=QUANTITY_dogebtc, 
        symbol=symbol_BTC,
        )
    
    saldo_btc = f"KRAKEN: saldo BTC {round(balance_btc,6)}"
    notify_ending(saldo_btc) 


def sell_doge_kraken(crypto, symbol_BTC):

    balance = kraken_request('/0/private/Balance', {
        "nonce": str(int(1000*time.time())),
    }, kraken_key, kraken_secret)

    quantity_DOGE = math.floor(float(balance.json()['result']['XXDG'])*0.997)
    
    # VENDE AL PREZZO DI MERCATO LA QUANTITà
    type='sell'
    
    market_order(
        crypto=crypto,
        type=type, 
        quantity=quantity_DOGE, 
        symbol=symbol_BTC,
        )

    # VERIFICA IL NUOVO SALDO IN BTC E EURO 
    balance = kraken_request('/0/private/Balance', {
        "nonce": str(int(1000*time.time())),
    }, kraken_key, kraken_secret)

    balance_btc = float(balance.json()['result']['XXBT'])

    saldo_btc = f"KRAKEN: saldo BTC {round(balance_btc,6)}"


    notify_ending(saldo_btc)

    #RICREA TUTTI GLI ORDINI CHE ERANO CANCELLATI PRIMA
    closed_orders = kraken_request('/0/private/ClosedOrders', {
    "nonce": str(int(1000*time.time())),
    "start": int(time.time())-(seconds_sleep+20),
    "closetime": "close",
    }, kraken_key, kraken_secret)
    orders = closed_orders.json()
    order_list = list(orders['result']["closed"].items())
    
    for order in order_list:
        order_details = order[1]
        
        if order_details['status'] == 'canceled' and order_details["descr"]["ordertype"] == 'limit':

            type = order_details["descr"]["type"]
            vol = order_details['vol']
            pair = order_details["descr"]["pair"]
            price = order_details["descr"]["price"]

            print(type,vol,pair,price)

            order_executed = kraken_request('/0/private/AddOrder', {
                "nonce": str(int(1000*time.time())),
                "ordertype": "limit",
                "type": type,
                "volume": vol,
                "pair": pair,
                "price":price
            }, kraken_key, kraken_secret)
            if order_executed.json()['error'] == []:
                print('eseguito')

            else:
                print(order_executed.json()['error'])   

#####################################################################
                
    
#listener che ascolta l'API di TWITTER

while True:

    try:

        auth = OAuthHandler(config('API_KEY'), config('API_SECRET'))
        auth.set_access_token(config('ACCESS_TOKEN'), config('ACCESS_TOKEN_SECRET'))
        

        class MyStreamListener(StreamListener):
            
            def on_status(self, status):             
                
                if status.user.id == twitter_id:
                    dt = datetime.datetime.now()
                    message = f"[{dt.strftime('%H:%M:%S')}] {status.user.name.upper()}: {status.text}"
                    notify_ending(message)
                    print(status.text)
        
                    if word_to_check in status.text.lower():
                        
                        if str(status.in_reply_to_status_id) == 'None':

                            start_time = time.time()
                            buy_doge_kraken(word_to_check, symbol_BTC)

                            print(time.time()-start_time)

                            time.sleep(seconds_sleep)
                       
                            sell_doge_kraken(word_to_check, symbol_BTC)
                            

        api = API(auth, wait_on_rate_limit=True)
        myStreamListener = MyStreamListener()
        myStream = Stream(auth = auth, listener=myStreamListener)
        myStream.filter(follow=[str(twitter_id)])
        

    except Exception as e:
        print(e)

        
    time.sleep(1)




