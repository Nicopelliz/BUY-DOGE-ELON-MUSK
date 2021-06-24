### ENGLISH ENGLISH ENGLISH (ITALIANO IN FONDO)

### IMPORTANT! : i'm not a financial adviser and i will not assume in any way shape or form responsibility if something goes wrong with the script. If you gain some money i will cheer for you! For me that has worked very well in the past months...


# BUY-DOGE-ELON-MUSK

### SHORT DESCRIPTION:

These scripts allow you to AUTOMATE the buying CRYPTOCURRENCY when meeting a certain condition from a TWITTER stream listener

## GET CLEAN AND USABLE DATA FROM BINANCE WEBSOCKET 

#### From folder "BINANCE_data"
1)Use the file "retrieve_data.py" to connect to Binance Websocket and start retrieving coin data (change the stream URL if you wish to change the coin pairs). The script will than store the data creating a new json file every day.

2)Use the file "clean_display_data.ipynb" to clean and plot the data. In this case i choosed to analyze DOGE coin price chart

## GET ALL THE TWEETS FROM CHOOSEN TWITTER PROFILE

#### In this case i choosed to scrape Elon Musk twitter profile

#### From folder " TWITTER_data"
1)Use the file "scrapeHTML_ElonMusk_Twitter.ipynb" using jupyter notebook to scrape the tweets from the HTML. This file will collect the text of the tweets and put them in a csv file. Use your personal account to enter twitter (to be sure to not missing tweets). Change the "SCROLL_TIME" in relation to how fast is your internet connection (remember if you go too fast twitter will prevent you from keep scrolling), you will have to try several times before getting a good result. You will always end up with many duplicates but it's fine: it's better to have duplicates than missing some tweets.

2) In case the result is not sufficient, try scraping the API with TWEEPY with "scrapeAPI_ElonMusk_Twitter.ipynb"(or "scrapeAPI_ElonMusk_Twitter.py"). 

NOTE: TWITTER has changed often the rules for using its API and also how much you can scroll down, giving both of these some big restrictions! I was lucky that when i first used those script i could go a lot back in time with scraping the HTML so it was sufficient.


## ANALIZE THE DATA TO SET UP THE MAIN PROGRAMME

With all the data you have collected you can dig deep to find some "connection" between someone's tweet and the changes in the price of a coin in the markets.
The connection between Elon Musk tweeting and the rise in DOGE's price it's pretty obvious. I just checked that in all the history of musk's "DOGE_tweet" there was never negative sentiment (in that case i should have put in place some sentiment analysis, but it would be very hard), and also that every one of them had a reaction on the markets. And both of those conditions were TRUE.



## BUY CRYPTO WHEN CHECKING FOR A WORD IN THE TEXT OF A TWEET

## MAIN FOLDER

### From the main folder you can pick two different script that will buy crypto directly, that have different interesting features.

1) With "buy_DOGE_Binance.py" you will be able to buy with Binance using "Threading" making fast API requests for multiple accounts, maybe for you or a friend.

2) With "buy_DOGE_Kraken.py" you will be able to buy with Kraken. In these case i wanted to profit from the script but also don't want to give up other trading opportunities given by other limit orders: so i implement a part of the script so that when the "condition is met" before buying he deletes all the open orders, and than after selling he restores them. (this little feature takes a small portion of time to execute).



## ADDITIONAL NOTES:
### There are many little variable to check and play with, in the script, in order get the best results: for exemple i choosed to buy DOGE when MUSK tweets and sell them after 180 seconds because that was the average time where price was higher when i analyzed the data, maybe you want to change that or check it again or do your own research....

###################################################################################################################################################################

### ITALIANO ITALIANO ITALIANO

### IMPORTANTE! : non sono un consulente finanziario e non mi assumo in alcun modo la responsabilità se qualcosa va storto con il programma. Se guadagni un po' di soldi, sarò contento per te! Per me ha funzionato molto bene negli ultimi mesi...

# ACQUISTA-DOGE-ELON-MUSK

### BREVE DESCRIZIONE:

Questo programma consente di AUTOMATIZZARE l'acquisto di CRIPTOVALUTE quando viene soddisfa una determinata condizione in uno stream listener su TWITTER

## RECUPERA DATI PULITI E ORDINATI DAL WEBSOCKET BINANCE 

#### Dalla cartella "BINANCE_data"
1) Usa il file "retrieve_data.py" per connetterti a Binance Websocket e iniziare a recuperare i dati delle CRYPTO (cambia l'URL dello stream se desideri cambiare le coppie di CRYPTO). Lo script memorizzerà quindi i dati creando un nuovo file json ogni giorno.

2) Utilizza il file "clean_display_data.ipynb" per pulire e tracciare i grafici. In questo caso ho scelto di analizzare il grafico dei prezzi di DOGE

## OTTIENI TUTTI I TWEET DAL PROFILO TWITTER SCELTO

#### In questo caso ho scelto di analizzare il profilo twitter di Elon Musk

#### Dalla cartella "TWITTER_data"
1) Usa il file "scrapeHTML_ElonMusk_Twitter.ipynb" usando il jupyter notebook per raschiare i tweet dall'HTML. Questo file raccoglierà il testo dei tweet e li inserirà in un file csv. Usa il tuo account personale per entrare in twitter (per essere sicuro di non perdere i tweet). Modifica lo "SCROLL_TIME" in relazione a quanto è veloce la tua connessione internet (ricorda se vai troppo veloce twitter ti impedirà di continuare a scorrere), dovrai riprovare più volte prima di ottenere un buon risultato. Finirai sempre con molti duplicati ma va bene: è meglio avere dei duplicati che rischiare di perdere qualche tweet.

2) Nel caso in cui il risultato non sia sufficiente, prova a raschiare l'API con TWEEPY con "scrapeAPI_ElonMusk_Twitter.ipynb" (o "scrapeAPI_ElonMusk_Twitter.py").

NOTA: TWITTER ha cambiato spesso le regole per l'utilizzo della sua API e anche quanto puoi scorrere verso il basso dando a entrambi alcune molte restrizioni! Sono stato fortunato che quando ho usato per la prima volta questi script potevo scrollare molto indietro nel tempo raschiando l'HTML, quindi era sufficiente.


## ANALIZZA I DATI PER IMPOSTARE IL PROGRAMMA PRINCIPALE

Con tutti i dati che hai raccolto puoi scavare a fondo per trovare qualche "connessione" tra il tweet di qualcuno e le variazioni del prezzo di qualche moneta nei mercati.
La connessione tra i tweet di Elon Musk e l'ascesa in DOGE è abbastanza ovvia. Ho verificato che negli ultimi anni di "DOGE_tweet" di musk non ci sia mai stato un sentimento negativo (in quel caso avrei dovuto fare un po' di analisi del sentimento, e sarebbe stata un ulteriore complicazione al programma), e anche che ognuno di loro avesse avuto una impatto sul prezzo di DOGE. Ed entrambi sono VERI.

## ACQUISTA CRYPTO QUANDO TROVA UNA PAROLA NEL TESTO DI UN TWEET
## CARTELLA PRINCIPALE

### Dalla cartella principale puoi scegliere due diversi script che acquisteranno direttamente le criptovalute, questi hanno diverse caratteristiche interessanti.

1) Con "buy_DOGE_Binance.py" potrai acquistare con Binance usando "Threading" facendo richieste API in parallelo per più account, magari per te o un amico

2) Con "buy_DOGE_Kraken.py" potrai acquistare con Kraken. In questo caso volevo trarre profitto dallo script ma anche non volevo rinunciare ad altre opportunità di trading date da altri ordini limite: quindi ho implementato una parte dello script in modo che quando la "condizione è soddisfatta" prima di acquistare cancella tutto gli ordini aperti, e dopo averli venduti li ripristina. (questa piccola funzione richiede una piccola porzione di tempo per essere eseguiti)



## NOTE AGGIUNTIVE:
### Ci sono molte piccole variabili da controllare e con cui giocare, nello script, per ottenere i migliori risultati: per esempio ho scelto di acquistare DOGE quando MUSK twitta e venderli dopo 180 secondi perché era il tempo medio in cui il prezzo era più in alto quando ho analizzato i dati, forse vuoi cambiarlo o controllarlo di nuovo o fare le tue ricerche ....
