import mlbgame
import praw
import pprint
import time
import sys
from datetime import datetime


print("Reposting wiki at {0}".format(str(datetime.now())))
r = praw.Reddit('wikibot', user_agent='randombot')

sub = r.subreddit('andomprecision1')

wikiText = sub.wiki['events'].content_md

now = datetime.now().date().isoformat()

post = sub.submit("Weekly events thread for " + now, wikiText)
post.mod.sticky(bottom=True)