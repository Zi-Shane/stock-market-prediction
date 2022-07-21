# %%
import os
import yfinance as yf

# e.g. company = 'BRK-A'
def download_ticker(company: str):
    tick = yf.Ticker(company)
    
    # historical data
    tick.history(period="max").to_csv(os.getcwd() + '/datasets/' + company + '.csv')
    print('/datasets/' + company + '.csv')
    # dividends & splits
    tick.actions.to_csv(os.getcwd() + '/datasets/' + company + '_actions.csv')
    print('/datasets/' + company + '_actions.csv')


try:
    os.mkdir('datasets')
    print('create directory: `datasets` ')
except:
    print('`datasets` already exist')

download_ticker('BRK-A')
