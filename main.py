#!/usr/bin/env python3
# coding=utf-8

import requests
print("Эти данные были получены из индекса цен на биткойны CoinDesk (USD):")
print("1 биткоин стоит",
      requests.get('http://api.coindesk.com/v1/bpi/currentprice.json').json()["bpi"]["USD"]["rate"], "$")
