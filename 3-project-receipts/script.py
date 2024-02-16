#Creating descriptions of furniture and their prices 
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
print(lovely_loveseat_description)

lovely_loveseat_price = 254.00
print(lovely_loveseat_price)

stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""
print(stylish_settee_description)

stylish_settee_price = 180.50
print(stylish_settee_price)

luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""
print(luxurious_lamp_description)

luxurious_lamp_price = 52.15
print(luxurious_lamp_price)

#Sales Tax is 8.8%
sales_tax = 0.088
print(sales_tax)

#This will tally the total price for customer one
customer_one_total = 0
print(customer_one_total)

#This will list out the descriptions of what customer one is buying
customer_one_itemization = ""
print(customer_one_itemization)

#We are adding to what customer one is buying
customer_one_total += lovely_loveseat_price 
print(customer_one_total)