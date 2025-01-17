# -*- coding: utf-8 -*-
"""Capstone Project_Walmart.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zMQLd-daCSbqkzFWh5-lUuBq725RkxXi

**Problem Statement 1: Walmart Dataset**

A retail store that has multiple outlets across the country are facing issues in managing the inventory - to match the demand with respect to supply. You are a data scientist, who has to come up with useful insights using the data and make prediction models to forecast the sales for X number of months/years.

**Dataset Information:**
The walmart.csv contains 6435 rows and 8 columns.

**Data Cleaning and Exploration**
"""

# Importing necessary libraries
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("Walmart DataSet.csv")

# 1. Initial exploration of the dataset
print("Shape of the dataset:", df.shape)  # Rows and columns
print("\nFirst five rows of the dataset:")
print(df.head())  # Display first 5 rows

# 2. Checking for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())  # Summing null values per column

# 3. Data types of each column
print("\nData types of columns:")
print(df.dtypes)  # Display data types

# 4. Statistical summary of numerical columns
print("\nStatistical summary of numerical columns:")
print(df.describe())  # Summary statistics (mean, std, min, max, etc.)

# 5. Identifying and handling missing values
# Filling missing values with mean for numeric columns, or mode for categorical
df_cleaned = df.copy()  # Create a copy for cleaning

# Fill numeric missing values with mean
numeric_cols = df_cleaned.select_dtypes(include=[np.number]).columns
df_cleaned[numeric_cols] = df_cleaned[numeric_cols].fillna(df_cleaned[numeric_cols].mean())

# Fill categorical missing values with mode
categorical_cols = df_cleaned.select_dtypes(include=['object']).columns
df_cleaned[categorical_cols] = df_cleaned[categorical_cols].apply(lambda x: x.fillna(x.mode()[0]))

print("\nMissing values after handling:")
print(df_cleaned.isnull().sum())

# 6. Checking for duplicate rows
duplicate_rows = df_cleaned.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicate_rows}")

# 7. Dropping duplicate rows, if any
df_cleaned = df_cleaned.drop_duplicates()

# 8. Distribution of categorical columns (if any)
print("\nDistribution of categorical columns:")
for col in categorical_cols:
    print(f"\nColumn: {col}")
    print(df_cleaned[col].value_counts())

# 9. Correlation matrix for numerical features
import seaborn as sns
import matplotlib.pyplot as plt

print("\nCorrelation matrix for numerical features:")
plt.figure(figsize=(10, 6))
sns.heatmap(df_cleaned[numeric_cols].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()

# 10. Export the cleaned dataset (optional)
cleaned_file_path = '/content/Walmart_Cleaned_DataSet.csv'
df_cleaned.to_csv(cleaned_file_path, index=False)
print(f"Cleaned dataset saved to: {cleaned_file_path}")

"""**Data Visualization**"""

# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Convert date column to datetime (if applicable)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# 2. Check for missing values in the Date column
print("\nMissing values in Date column:")
print(df['Date'].isnull().sum())

# 3. Plotting sales over time
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Weekly_Sales'], marker='o', linestyle='-')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Weekly_Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('Sales_trend_over_time.png')  # Save the plot
plt.show()

# 4. Aggregating and plotting monthly sales trends
df['Month'] = df['Date'].dt.to_period('M')  # Extracting month and year

monthly_sales = df.groupby('Month')['Weekly_Sales'].sum()
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line', marker='o', color='blue')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('monthly_sales_trends.png')
plt.show()

# 5. Sales distribution (histogram)
plt.figure(figsize=(8, 5))
sns.histplot(df['Weekly_Sales'], bins=30, kde=True, color='green')
plt.title('Sales Distribution')
plt.xlabel('Weekly_Sales')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.savefig('sales_distribution.png')
plt.show()

# 6. Box plot to check for outliers in sales
plt.figure(figsize=(8, 5))
sns.boxplot(y=df['Weekly_Sales'], color='cyan')
plt.title('Box Plot of Sales')
plt.grid(True)
plt.tight_layout()
plt.savefig('sales_box_plot.png')
plt.show()

# 7. Yearly sales trends (assuming multiple years of data)
df['Year'] = df['Date'].dt.year
yearly_sales = df.groupby('Year')['Weekly_Sales'].sum()

plt.figure(figsize=(10, 6))
yearly_sales.plot(kind='bar', color='orange')
plt.title('Yearly Sales Trends')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.savefig('Yearly_sales.png')
plt.show()

# 8. Pair plot to visualize relationships between numerical variables
# Selecting relevant numerical columns for the pair plot
numeric_columns = ['Weekly_Sales', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']  # Replace with actual column names

sns.pairplot(df[numeric_columns])
plt.suptitle('Pair Plot of Sales and Other Variables', y=1.02)
plt.tight_layout()
plt.savefig('Pair_plot.png')
plt.show()

# Filter only numeric columns from the dataset
numeric_df = df.select_dtypes(include=[np.number])

# Check if there are numeric columns to plot
if not numeric_df.empty:
    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('correlation_plot.png')
    plt.show()
else:
    print("No numeric columns available for correlation plot.")

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Convert 'Date' column to datetime format (replace 'Date' with the actual date column if different)
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# 2. Store-wise Sales Performance (replace 'Store' and 'Sales' with actual column names)
# Aggregate total sales by store
if 'Store' in df.columns and 'Weekly_Sales' in df.columns:
    store_sales = df.groupby('Store')['Weekly_Sales'].sum().sort_values(ascending=False)

    # Plot the store-wise total sales
    plt.figure(figsize=(10, 6))
    store_sales.plot(kind='bar', color='purple')
    plt.title('Total Sales by Store')
    plt.xlabel('Store')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('store_sales_performance.png')
    plt.show()

    # Insight: Top-performing stores
    top_stores = store_sales.head(5)
    print("Top 5 stores by sales:\n", top_stores)

    # Insight: Underperforming stores
    low_stores = store_sales.tail(5)
    print("\nBottom 5 stores by sales:\n", low_stores)

# 3. Sales Trend Analysis (Monthly/Weekly)
if 'Date' in df.columns and 'Weekly_Sales' in df.columns:
    # Extract month and year from Date
    df['Month'] = df['Date'].dt.to_period('M')  # Monthly
    df['DayOfWeek'] = df['Date'].dt.day_name()  # Day of the week

    # Monthly sales trends
    monthly_sales = df.groupby('Month')['Weekly_Sales'].sum()

    plt.figure(figsize=(10, 6))
    monthly_sales.plot(kind='line', marker='o', color='blue')
    plt.title('Monthly Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('monthly_sales_trends.png')
    plt.show()

    # Insight: Identify peak months
    peak_months = monthly_sales.sort_values(ascending=False).head(3)
    print("\nTop 3 months with the highest sales:\n", peak_months)

# 4. Sales by Day of the Week
if 'DayOfWeek' in df.columns and 'Weekly_Sales' in df.columns:
    weekly_sales = df.groupby('DayOfWeek')['Weekly_Sales'].sum().sort_values()

    plt.figure(figsize=(10, 6))
    weekly_sales.plot(kind='bar', color='green')
    plt.title('Sales by Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Total Sales')
    plt.tight_layout()
    plt.savefig('sales_by_day_of_week.png')
    plt.show()

    # Insight: Best day of the week for sales
    best_day = weekly_sales.idxmax()
    print("\nDay with the highest sales: ", best_day)

# 5. Category/Product Analysis (if applicable, replace 'Category' with the actual column name)
# Example: Aggregate sales by product category
if 'Category' in df.columns and 'Weekly_Sales' in df.columns:
    category_sales = df.groupby('Category')['Weekly_Sales'].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    category_sales.plot(kind='bar', color='orange')
    plt.title('Total Sales by Product Category')
    plt.xlabel('Category')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('sales_by_category.png')
    plt.show()

    # Insight: Top-selling product categories
    top_categories = category_sales.head(3)
    print("\nTop 3 product categories by sales:\n", top_categories)

# 6. Promotions and Holidays Impact (if applicable)
# Example: Create a new column for holiday season impact if a "Holiday" column exists
if 'Holiday_Flag' in df.columns and 'Weekly_Sales' in df.columns:
    holiday_sales = df.groupby('Holiday_Flag')['Weekly_Sales'].mean()

    plt.figure(figsize=(8, 5))
    holiday_sales.plot(kind='bar', color='red')
    plt.title('Average Sales During Holidays')
    plt.xlabel('Holiday (Yes = 1/No = 0)')
    plt.ylabel('Average Sales')
    plt.tight_layout()
    plt.savefig('holiday_sales_impact.png')
    plt.show()

    # Insight: Holiday vs Non-holiday sales comparison
    print("\nSales impact during holidays vs non-holidays:\n", holiday_sales)

"""**Sales Forecasting Using SARIMA**"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
import warnings
warnings.filterwarnings('ignore')

# 1. Convert 'Date' column to datetime format (replace 'Date' with actual column name)
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# 2. Group the sales by Store and Date (weekly aggregation)
if 'Date' in df.columns and 'Store' in df.columns and 'Weekly_Sales' in df.columns:
    df.set_index('Date', inplace=True)  # Set date as the index
    df = df.groupby(['Store', pd.Grouper(freq='W')])['Weekly_Sales'].sum().reset_index()

# Create a dictionary to store forecasts for each store
store_forecasts = {}

# Function to forecast sales for a store
def forecast_sales_for_store(store_data, store_name):
    # Set the 'Date' column as index
    store_data.set_index('Date', inplace=True)

    # Split into train and test sets (train on all data and forecast for 12 weeks)
    train = store_data['Weekly_Sales']

    # Build SARIMA model (order and seasonal order can be fine-tuned)
    model = SARIMAX(train,
                    order=(1, 1, 1),
                    seasonal_order=(1, 1, 1, 52),  # Weekly seasonality
                    enforce_stationarity=False,
                    enforce_invertibility=False)

    sarima_model = model.fit(disp=False)

    # Forecast for the next 12 weeks
    forecast = sarima_model.get_forecast(steps=12)
    forecast_values = forecast.predicted_mean

    # Confidence intervals
    conf_int = forecast.conf_int()

    # Plotting the forecast
    plt.figure(figsize=(10, 6))
    plt.plot(train.index, train, label='Observed Sales')
    forecast_index = pd.date_range(start=train.index[-1], periods=13, freq='W')[1:]
    plt.plot(forecast_index, forecast_values, label='Forecasted Sales', color='orange')
    plt.fill_between(forecast_index, conf_int.iloc[:, 0], conf_int.iloc[:, 1], color='pink', alpha=0.3)
    plt.title(f'Sales Forecast for Store {store_name} (Next 12 Weeks)')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'store_{store_name}_sales_forecast.png')
    plt.show()

    # Save the forecasted sales in a dictionary
    store_forecasts[store_name] = forecast_values

# 3. Apply the forecast function for each store
stores = df['Store'].unique()  # Get a list of unique stores

for store in stores:
    # Get the data for the current store
    store_data = df[df['Store'] == store][['Date', 'Weekly_Sales']]

    # Forecast sales for the store
    forecast_sales_for_store(store_data, store)

# Print the forecasted sales for each store
for store_name, forecast in store_forecasts.items():
    print(f"\nForecasted Sales for Store {store_name} (Next 12 Weeks):\n", forecast)

"""**Model Evaluation**"""

# Split the data into training and test sets
train_data = df['Weekly_Sales'][:-12]  # Use all but the last 12 weeks for training
test_data = df['Weekly_Sales'][-12:]  # Use the last 12 weeks for testing

from statsmodels.tsa.statespace.sarimax import SARIMAX

sarima_model = SARIMAX(train_data, order=(1,1,1), seasonal_order=(1,1,1,52))
sarima_fit = sarima_model.fit()

from sklearn.metrics import mean_absolute_error, mean_squared_error

# Predictions on the test data
predictions = sarima_fit.get_forecast(steps=len(test_data)).predicted_mean

# Calculate evaluation metrics
mae = mean_absolute_error(test_data, predictions)
mse = mean_squared_error(test_data, predictions)
rmse = np.sqrt(mse)
mape = np.mean(np.abs((test_data - predictions) / test_data)) * 100

print(f'MAE: {mae}, MSE: {mse}, RMSE: {rmse}, MAPE: {mape}')

"""**Residual Analysis**"""

import statsmodels.api as sm

# Plot residuals
residuals = sarima_fit.resid
plt.figure(figsize=(10,6))
plt.subplot(211)
residuals.plot(title="Residuals", ax=plt.gca())

# ACF plot of residuals
plt.subplot(212)
sm.graphics.tsa.plot_acf(residuals, lags=40, ax=plt.gca())
plt.savefig('Residuals_plot.png')
plt.show()

"""**Forecast Accuracy on the Test Set**"""

# Get forecast for the test period
forecast = sarima_fit.get_forecast(steps=len(test_data))
forecast_values = forecast.predicted_mean

# Plot the forecasted vs actual sales
plt.figure(figsize=(10, 6))
plt.plot(train_data.index, train_data, label='Training Sales')
plt.plot(test_data.index, test_data, label='Actual Sales')
plt.plot(test_data.index, forecast_values, label='Forecasted Sales')
plt.title('Actual vs Forecasted Sales')
plt.legend()
plt.savefig('Actual vs Forecasted Sales_plot.png')
plt.show()

"""**Model Diagnostics**"""

print(f'AIC: {sarima_fit.aic}, BIC: {sarima_fit.bic}')