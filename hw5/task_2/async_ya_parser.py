import aiohttp
import asyncio
import json
import datetime
import pandas as pd
import argparse
import random
from bs4 import BeautifulSoup
from pathlib import Path


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"
]


async def fetch_html(session, url):
    headers = {'User-Agent': random.choice(USER_AGENTS)}
    async with session.get(url) as response:
        return await response.text()


def parse_apartments(data):
    bs = BeautifulSoup(data, 'html.parser')
    apartments_raw = bs.find_all('li', class_='OffersSerpItem')
    apartments = []

    for item in apartments_raw:
        apartments.append({
            'title': item.find('span', class_='OffersSerpItem__title').text.strip(),
            'date': item.find('div', class_='OffersSerpItem__publish-date').text.strip(),
            'price': item.find('span', class_='price').text.strip(),
            'floor': item.find('div', class_='OffersSerpItem__building').text.strip(),
            'address': item.find('div', class_='OffersSerpItem__address').text.strip(),
            'description': item.find(class_='OffersSerpItem__description').text.strip() if item.find(
                class_='OffersSerpItem__description') else '',
        })

    return apartments


async def main(output_dir):
    async with aiohttp.ClientSession() as session:
        html_content = await fetch_html(session, 'https://realty.yandex.ru/nizhniy_novgorod/snyat/kvartira/')

        apartments = parse_apartments(html_content)

        output_file = Path(output_dir) / "apartments.json"
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(apartments, json_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", type=str, default="artifacts", help="Output directory to save apartments info")
    args = parser.parse_args()

    output_dir = args.output_dir
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    asyncio.run(main(output_dir))
