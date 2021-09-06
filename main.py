from server import App
from scrapper import scrape_google_play

app = App()

@app.get("/{app_id}")
async def root(app_id: str):
    return scrape_google_play(app_id)