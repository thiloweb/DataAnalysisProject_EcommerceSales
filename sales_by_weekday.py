import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Group and sort by column
total_by_weekday = dataset.groupby(["dayname","weekday"])["order_value"].sum().reset_index().sort_values(by="weekday")
# Draw plot
x_values = np.arange(len(total_by_weekday["dayname"]))
y_values = total_by_weekday["order_value"]
plt.bar(x_values, y_values, align='center', color="lightblue", edgecolor="black")
plt.xticks(x_values, total_by_weekday["dayname"], rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.ylim(5600000,6400000)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'$ {x/1e6:,.2f}M'))
plt.axhline(y=np.mean(y_values), color = 'r',linestyle = '--', linewidth = 1)
plt.rcParams['font.sans-serif'] = ['Calibri']
plt.text(7, 6000000, "AVG", fontsize = 14, color = "r")
plt.title('Sales by Weekday', fontsize=17, fontweight="bold")
plt.subplots_adjust(bottom=0.20)
plt.show()