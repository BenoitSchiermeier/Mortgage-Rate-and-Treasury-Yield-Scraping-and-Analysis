import json
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 1) Use headless Chrome using Selenium so that in runs in the background
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

# given website in question 1 -> tell chrome to open it
url = 'https://housingbrief.com/mortgage-rates/67d80b67b658f8e76398a0c8'
driver.get(url) 

# sleep for some time to let the chart render
time.sleep(6)

# use JS and execute it in the page 
# it locates the Highcharts series named “30 YR Fixed,” grabs its data 
# array ([[timestamp, rate, …], …])
js = """
  const series = Highcharts.charts
    .flatMap(c => c.series)
    .find(s => s.name.includes('30 YR Fixed'));
  return JSON.stringify(series.options.data);
"""

# execute script above and save output of the script to data_json
try:
     data_json = driver.execute_script(js)
except Exception as e:
    
    # if this outputed, there was an error
    raise RuntimeError(f"Failed to extract Highcharts data: {e!s}")

driver.quit()

# load JSON into Python 
raw = json.loads(data_json)  

# Cleaning the data... only first two elements needed -> (timestamp_ms) and morgage rate)
cleaned = [[r[0], r[1]] for r in raw]

# build dataframe from cleaned data
df = pd.DataFrame(cleaned, columns=['timestamp_ms', '30-Year Fixed Mortgage Rate'])
df['Date'] = pd.to_datetime(df['timestamp_ms'], unit='ms')

# only choose the past 10 years
ten_years_ago = pd.Timestamp.today() - pd.DateOffset(years=10)
df = df[df['Date'] >= ten_years_ago].copy()

# reorder colums and save...
df = df[['Date', '30-Year Fixed Mortgage Rate']]
df.to_csv('housingbrief_30yr_mortgage_rate.csv', index=False)

# to make sure script works: 
print(f"Created {len(df)} rows in housingbrief_30yr_mortgage_rate.csv")
