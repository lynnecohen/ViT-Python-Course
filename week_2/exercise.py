# ITP Week 2 Day 1 Exercise

# SCENARIO: You're a store owner receiving the inventory report for this month.
# You will receive the product order spreadsheet soon and it is easier to calculate your order
# if your inventory was also on a spreadsheet! Recreate the following spreadsheet with Python: 

# don't forget your appropriate imports.
# assign the title of the initial active sheet to "CURRENT_MONTH_INVENTORY"

import openpyxl
from openpyxl import Workbook

wb = Workbook()
ws=wb.active

ws['A1'] = "product_name"

data = [
    ['product_name','product_id','max_amount','reorder_threshold','quantity'],
	['oreo',2323,1000,300,743],
	['coke',6545, 500,100,101],
	['pepsi',3456,200,50,137],
	['lays_chip',4567,1500,500,364],
	['pringles',2134,2000,600,120],
	['sour_worms',2362,100,10,85],
	['choco_cookies',923,200,25,24],
	['donuts',2786,200,25,12],
	['hot_dogs',6723,100,10,39],
	['ice_cream',9237,200,50,234],
	['gum',2092,3500,1000,1232],
	['pretzels',8246,100,5,11],
	['kit_kat',9276,1000,250,249],
]

# print(data[11][0])


# TIP: create a list of each column (ie. product_names = [oreo, ...]) and use those to loop through :)
row_counter = 0
for row in ws.iter_rows(min_row=1, max_row=14, min_col=1, max_col=5):
    # print(f"row: {row_counter}")
    row_counter += 1
    col_counter=0
    for cell in row:
        # print(f"Column: {col_counter}")
        cell.value = data[row_counter-1][col_counter]
        col_counter += 1
        
# save your file
wb.save("week_2/spreadsheets/inventory.xlsx")