import pandas as pd
import matplotlib.pyplot as plt
# Convert back data type for Power BI (str to date)
dataset["order_date"] = pd.to_datetime(dataset["order_date"])
# Create columns and group by months from 11/2023 to 10/2024 for x-axis
orders_fy24_by_month = dataset.groupby(pd.Grouper(key='order_date', axis=0, freq='ME')).sum().reset_index()
orders_fy24_by_month["month"] = orders_fy24_by_month["order_date"].dt.month
orders_fy24_by_month["monthname"] = orders_fy24_by_month["order_date"].dt.month_name()
orders_fy24_by_month["year"] = orders_fy24_by_month["order_date"].dt.year
orders_fy24_by_month_monthname_year = orders_fy24_by_month["monthname"] + " " + orders_fy24_by_month["year"].astype(str)
# Draw plot
x_values = orders_fy24_by_month["order_date"]
y_values = orders_fy24_by_month["order_value"]
plt.plot(x_values, y_values, marker='.')
ax = plt.subplot()
plt.xticks(x_values, orders_fy24_by_month_monthname_year, rotation=75, fontsize=12)
plt.yticks(fontsize=12)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'$ {x/1e6:,.2f}M'))
plt.subplots_adjust(bottom=0.30, left=0.15)
plt.axhline(orders_fy24_by_month["order_value"].mean(), color = 'r',linestyle = '--', linewidth = 1)
ax.text(0.70, 0.62, f"MONTHLY AVG:\n$ {orders_fy24_by_month["order_value"].mean():,.0f}", transform=ax.transAxes, fontsize=15,verticalalignment='top', color="red", bbox=dict(facecolor='ivory', boxstyle='square,pad=0.5'))
plt.rcParams['font.sans-serif'] = ['Calibri']
plt.title("Total Sales by Month", fontsize=16, fontweight="bold")
plt.grid()
plt.show()