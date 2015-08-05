import re, requests, json
from time import sleep
from datetime import datetime, timedelta
from collections import defaultdict
from bs4 import BeautifulSoup
from flask import current_app
# from flask.ext.script import Command, Option
from app import models, db
from app.models import NytArticle

class NytTrending():
    """Add nyt trending articles to db"""

    def run(self):
        # creates empty dictionary
        results = defaultdict(lambda:0, {})
        # gets current date and time
        now = datetime.now()
        # round down to nearest hour
        fetch_date = datetime(now.year, now.month, now.day, now.hour, 0, 0)
        print fetch_date

        # yesterday
        yesterday = fetch_date.date() - timedelta(days=1)
        print yesterday

        url = 'http://www.nytimes.com/most-popular-emailed?period=1'

        category = url.split('?')[0].split('/')[-1]
        print category

        soup = BeautifulSoup(requests.get(url, timeout=5).content)
        stories = soup.findAll('div', {'class': 'story'})

        for i, story in enumerate(stories):
            thumb, title, link, desc = (None,) * 4

            thumb = story.find('img')
            if thumb:
                thumb = thumb.get('src')

            title_cntnr = story.find('h3')
            if title_cntnr:
                title = title_cntnr.text.strip()
                link = title_cntnr.find('a').get('href')

            desc = story.find('p', {'class': 'summary'})
            if desc:
                desc = desc.text.strip()

            rank = i + 1

            if rank <= 10 and title and link:
                nyt = NytArticle.query.filter_by(
                    category = category,
                    rank = rank,
                    day_id = yesterday
                ).first()

                if nyt is None:
                    nyt = NytArticle(
                        category = category,
                        rank = rank,
                        title = title,
                        link = link,
                        desc = desc,
                        thumb = thumb,
                        fetch_date = fetch_date,
                        day_id = yesterday
                    )
                    db.session.add(nyt)
                    db.session.commit()
                    results['new'] += 1
                else:
                    results['repeat'] += 1

        print dict(results)