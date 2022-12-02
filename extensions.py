import requests
import json
from config import keys


class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        url = f"https://api.apilayer.com/currency_data/convert?to={base}&from={quote}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "wBWw8FrVUdhFoIYl4oCbcJjXmxKdUt1a"
        }

        response = requests.request("GET", url, headers=headers)

        status_code = response.status_code
        result = response.text
#new_price = json.loads(response.content).get('ваш_ключ_словаря')
        total_base = json.loads(response.content).get('result')

        return total_base