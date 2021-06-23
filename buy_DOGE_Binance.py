from concurrent.futures import ThreadPoolExecutor
# generic imports
from logging import exception
import pprint, requests, datetime, time, math
from decouple import config
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
my_twitter_id = 'your_twitter_ID' # Per fare i test del programma
elon_musk_twitter_id = 44196397
twitter_id = elon_musk_twitter_id
seconds_sleep = 100

# lista parametri per ordini:

binance_parameters = [
        {'id':'Account1',
        'api_key':config("Account1_API_KEY_binance"),
        'api_secret':config("Account1_API_SECRET_binance"),
        'asset':['BTC',0.97], # ASSET con cui comprare DOGE e rispettiva percentuale (rispetto al totale nell'account) da utilizzare per le transazioni
        'symbol':'DOGE',
        'quantity':'',
        'active':True # True o False determina se questo particolare verrà utilizzato o no nella funzione che genera le transazioni   
        },
        {'id':'Account2',
        'api_key':config('Account2_API_KEY_binance'),
        'api_secret':config('Account2_API_SECRET_binance'),
        'asset':['BTC',0.35],
        'symbol':'DOGE',
        'quantity':'',
        'active':False
        },
        {'id':'Account3',
        'api_key':config('Account3_API_KEY_binance'),
        'api_secret':config('Account3_API_SECRET_binance'),
        'asset':['BTC',0.6],
        'symbol':'DOGE',
        'quantity':'',
        'active':True
        },
    ]

# TELEGRAM TELEGRAM
# notifica alla chat di telegram
def notify_ending(message):
        
    token = config('TOKEN')
    chat_id = config('CHAT_ID')  
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)

# acquista DOGE seguendo le istruzioni presenti nei parametri
def buy_doge_binance(parameters):

    if parameters['active']==True:

        client = Client(api_key=parameters['api_key'], api_secret=parameters['api_secret'])

        asset = parameters['asset']
        symbol=parameters['symbol']
        trade_symbol = f"{symbol}{asset[0]}"

        balance = float(client.get_asset_balance(asset=asset[0])['free'])
        avg_price = float(client.get_avg_price(symbol=trade_symbol)['price'])
        rounded_price = math.floor(avg_price*10000000)/10000000
        quantity = math.floor((balance*asset[1])/rounded_price)

        try:
            order = client.order_market_buy(
            symbol=trade_symbol,
            quantity=quantity)
            
            
        except Exception as e:
            print(e)
            message = f'{parameters["id"]} : errore nel acquisto'
            notify_ending(message)
        
        saldo = f"{parameters['id']} saldo {asset[0]}: {balance}"
        notify_ending(saldo)
        message = f'{parameters["id"]} : acquistato {quantity} di {symbol} con {asset[0]}!!!!!!!!!'
        notify_ending(message)
        
        return quantity

# vende DOGE seguendo le istruzioni presenti nei parametri
def sell_doge_binance(parameters):

    if parameters['active']==True:

        client = Client(api_key=parameters['api_key'], api_secret=parameters['api_secret'])
        asset = parameters['asset']
        symbol=parameters['symbol']
        trade_symbol = f"{symbol}{asset[0]}"
        quantity = parameters['quantity']-1
    
        try:
            order = client.order_market_sell(
            symbol=trade_symbol,
            quantity=quantity)
            
            message = f'{parameters["id"]} : venduto {quantity} di {symbol} con {asset[0]}!!!!!!!!!'
            notify_ending(message)
            
        except Exception as e:
            print(e)
            message = f'{parameters["id"]} : errore nella vendita'
            notify_ending(message)
        
        balance = float(client.get_asset_balance(asset=asset[0])['free'])
        saldo = f"{parameters['id']} saldo {asset[0]}: {balance}"
        notify_ending(saldo)

# TWITTER stream listener che registra ogni nuovo tweet scritto da Elon Musk    
while True:

    try:

        auth = OAuthHandler(config('API_KEY'), config('API_SECRET'))
        auth.set_access_token(config('ACCESS_TOKEN'), config('ACCESS_TOKEN_SECRET'))
        

        class MyStreamListener(StreamListener):
            
            def on_status(self, status):             
                start_time = time.time()
                if status.user.id == twitter_id:
                    
                    if word_to_check in status.text.lower() and str(status.in_reply_to_status_id) == 'None':                   

                        with ThreadPoolExecutor() as executor:   
                            quantities = executor.map(buy_doge_binance, binance_parameters)
                            
                        print(time.time()-start_time)
                        
                        dt = datetime.datetime.now()
                        message = f"[{dt.strftime('%H:%M:%S')}] {status.user.name.upper()}:{status.created_at} {status.text}"
                        notify_ending(message)
                        print(message)
                        
                        i=0
                        for quantity in quantities:
                            binance_parameters[i]['quantity']=quantity
                            i+=1

                        time.sleep(seconds_sleep)

                        with ThreadPoolExecutor() as executor:   
                            executor.map(sell_doge_binance, binance_parameters)

                        print(time.time()-start_time)
                    
                    elif word_to_check in status.text.lower() and not str(status.in_reply_to_status_id) == 'None':
                        dt = datetime.datetime.now()
                        message = f"[{dt.strftime('%H:%M:%S')}] {status.user.name.upper()}:{status.created_at} {status.text}"
                        notify_ending(message)
                        print(message)
                        appunto = 'DOGE presente nel TWEET'
                        notify_ending(appunto)
                    
                    else:
                        dt = datetime.datetime.now()
                        message = f"[{dt.strftime('%H:%M:%S')}] {status.user.name.upper()}:{status.created_at} {status.text}"
                        notify_ending(message)
                        print(message)
                    

        api = API(auth, wait_on_rate_limit=True)
        myStreamListener = MyStreamListener()
        myStream = Stream(auth = auth, listener=myStreamListener)
        myStream.filter(follow=[str(twitter_id)])
        

    except Exception as e:
        print(e)

        
    time.sleep(1)



