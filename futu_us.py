import futu as ft
import pandas as pd
import numpy as np 
import configparser

config = configparser.ConfigParser()
config.read('futu.config')
pwd_unlock = config['DEFAULT']['Password']
trd_ctx = ft.OpenUSTradeContext(host = '127.0.0.1', port = 11111)
trd_ctx.unlock_trade(pwd_unlock)
deal_list = trd_ctx.history_deal_list_query(start = config['US']['StartDate'], end = config['US']['EndDate'])
print(pd.DataFrame.to_csv(deal_list[1]))
trd_ctx.close()