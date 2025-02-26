import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Create bins
bins_by_1000 = np.arange(0,12)*1000
binned_value_ranges = pd.cut(dataset["order_value"], bins=bins_by_1000)
sales_by_bins = dataset["order_value"].groupby(binned_value_ranges, observed=True).sum().reset_index(name = 'total_by_bin')
# Draw plot
plt.subplots(figsize=(9,6))
ax = plt.subplot()
x_values = sales_by_bins.index.values
y_values = sales_by_bins["total_by_bin"]
bars = ax.bar(x_values,y_values,color="lightblue", edgecolor="black", linewidth=0.5)
ax.bar_label(bars, fmt=lambda x:f'{x/1e6:.2f}M', fontsize=12)
plt.title("Total Sales by Order Value Range", fontsize=16, fontweight="bold")
plt.xticks(x_values, labels=x_values, fontsize=12)
plt.yticks(fontsize=12)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'$ {x/1e6:,.0f}M'))
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x} - {x+1}k'))
plt.rcParams['font.sans-serif'] = ['Calibri']
plt.xlabel("Order Value Range in $", fontweight="bold", fontsize="12")
plt.show()