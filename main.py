from server import App
from services.scrapper import scrape_google_play

app = App()

@app.get('/')
async def root():
    return "hello scrappers"

@app.get("/scrape/{app_id}")
async def scrape(app_id: str):
    return scrape_google_play(app_id)