import pandas as pd
import matplotlib.pyplot as plt
# Create and group by columns
dataset["total_value"] = dataset["quantity"] * dataset["price_at_purchase"]
sales_fy2024_by_categories = dataset.groupby("category")["total_value"].sum().reset_index()
# Draw plot
category_colors = ["limegreen","red","skyblue","goldenrod"]
plt.pie(sales_fy2024_by_categories["total_value"],
        textprops=dict(color="black",size=14),
        labels=sales_fy2024_by_categories["category"].str.upper(),
        colors=category_colors,
        autopct=lambda x:f"{x:.2f}%\n ($ {x*sum(sales_fy2024_by_categories["total_value"])/1e8 :.2f}M)",
        startangle = 270,
        shadow=True)
plt.rcParams['font.sans-serif'] = ['Calibri']
plt.title("Sales Distribution by Categories", fontsize=16, fontweight="bold")
plt.show()