# Crypto Currency API

Этот API предоставляет доступ к данным о криптовалютах с использованием CoinMarketCap API.

## Функции

- **Получение списка криптовалют**: Получите данные о криптовалютах, включая цену, объем торгов, и другие параметры.
- **Получение данных по конкретной криптовалюте**: Получите подробные данные по конкретной криптовалюте, используя её ID.

## Как запустить

### 1. Клонируйте репозиторий:

```bash
git clone https://Shahzod2555/CryptoCurrencyAPI.git
cd CryptoCurrencyAPI
```
### 2. Установите зависимости:
Создайте виртуальное окружение и активируйте его:

``` bash
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows
```
Установите зависимости:

``` bash
pip install -r requirements.txt
```

3. Создайте файл .env в корне проекта и добавьте свой API ключ от CoinMarketCap:

```
CMC_API_KEY=Сюда ваш api key
```
4. Запустите сервер:
```bash
python app.py
```
API будет доступен по адресу http://127.0.0.1:8000.

## Эндпоинты:

URL: `/cryptocurrencies`  | Метод: `GET`

Описание: Получить список криптовалют с основными данными.

Пример ответа: json
```json
[
  {
    "name": "Bitcoin",
    "slug": "bitcoin",
    "date_added": "2013-04-28T00:00:00.000Z",
    "circulating_supply": 18752975,
    "total_supply": 21000000,
    "is_active": 1,
    "price_usd": 45000.00,
    "percent_change_7d": 2.5,
    "volume_24h": 3500000000
  },
  {
    "name": "Ethereum",
    "slug": "ethereum",
    "date_added": "2015-07-30T00:00:00.000Z",
    "circulating_supply": 115000000,
    "total_supply": 120000000,
    "is_active": 1,
    "price_usd": 3000.00,
    "percent_change_7d": 1.2,
    "volume_24h": 2500000000
  }
]
```

URL: `/cryptocurrencies/{currency_id}` | Метод: `GET`

Описание: Получить данные о конкретной криптовалюте по её ID.

Пример ответа: json

``` json
{
  "name": "Bitcoin",
  "slug": "bitcoin",
  "date_added": "2013-04-28T00:00:00.000Z",
  "circulating_supply": 18752975,
  "total_supply": 21000000,
  "is_active": 1,
  "price_usd": 45000.00,
  "percent_change_7d": 2.5,
  "volume_24h": 3500000000
}
```
