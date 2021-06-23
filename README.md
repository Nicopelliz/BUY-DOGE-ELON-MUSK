# IMPORTANT! : i'm not a financial adviser and i will not assume in any way shape or form responsability if something goes wrong with the script... (if you are able to gain some money i will cheer with you)

ENGLISH ENGLISH ENGLISH
# BUY-DOGE-ELON-MUSK

SHORT DESCRIPTION:

These scripts allow you to AUTOMATE buying CRYPTOCURRENCY when meeting a certain condition from a TWITTER stream listener

## GET CLEAN AND USE DATA FROM BINANCE WEBSOCKET 
#### From folder "BINANCE_data"
1)Use the file "retrieve_data.py" to connect to Binance Websocket and start retrieving coin data (change the stream URL if you wish to change the coin pairs). The script will than store the data creating a new json file every day.

2)Use the file "clean_display_data.ipynb" to clean and plot the data. In this case i choosed to analyze DOGE coin price chart

## GET ALL THE TWEETS FROM CHOOSEN TWITTER PROFILE
#### In this case i choosed to scrape Elon Musk twitter profile

#### From folder " TWITTER_data"
1)Use the file "scrapeHTML_ElonMusk_Twitter.ipynb" using jupyter notebook to scrape the tweets from the HTML. This file will collect the text of the tweets and put them in a csv file.

Use your personal account to enter twitter (to be sure to not missing tweets). Change the "SCROLL_TIME" in relation to how fast is your internet connection (remember if you go too fast twitter will stop prevent you from keep scrolling), you will have to try several times before getting a good result. You will always end up with duplicates but it's fine: it's better to have duplicates than missing some tweets.

2) In case the result is not sufficient, try scraping the API with TWEEPY with "scrapeAPI_ElonMusk_Twitter.ipynb"(or "scrapeAPI_ElonMusk_Twitter.py"). 

NOTE: TWITTER has changed often the rules for using its API and also how much you can scroll down giving both of them some big restrictions! I was lucky that when i first used those script i could go very much back in time with scraping the HTML so it was sufficient.


## ANALIZE THE DATA TO SET UP THE MAIN PROGRAMME

With all the data you have collected you can dig deep to find some "connection" between someone's tweet and the changes in the price of some coin in the markets.
:The connection between Elon Musk tweeting and rise in DOGE it's pretty obvious. I just checked that in all the history of musk's "DOGE_tweet" there was never negative sentiment (in that case i should have put in place some sentiment analysis, but it would be very hard), and also that every one of them had a reaction on the markets. And both of those were TRUE.



## BUY CRYPTO WHEN CHECKING FOR A WORD IN THE TEXT OF A TWEET
## MAIN FOLDER

### From the main folder you can pick two different script that will buy crypto directly, that have different interesting features.

1) With "buy_DOGE_Binance.py" you will be able to buy with Binance using "Threades" making fast API requests for multiple accounts, maybe for you or a friend

2) With "buy_DOGE_Kraken.py" you will be able to buy with Kraken. In these case i wanted to profit from the script but also don't want to give up other trading opportunities given by other limit orders: so i implement a part of the script so that when the "condition is met" before buying he deletes all the open orders, and than after selling he restores them. (this little feature takes a small portion of time to execute)



## ADDITIONAL NOTES:
### There are many little variable to check and play with, in the script, in order get the best results: for exemple i choosed to buy DOGE when MUSK tweets and sell them after 180 seconds because that was the average time where price was higher when i analyzed the data, maybe you want to change that or check it again or do your own research....
