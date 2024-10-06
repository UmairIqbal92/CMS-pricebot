import os

# the token of your bot
TOKEN_BOT = '8125101838:AAHYWKI2PRUIxKqnSOXtn3uii8InWBynec0'

# do APIs requests with pause
TIME_INTERVAL = 3600

# new pro API CoinMarketCap Key
CMC_API_KEY = "put_your_here"
COINMARKET_API_URL_GLOBAL = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest' \
                            '?CMC_PRO_API_KEY={}'
COINMARKET_API_URL_COINLIST = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5000' \
                              '&CMC_PRO_API_KEY={}'

FILE_JSON_COINMARKET = os.path.dirname(os.path.realpath(__file__)) + '/coinmarketcoins.json'
FILE_JSON_GLOBALINFOAPI = os.path.dirname(os.path.realpath(__file__)) + '/globalinfoapi.json'


class JSONFiles:
    def __init__(self):
        self.coinmarketcapjson = {}
        self.globalinfoapijson = {}

    def update_cmc_json(self, json1):

        assert isinstance(json1, dict)
        self.coinmarketcapjson = json1
        return json1

    def update_globalcmc_json(self, json2):
        assert isinstance(json2, dict)
        self.globalinfoapijson = json2
        return json2


# the object of class JSONFiles for save json API coins lists
jsonfiles = JSONFiles()
