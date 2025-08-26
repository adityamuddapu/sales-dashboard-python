# sales-dashboard-python

Small analytics project that loads a CSV of retail sales and produces:
- Monthly revenue trend (`revenue_by_month.png`)
- Units sold by category (`units_by_category.png`)
- Top products by revenue (`top_products_revenue.png`)
- Descriptive stats (`summary_stats.md`)

**Tech:** Python, Pandas, Matplotlib

## Run
```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows (PowerShell):
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
python sales_dashboard.py
