import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Create bins
bins_by_1000 = np.arange(0,12)*1000
# Draw plot
plt.hist(dataset["order_value"], edgecolor="black", linewidth=0.2, color="lightblue")
ax = plt.subplot()
ax.text(0.54, 0.93, f"Total Order Quantity:\n{dataset["order_id"].count()}", transform=ax.transAxes, fontsize=13, fontweight="bold",verticalalignment='top', bbox=dict(facecolor='ivory', boxstyle='square,pad=0.5', alpha=0.5))
plt.title("Frequency Distribution of Order Values", fontsize=16, fontweight="bold")
plt.xticks(bins_by_1000, fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel("Order Value Range in $", fontweight="bold", fontsize=12)
plt.ylabel("Number of Orders", fontweight="bold", fontsize=12)
plt.rcParams['font.sans-serif'] = ['Calibri']
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x/1000:,.0f}k'))
plt.subplots_adjust(left=0.15)
plt.show()