import service

if __name__ == '__main__':
    service.get_all_binance("ETHUSDT", '1h', save=True)
    service.get_all_binance("LTCUSDT", '1d', save=True)
    service.get_all_binance("BTCUSDT", '5m', save=True)

    # table = {"BTCUSDT",
    #          "ETHUSDT",
    #          "LTCUSDT",
    #          "XRPUSDT",
    #          "BCHUSDT",
    #          "LINKUSDT",
    #          "DOTUSDT",
    #          "ADAUSDT",
    #          "BSVUSDT",
    #          "CROUSDT",
    #          "USDCUSDT",
    #          "EOSUSDT",
    #          "XMRUSDT",
    #          "TRXUSDT",
    #          "XTZUSDT",
    #          "FILUSDT",
    #          "XLMUSDT",
    #          "NEOUSDT"}

# for element in table:
#     service.get_all_binance(element, '5m', save=True)
