import openpyxl

from openpyxl import Workbook

# ITP Week 2 Day 1 Exercise
wb = Workbook()
ws = wb.active
# SCENARIO: You're a store owner receiving the inventory report for this month.
# You will receive the product order spreadsheet soon and it is easier to calculate your order
# if your inventory was also on a spreadsheet! Recreate the following spreadsheet with Python: 

# don't forget your appropriate imports.
# assign the title of the initial active sheet to "CURRENT_MONTH_INVENTORY"

ws.title = "CURRENT_MONTH_INVENTORY"

txt = """product_name    product_id  max_amount      reorder_threshold   quantity
	oreo            2323        1000            300                 743
	coke            6545        500             100                 101
	pepsi	        3456        200             50                  137
	lays_chip	    4567        1500            500                 364
	pringles	    2134        2000            600                 120
	sour_worms	    2362        100             10                  85
	choco_cookies   0923	    200             25                  24
	donuts	        2786        200             25                  12
	hot_dogs	    6723        100             10                  39
	ice_cream	    9237        200             50                  234
	gum	            2092        3500            1000                1232
	pretzels        8246	    100             5                   11
	kit_kat	        9276        1000            250                 249"""
# TIP: create a list of each column (ie. product_names = [oreo, ...]) and use those to loop through :)



# product_names = []
# product_ids = []
# max_amounts = []
# reorder_thresholds = []
# quantities = []

# for row in product_row[1:]:
#     row = row.strip()
#     if not row:
#         continue
#     product_cell = row.split()
#     product_names.append(product_cell[0])
#     product_ids.append(product_cell[1])
#     max_amounts.append(int(product_cell[2]))
#     reorder_thresholds.append(int(product_cell[3]))
#     quantities.append(int(product_cell[4]))

# print(product_cell)
# print(product_names)
# print(product_ids)
# print(max_amounts)
# print(reorder_thresholds)
# print(quantities)

product_row = (txt.replace("\t"," ")).split("\n")

x = 1

for row in product_row:
    y = 1
    row = row.strip()
    if not row:
        continue
    product_cell = row.split()

    n = 0
    for value in product_cell:
        ws.cell(row=x, column=y, value=product_cell[n])
        y += 1
        n += 1
    x += 1

# save your file
wb.save("week_2\spreadsheets\inventory.xlsx")