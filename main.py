from fastapi import FastAPI
from wordtune import CRAWLER

app=FastAPI()
scraper = CRAWLER()

@app.get("/{search_data}")
async def read_item(search_data):
    return scraper.process_logic(search_data)