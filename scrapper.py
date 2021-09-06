from google_play_scraper import app

import pandas as pd
import numpy as np

from google_play_scraper import Sort, reviews_all

def scrape_google_play(app_id: str, lang = 'pt', country = 'br', sort: Sort.MOST_RELEVANT | Sort.NEWEST = Sort.NEWEST):
    reviews = reviews_all(
    app_id,
    sleep_milliseconds=0,
    lang=lang, 
    country=country,
    sort=sort, 
    )

    df = pd.DataFrame(np.array(reviews),columns=['review'])

    df = df.join(pd.DataFrame(df.pop('review').tolist()))

    return df.to_json()