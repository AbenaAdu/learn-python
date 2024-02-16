#Creating descriptions of furniture 
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
print(lovely_loveseat_description)

stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""
print(stylish_settee_description)

luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""
print(luxurious_lamp_description)

#The prices of the furniture
lovely_loveseat_price = 254.00
print(lovely_loveseat_price)

stylish_settee_price = 180.50
print(stylish_settee_price)

luxurious_lamp_price = 52.15
print(luxurious_lamp_price)

#Sales Tax is 8.8%
sales_tax = 0.088
print(sales_tax)

#This will tally the total price for customer one
customer_one_total = 0
print(customer_one_total)

customer_one_total += lovely_loveseat_price 
print(customer_one_total)

customer_one_total += luxurious_lamp_price
print(customer_one_total)

#We are adding to the itemization of what customer one purchases
customer_one_itemization = ""
print(customer_one_itemization)

customer_one_itemization += lovely_loveseat_description
print(customer_one_itemization)

customer_one_itemization += luxurious_lamp_description
print(customer_one_itemization)

#Calculating sales tax for customer's purchase
customer_one_tax = customer_one_total * sales_tax
print(customer_one_tax)

customer_one_total += customer_one_tax
print(customer_one_total)

#We are printing out customer one's receipt
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)
