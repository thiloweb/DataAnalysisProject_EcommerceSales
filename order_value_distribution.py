import pandas as pd
import matplotlib.pyplot as plt
# Draw plot
plt.figure(figsize =(5,5))
plt.boxplot(dataset["order_value"], patch_artist=True, boxprops = dict(facecolor = "lightblue"))
plt.text(1.11, 3000, f"AVG: ${dataset["order_value"].mean():.2f}", fontsize = 14, color = "r")
plt.title("Order Value Distribution", fontweight="bold", fontsize=17)
plt.ylabel('Order Value in $', fontweight="bold", fontsize=14)
plt.xticks([])
plt.yticks(fontsize=16)
plt.axhline(dataset["order_value"].mean(), color = 'r',linestyle = '--', linewidth = 1)
plt.rcParams['font.sans-serif'] = ['Calibri']
plt.subplots_adjust(left=0.2)
plt.grid()
plt.show()