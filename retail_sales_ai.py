import warnings
from statsmodels.tools.sm_exceptions import ConvergenceWarning

# Suppress only the ConvergenceWarning from statsmodels
warnings.simplefilter("ignore", ConvergenceWarning)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# --- Step 1: User input for data generation parameters ---
try:
    promo_prob = float(input("Set daily promo probability (default 0.12): ") or 0.12)
except ValueError:
    promo_prob = 0.12

try:
    trend_start = float(input("Set start of sales trend (default 200): ") or 200)
except ValueError:
    trend_start = 200

try:
    trend_end = float(input("Set end of sales trend (default 280): ") or 280)
except ValueError:
    trend_end = 280

try:
    holiday_month = int(input("Set main holiday month (1-12, default 12): ") or 12)
    if holiday_month < 1 or holiday_month > 12:
        holiday_month = 12
except ValueError:
    holiday_month = 12

# --- Step 2: Generate synthetic retail sales dataset with inputs ---
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", periods=730, freq='D')
trend = np.linspace(trend_start, trend_end, 730)
seasonality = 30 * np.sin(2 * np.pi * dates.dayofyear / 365.25)
random_noise = np.random.normal(0, 15, 730)
promo = np.random.binomial(1, promo_prob, 730)
holiday_spike = np.where((dates.month == holiday_month) & (dates.day < 26), 50, 0)

sales = trend + seasonality + random_noise + (promo * 40) + holiday_spike
sales = np.maximum(0, sales)

data = pd.DataFrame({
    'date': dates,
    'sales': sales.round().astype(int),
    'promo': promo,
})

# Save dataset as CSV
data.to_csv("retail_sales_data.csv", index=False)
print("Synthetic retail sales dataset saved as 'retail_sales_data.csv'.")

# --- Step 3: Forecast sales for next 30 days ---
data.set_index('date', inplace=True)
data.index = pd.DatetimeIndex(data.index, freq='D')  # Set frequency explicitly
ts = data['sales']

decomp = seasonal_decompose(ts, model='additive', period=365)
decomp.plot()
plt.suptitle('Seasonal Decomposition (Additive)', y=1.01)
plt.tight_layout()
plt.show()

forecast_period = 30
model = ExponentialSmoothing(ts, trend='additive', seasonal='additive', seasonal_periods=365)
fit = model.fit()
forecast = fit.forecast(forecast_period)

# --- Step 4: Inventory Recommendations ---
mean_sales = ts[-30:].mean()
std_sales = ts[-30:].std()
lead_time = 7
safety_stock = int(1.65 * std_sales * np.sqrt(lead_time))
reorder_point = int(mean_sales * lead_time + safety_stock)

print(f"\n--- Inventory Recommendation ---")
print(f"Recommended reorder point for next period: {reorder_point} units")
print(f"Suggested safety stock: {safety_stock} units")

# --- Step 5: Visualization ---
plt.figure(figsize=(14, 6))
plt.plot(ts.index, ts.values, label="Actual Sales")
plt.plot(pd.date_range(ts.index[-1]+pd.Timedelta(days=1), periods=forecast_period, freq='D'),
         forecast, 'r--', label="30-Day Forecast")
plt.title("Retail Sales: History & 30-Day Forecast")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.tight_layout()
plt.show()

data_reset = data.reset_index()
corr = data_reset[['sales', 'promo']].corr()
sns.heatmap(corr, annot=True, cmap='YlGnBu')
plt.title('Feature Correlation Heatmap')
plt.show()
