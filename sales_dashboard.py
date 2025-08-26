import pandas as pd
import matplotlib.pyplot as plt

# 1) Load & clean
df = pd.read_csv("sales.csv", parse_dates=["date"])
df["revenue"] = df["units_sold"] * df["unit_price"]
df = df.dropna()

print("=== basic summary ===")
print(df.describe(include="all"))

# 2) Monthly revenue trend
monthly_rev = (
    df.set_index("date")
      .groupby(pd.Grouper(freq="M"))["revenue"]
      .sum()
)
plt.figure(figsize=(8,4))
monthly_rev.plot(marker="o")
plt.title("Monthly Revenue")
plt.ylabel("USD")
plt.xlabel("Month")
plt.tight_layout()
plt.savefig("revenue_by_month.png")
plt.close()

# 3) Units sold by category
cat_units = df.groupby("category")["units_sold"].sum().sort_values(ascending=False)
plt.figure(figsize=(6,4))
cat_units.plot(kind="bar")
plt.title("Units Sold by Category")
plt.ylabel("Units")
plt.tight_layout()
plt.savefig("units_by_category.png")
plt.close()

# 4) Top products by revenue
top_products = (
    df.groupby("product")["revenue"]
      .sum()
      .sort_values(ascending=True)
      .tail(5)
)
plt.figure(figsize=(7,4))
top_products.plot(kind="barh")
plt.title("Top 5 Products by Revenue")
plt.xlabel("USD")
plt.tight_layout()
plt.savefig("top_products_revenue.png")
plt.close()

# 5) Quick stats table to Markdown
summary = df[["units_sold","unit_price","revenue"]].describe().round(2)
summary.to_markdown("summary_stats.md")

print("done. images: revenue_by_month.png, units_by_category.png, top_products_revenue.png")
