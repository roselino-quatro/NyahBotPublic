# Pega as constantes do arquivo .env 
import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN=os.getenv("TELEGRAM_TOKEN")
WIKIART_TOKEN=os.getenv("WIKIART_TOKEN")
WIKIART_SECRET=os.getenv("WIKIART_SECRET")
