import requests
import json, sys
import datetime

def display_date(t):
  return datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')

url = 'https://api.thegraph.com/subgraphs/name/ianlapham/uniswapv2'

if len(sys.argv)==2:
  token_address = sys.argv[1]
else:
  token_address = "0x6b175474e89094c44da98b954eedeac495271d0f"
print(token_address)

data = '''
query {
  tokenDayDatas(orderBy: date, orderDirection: desc, first: 30
  where: {
    token: "%s"
  }
  ) {
    id
    date
    priceUSD
    totalLiquidityToken
    totalLiquidityUSD
    totalLiquidityETH
    dailyVolumeETH
    dailyVolumeToken
    dailyVolumeUSD
  }
}
'''%token_address
resp = requests.post(url,json={'query': data}).json()
data_ = resp['data']['tokenDayDatas']
print('date', 'price', 'volume(usd)', 'volume(token)', 'liquidity(usd)', 'liquidity(token)')
for p in data_:
  day = display_date(p['date'])
  print(day, round(float(p['priceUSD']),2), int(float(p['dailyVolumeUSD'])), int(float(p['dailyVolumeToken'])), 
    int(float(p['totalLiquidityUSD'])), int(float(p['totalLiquidityToken'])))