"""
Python + Trongrid API. Получаю транзакции USDT в сети TRC20 блокчейна TRON. Легко, без парсинга.

Получаю транзакции в USDT TRC20 через

TRONGRID API
https://developers.tron.network/reference/get-trc20-transaction-info-by-account-address

TRONSCAN USDT TRC20
https://tronscan.org/#/token20/TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t

!!! Поддержи блоггера !!!
https://azzrael.ru/spasibo

"""
import datetime as dt
import requests

print("Hola, AzzraelCode YouTube Subs!")

num = 0
account_id = "xxx" # можно взять на https://tronscan.org/#/token20/TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t
url = f"https://api.trongrid.io/v1/accounts/{account_id}/transactions/trc20"
pages = 3

params = {
    # 'only_to': True,
    # 'only_from': True,
    # 'max_timestamp': dt.datetime.timestamp(dt.datetime.now() - dt.timedelta(hours=6))*1000,
    'only_confirmed': True,
    'limit': 20,
}


for _ in range(0, pages):
    r = requests.get(url, params=params, headers={"accept": "application/json"})
    params['fingerprint'] = r.json().get('meta', {}).get('fingerprint')

    for tr in r.json().get('data', []):
        num += 1
        symbol = tr.get('token_info', {}).get('symbol')
        fr = tr.get('from')
        to = tr.get('to')
        v = tr.get('value', '')
        dec = -1 * int(tr.get('token_info', {}).get('decimals', '6'))
        f = float(v[:dec] + '.' + v[dec:])
        time_ = dt.datetime.fromtimestamp(float(tr.get('block_timestamp', '')) / 1000)

        print(f"{num:>3} | {time_} | {f:>9.02f} {symbol} | {fr} > {to}")
