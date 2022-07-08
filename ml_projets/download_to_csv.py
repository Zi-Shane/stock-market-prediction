# %%
import yfinance as yf

# e.g. company = 'BRK-A'
def download_ticker(company: str):
    tick = yf.Ticker(company)
    
    # historical data
    tick.history(period="max").to_csv('../datasets/' + company + '.csv')
    print('../datasets/' + company + '.csv')
    # dividends & splits
    tick.actions.to_csv('../datasets/' + company + '_actions.csv')
    print('../datasets/' + company + '_actions.csv')


download_ticker('BRK-A')
