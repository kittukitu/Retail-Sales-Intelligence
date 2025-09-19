Retail Sales Forecasting & Inventory Recommendation
This project generates synthetic daily retail sales data with customizable parameters for promotions, sales trends, and holiday effects. It trains a time series forecasting model to predict next month’s sales, provides inventory (reorder point, safety stock) recommendations, and visualizes historical data with forecasts and correlations.

Features
Synthetic retail sales dataset: 2 years (730 days) with daily granularity.

Customizable simulation parameters:

Promotion probability

Start and end of sales trend

Main holiday month

Promotional and holiday impact on sales

Forecasting: 30-day sales prediction using Holt-Winters Exponential Smoothing.

Inventory recommendations: Safety stock and reorder point calculation.

Visualizations:

Seasonal decomposition

Historical vs forecasted sales

Feature correlation heatmap.

Requirements
Python 3.x

pandas

numpy

matplotlib

seaborn

statsmodels

Install with:

bash
pip install pandas numpy matplotlib seaborn statsmodels
Usage
Run the script
The script will prompt for data generation parameters with defaults:

Daily promo probability (default=0.12)

Sales trend start value (default=200)

Sales trend end value (default=280)

Main holiday month (default=12)
Enter custom values or press Enter to accept defaults.

Data Generation
A synthetic sales dataset is generated and saved as retail_sales_data.csv.

Forecast & Inventory Recommendation

30-day forecast using Holt-Winters model.

Inventory calculations for reorder point and safety stock for the next lead time period.

Recommendations are printed in the console.

Visualizations

Seasonal decomposition plot

Historical sales and forecast plot

Correlation heatmap (sales vs promo)

Files
retail_sales_data.csv: The generated daily sales dataset

Script file: Main Python script with forecasting and recommendations

Notes
Dataset simulates holiday sales spike before 26th of chosen holiday month.

Seasonal period is set to one year, accommodating annual patterns.

Lead time is set to 7 days (changeable in script for different scenarios).

Visualizations require a GUI environment for display.