import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('mortgage_vs_treasury_spread.csv', parse_dates=['Date'])
df = df.sort_values('Date').set_index('Date')

# Chart 1) Time-series plot of both rates
plt.figure()
plt.plot(df.index, df['30-Year Fixed Mortgage Rate'], label='30Y Mortgage Rate')
plt.plot(df.index, df['10Y Treasury Yield'], label='10Y Treasury Yield')
plt.title('30Y Mortgage Rate vs 10Y Treasury Yield')
plt.xlabel('Date')
plt.ylabel('Rate (%)')
plt.legend()
plt.tight_layout()
plt.show()

# Chart 2) Scatter plot of Mortgage vs Treasury
plt.figure()
plt.scatter(df['10Y Treasury Yield'], df['30-Year Fixed Mortgage Rate'], s=10)
plt.title('Scatter: Mortgage Rate vs Treasury Yield')
plt.xlabel('10Y Treasury Yield (%)')
plt.ylabel('30Y Mortgage Rate (%)')
plt.tight_layout()
plt.show()

# Chart 3) Plot the spread as a line over time
plt.figure()
plt.plot(df['Spread (Mortgage − Treasury)'])
plt.title('Spread Over Time: 30Y Mortgage Rate − 10Y Treasury Yield')
plt.xlabel('Date')
plt.ylabel('Spread (percentage points)')
plt.tight_layout()
plt.show()

# Chart 4) Rolling correlation (1-year window)
corr_window = 252     # because there are 252 trading days (data does not include weekends)
roll_corr = df['30-Year Fixed Mortgage Rate'] \
    .rolling(window=corr_window) \
    .corr(df['10Y Treasury Yield'])
plt.figure()
plt.plot(roll_corr.index, roll_corr, label=f'{corr_window}-day Rolling Corr')
plt.title('Rolling Correlation (30Y Mortgage vs 10Y Treasury)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.ylim(-1,1)
plt.axhline(0, linestyle='--', linewidth=1)
plt.tight_layout()
plt.show()


# Chart 5) 1-year rolling regression
window = 252  # 1-year trading days
betas = []
dates = df.index[window:]

# Prepare arrays
y_all = df['30-Year Fixed Mortgage Rate'].values
x_all = df['10Y Treasury Yield'].values.reshape(-1, 1)

# Rolling regression
for i in range(window, len(df)):
    y = y_all[i-window:i]
    x = x_all[i-window:i]
    lr = LinearRegression().fit(x, y)
    betas.append(lr.coef_[0])

# Plot rolling beta
plt.figure()
plt.plot(dates, betas, label='Rolling Beta (sensitivity)')
plt.axhline(1, color='k', linestyle='--', linewidth=1, label='Beta = 1')
plt.title('1-Year Rolling Regression Beta')
plt.xlabel('Date')
plt.ylabel('Slope of Mortgage vs Treasury')
plt.legend()
plt.tight_layout()
plt.show()


