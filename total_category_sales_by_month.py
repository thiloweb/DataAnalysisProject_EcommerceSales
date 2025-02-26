import pandas as pd
import matplotlib.pyplot as plt
# Convert back data type for Power BI (str to date)
dataset["order_date"] = pd.to_datetime(dataset["order_date"])
# Create columns and group by months from 11/2023 to 10/2024 for x-axis
orders_fy24_by_months = dataset.groupby([pd.Grouper(key='order_date', axis=0, freq='ME'),"month"]).sum().reset_index()
orders_fy24_by_months["month"] = orders_fy24_by_months["order_date"].dt.month
orders_fy24_by_months["monthname"] = orders_fy24_by_months["order_date"].dt.month_name()
orders_fy24_by_months["year"] = orders_fy24_by_months["order_date"].dt.year
orders_fy24_by_months_monthname_year = orders_fy24_by_months["monthname"] + " " + orders_fy24_by_months["year"].astype(str)
# Set category values for y-label
orders_fy24_electronics = dataset.loc[dataset["category"]=="Electronics"].groupby([pd.Grouper(key='order_date', axis=0, freq='ME'),"category","month"]).sum().reset_index()
orders_fy24_accessories = dataset.loc[dataset["category"]=="Accessories"].groupby([pd.Grouper(key='order_date', axis=0, freq='ME'),"category","month"]).sum().reset_index()
orders_fy24_homekitchen = dataset.loc[dataset["category"]=="Home & Kitchen"].groupby([pd.Grouper(key='order_date', axis=0, freq='ME'),"category","month"]).sum().reset_index()
orders_fy24_furniture = dataset.loc[dataset["category"]=="Furniture"].groupby([pd.Grouper(key='order_date', axis=0, freq='ME'),"category","month"]).sum().reset_index()
category_styling = {"Accessories":{"color":"limegreen","y_legend":0.46},
                    "Electronics":{"color":"red","y_legend":0.88},
                    "Furniture":{"color":"skyblue","y_legend":0.25},
                    "Home & Kitchen":{"color":"goldenrod","y_legend":0.56}
                }
# List of all sales values by month for each category
y_values_labels = [orders_fy24_accessories["order_value"], orders_fy24_electronics["order_value"], orders_fy24_furniture["order_value"], orders_fy24_homekitchen["order_value"]]
x_values = orders_fy24_by_months["order_date"]
# Draw plot
for linegraph in range(len(y_values_labels)):
    plt.plot(x_values,y_values_labels[linegraph], marker='.', color=list(list(category_styling.values())[linegraph].values())[0])
ax = plt.subplot()
plt.xticks(x_values, orders_fy24_by_months_monthname_year, rotation=75, fontsize=12)
plt.yticks(fontsize=12)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'$ {x/1e6:,.2f}M'))
plt.subplots_adjust(bottom=0.30, left=0.13, right=0.80)
for cat_style in range(len(y_values_labels)):
    ax.text(1.02, 
        list(list(category_styling.values())[cat_style].values())[1], # Access y legend height  
        list(category_styling.keys())[cat_style].upper(), # Access category name
        color=list(list(category_styling.values())[cat_style].values())[0], # Access color value
        transform=ax.transAxes, 
        fontsize=13, 
        verticalalignment='top', 
        fontweight="bold")
plt.rcParams['font.sans-serif'] = ['Calibri']
plt.title("Total Category Sales by Month", fontsize=16, fontweight="bold")
plt.grid(alpha = 0.5)
plt.show()