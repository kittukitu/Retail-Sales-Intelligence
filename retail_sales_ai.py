import argparse
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import google.generativeai as genai

# 🔑 Configure Gemini
genai.configure(api_key="AIzaSyC2EVCSgC-DRWVunkKi7Ro0J1upoN3UglE")
model = genai.GenerativeModel("gemini-1.5-flash")


def forecast(sales_history):
    try:
        if len(sales_history) < 5:
            print("❌ Error: Need at least 5 data points for forecasting.")
            return

        # Holt-Winters forecasting
        series = pd.Series(sales_history)
        model_hw = ExponentialSmoothing(series, trend="add", seasonal=None)
        model_fit = model_hw.fit()
        forecast_values = model_fit.forecast(steps=3).tolist()

        # Trend detection
        trend_direction = (
            "increasing 📈" if np.mean(sales_history[-3:]) > np.mean(sales_history[:3]) else "decreasing 📉"
        )

        # AI prompt
        prompt = f"""
        You are an AI retail analyst.
        Given the sales history: {sales_history}
        Forecasted next 3 sales: {forecast_values}
        Trend: {trend_direction}

        Provide:
        1. A professional inventory recommendation.
        2. A short explanation why this recommendation is suitable.
        """

        response = model.generate_content(prompt)
        ai_text = response.text if response else "❌ No AI response"

        # Split AI recommendation + explanation
        parts = ai_text.split("\n", 1)
        recommendation = parts[0].strip() if parts else "Not generated"
        ai_explanation = parts[1].strip() if len(parts) > 1 else ai_text

        # Print results
        print("\n📊 Forecast & AI Recommendation")
        print(f"Next 3 Sales Predictions: {', '.join([str(round(x, 2)) for x in forecast_values])}")
        print(f"Trend: {trend_direction}")
        print(f"Inventory Recommendation: {recommendation}")
        print("\nAI Explanation:")
        print(ai_explanation)

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retail Sales Intelligence AI (Terminal Version)")
    parser.add_argument("--sales", type=str, help="Comma-separated sales history (at least 5 values)")

    args = parser.parse_args()

    # If not provided, ask interactively
    sales_input = args.sales if args.sales else input("Enter Sales History (comma-separated, at least 5 values): ")
    sales_history = [float(x.strip()) for x in sales_input.split(",") if x.strip()]

    forecast(sales_history)
