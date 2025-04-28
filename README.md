# Scraping Mortgage rate and Treasury Yield Data
*By Benoit Schiermeier*

## Instructions
1. Install dependencies:

2. Run the scripts:
- `Question1.py`: Uses Selenium to open the HousingBrief website, extract historical 30-Year Fixed Mortgage Rate data from an embedded Highcharts object using JavaScript, clean the data, and save the last 10 years of mortgage rates into a CSV file.
- `Question2.py`: Loads the scraped mortgage rate data, pulls 10-year Treasury yield data from the FRED API, calculates the spread between mortgage rates and Treasury yields, and saves the result to a CSV file.
- `Question2B.py`: Loads the merged mortgage and Treasury spread data, generates time-series, scatter, spread, rolling correlation, and rolling beta plots to visualize how the relationship between mortgage rates and Treasury yields has evolved over time.



## Tools Used
- **Selenium** – for web scraping mortgage rate data
- **Pandas** – for data manipulation and cleaning
- **Matplotlib** – for data visualization and plotting
- **Scikit-learn** – for running rolling regression analysis
- **pandas-datareader** – for fetching Treasury yield data from FRED

## Notes
All data was gathered using public sources, and analysis was completed in Python.

---


![Figure_5](https://github.com/user-attachments/assets/5a40b391-db28-4b4b-b0b5-11633586f1de)
![Figure_3](https://github.com/user-attachments/assets/1ab848eb-5513-4709-a632-f8e5eb0e2a1e)
![Figure_4](https://github.com/user-attachments/assets/bb84d9e3-fe7d-4e39-92c0-566a710f9f01)
![Figure_2](https://github.com/user-attachments/assets/6dc74f4f-0e0c-4275-ae23-099a212f3cc4)
![Figure_1](https://github.com/user-attachments/assets/c1f2d6e2-c4b4-4317-b3b9-7374adad4125)
