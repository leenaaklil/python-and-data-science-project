# utils.py
import numpy as np
import pandas as pd
from datetime import datetime

def generate_random_sales(min_val, max_val, size):
    return np.random.randint(min_val, max_val + 1, size)

def generate_sales_data():
    
    # Generate monthly dates
    dates = pd.date_range(start='2025-01-01', end='2025-12-01', freq='MS')
    
    # Generate sales data for each product
    product_a = generate_random_sales(50, 100, 12)
    product_b = generate_random_sales(30, 80, 12)
    product_c = generate_random_sales(20, 60, 12)
    product_d = generate_random_sales(10, 50, 12)
    
    # Create DataFrame
    sales_df = pd.DataFrame({
        'Date': dates,
        'Product_A': product_a,
        'Product_B': product_b, 
        'Product_C': product_c,
        'Product_D': product_d
    })
    
    return sales_df

if __name__ == "__main__":
    # Generate and save initial data
    df = generate_sales_data()
    df.to_csv('data/initial.csv', index=False)
    print("Initial data saved to data/initial.csv")