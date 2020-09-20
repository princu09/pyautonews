import time
import schedule
import requests
import urllib
import feedparser
import json
from apscheduler.schedulers.blocking import BlockingScheduler


def telegram_bot_sendtext(news_title , news_desc , news_link):
    
    bot_token = '1323948381:AAFIvfAAkIIEyadGE4y9M6we1fS_mlBRWnc'
    bot_chatID = '@hgdw09'

    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + '*' + news_title  + '*' + "," + news_desc + '*' + news_link + '*'

    response = requests.get(send_text)

    return response.json()

def NewsFromNFG(): 
    
    # Digital Inspiration Feed

    NewsFeed = feedparser.parse("https://www.labnol.org/rss.xml")

    for ar in NewsFeed.entries: 
        title = (ar["title"])
        desc = (ar["description"])
        link = (ar["link"])
        # print(title)
        # print(desc)
        # print(link)
        telegram_bot_sendtext(title , desc , link)
        time.sleep(600)

def NewsFromNFG2(): 
  
    NewsFeed = feedparser.parse("https://feeds.feedburner.com/gadgets360-latest")

    for ar in NewsFeed.entries: 
        title = (ar["title"])
        desc = (ar["description"])
        link = (ar["link"])
        # print(title)
        # print(desc)
        # print(link)
        telegram_bot_sendtext(title , desc , link)
        time.sleep(600)

def NewsFromNFG3(): 
  
    NewsFeed = feedparser.parse("https://gadgets.ndtv.com/rss/feeds")

    for ar in NewsFeed.entries: 
        title = (ar["title"])
        desc = (ar["description"])
        link = (ar["link"])
        # print(title)
        # print(desc)
        # print(link)
        telegram_bot_sendtext(title , desc , link)
        time.sleep(600)


if __name__ == '__main__':

    schedule.every().day.at("12:00").do(NewsFromNFG2)

    NewsFromNFG3()
    
    schedule.every().day.at("12:00").do(NewsFromNFG)

    NewsFromNFG()

    schedule.every().day.at("12:00").do(NewsFromNFG2)

    NewsFromNFG2()