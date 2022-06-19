from fastapi import FastAPI, Request
from extractor import *

app = FastAPI()

@app.get('/{smogon_url:path}')
async def get_pokemon_data(request: Request, smogon_url: str):
    return pokemon_data(url=f'https://www.smogon.com/{smogon_url}')