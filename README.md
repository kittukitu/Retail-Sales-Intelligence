🛍️ Retail Sales Intelligence AI

An AI-powered tool that combines time series forecasting (Holt-Winters) with Google Gemini AI to predict retail sales trends and provide inventory recommendations.

🚀 Features

Uses Holt-Winters Exponential Smoothing for forecasting.

Predicts the next 3 sales values.

Detects trend direction (increasing 📈 or decreasing 📉).

Generates AI-powered inventory recommendations with explanations.

Supports both command-line arguments and interactive mode.

⚙️ Installation
1. Clone Repository
git clone https://github.com/yourusername/retail-sales-ai.git
cd retail-sales-ai

2. Create Virtual Environment (recommended)
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3. Install Dependencies
pip install -r requirements.txt


requirements.txt

numpy
pandas
statsmodels
google-generativeai
argparse

🔑 Setup Gemini API

Get your API Key from Google AI Studio
.

Replace your key in the script:

genai.configure(api_key="YOUR_API_KEY")

🖥️ Usage
Run with CLI arguments
python app.py --sales 120,135,150,160,170,180,200

Run in interactive mode
python app.py


Example Input/Output:

Enter Sales History (comma-separated, at least 5 values): 120,135,150,160,170,180,200

📊 Forecast & AI Recommendation
Next 3 Sales Predictions: 190.67, 201.23, 211.56
Trend: increasing 📈
Inventory Recommendation: Increase stock levels gradually to match rising demand.

AI Explanation:
The forecast indicates a steady upward trend in sales, so increasing inventory ensures you meet demand without overstocking.

✅ Test Cases
Test Case 1: Increasing Trend
python app.py --sales 100,120,140,160,180,200,220


Expected:

Predictions continue increasing.

Trend: increasing 📈

AI suggests increasing inventory gradually.

Test Case 2: Decreasing Trend
python app.py --sales 500,480,460,440,420,400,380


Expected:

Predictions keep decreasing.

Trend: decreasing 📉

AI suggests reducing inventory or running promotions.

Test Case 3: Insufficient Data
python app.py --sales 100,200,300


Expected:

❌ Error: Need at least 5 data points for forecasting.

📊 Methodology

Forecasting Model → Holt-Winters Exponential Smoothing (trend="add").

Trend Detection → Compares average of last 3 vs first 3 sales values.

AI Recommendation → Prompt to Gemini AI with sales history, forecast, and trend.

📌 Roadmap

 Add visualizations (matplotlib plots of forecasts).

 Support seasonality in Holt-Winters.

 Extend with real POS data integration.