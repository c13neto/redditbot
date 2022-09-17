import praw
import feedparser
import re


#reddit informações
reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    password="PASSWORD",
    user_agent="USERAGENT",
    username="USERNAME",
)
subreddit = ['']

#html removedor
TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

#feed
news = feedparser.parse('')
indic = len(NewsFeed.entries) + 1

#---------------------------------------
med = 0
#---------------------------------------

#postar
for med in range(indic):
    reddit.subreddit(subreddit).submit(title = remove_tags(entry.title[med]), selftext = remove_tags(News.Feed.entries[med]) )
