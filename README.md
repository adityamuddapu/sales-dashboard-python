Project Overview:

This project analyzes retail sales data (CSV) to generate insights into revenue trends, category performance, and top products. Built with Python, Pandas, and Matplotlib, it demonstrates the full workflow of data cleaning, exploratory data analysis, and dashboard creation to simulate a real-world business scenario.

Key Skills Demonstrated:

- Data cleaning & preprocessing

- Exploratory data analysis

- Visualization for business insights

- Reproducible workflow with requirements.txt


# sales-dashboard-python

Results: Identified revenue seasonality, top-performing categories, and high-revenue products to simulate real-world business intelligence reporting.

### Revenue Trend Analysis (Jan–Jun 2024)  
![Monthly revenue by month](images/revenue_by_month.png)

Revenue dipped in February but rebounded by 30% in June.

### Category Sales Distribution  
![Units sold by category](images/units_by_category.png)

Groceries dominated sales volume (~70%), while Electronics and Clothing lagged significantly.

### Top 5 Products by Revenue
![Top products by revenue](images/top_products_revenue.png)

Monitors and Headphones generated the highest revenue, showing that higher-ticket electronics outperformed apparel despite lower unit volume.

**Tech:** Python, Pandas, Matplotlib

## How to Run

1. Clone the repo.

2. Install dependencies: pip install -r requirements.txt.

3. Run script: python sales_dashboard.py.

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows (PowerShell):
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
python sales_dashboard.py

## Dashboards

### Monthly Revenue Trend
![Monthly revenue by month](images/revenue_by_month.png)

### Units Sold by Category
![Units sold by category](images/units_by_category.png)

### Top Products by Revenue
![Top products by revenue](images/top_products_revenue.png)
