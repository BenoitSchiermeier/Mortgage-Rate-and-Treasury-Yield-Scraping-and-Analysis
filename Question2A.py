import pandas as pd
import datetime
from pandas_datareader import data as web

# load mortgage‐rate history scraped in question 1: 
mortgage_rate = pd.read_csv(
    'housingbrief_30yr_mortgage_rate.csv',
    parse_dates=['Date']
)

# 10-year Treasury yield from FRED: (from this website: https://fred.stlouisfed.org/series/DGS10)
# fred API used with "DGS10" as identifier
# Determine the first mortgage date & back up 7 days
start = mortgage_rate['Date'].min() - datetime.timedelta(days=7)
end   = datetime.datetime.today()

treasury = web.DataReader('DGS10', 'fred', start=start, end=end)

# reset index and rename columns: 
treasury = treasury.reset_index().rename(columns={
    'DATE': 'Date',
    'DGS10': '10Y Treasury Yield'
})

# Merge as-of to align respective mortgage dates with treasury yield
# every mortgage date — will will be matched w/ most recent prior Treasury yield
df = pd.merge_asof(
    mortgage_rate.sort_values('Date'),
    treasury.sort_values('Date'),
    on='Date',
    direction='backward'
)

# calculate spread
df['Spread (Mortgage − Treasury)'] = (
    df['30-Year Fixed Mortgage Rate'] - df['10Y Treasury Yield']
)

# Save to CSV
result = 'mortgage_vs_treasury_spread.csv'
df.to_csv(result, index=False)

# check py script
print(f"Wrote {len(df)} rows to {result}")
