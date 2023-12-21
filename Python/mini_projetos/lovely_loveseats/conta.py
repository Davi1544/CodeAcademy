# lovely loveseat
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

# stylish settee
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

# luxurious lamp
luxurious_lamp_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
luxurious_lamp_price = 52.15

# outras variáveis
sales_tax = .088
customer_one_total = 0
customer_one_itemization = ""
customer_one_tax = 0

# adicionando valores
customer_one_total += (lovely_loveseat_price + luxurious_lamp_price)
customer_one_itemization += (lovely_loveseat_description + luxurious_lamp_description)
customer_one_tax += (customer_one_total * sales_tax)
customer_one_total += customer_one_tax

# printando a conta
print("Customer One Items: " + str(customer_one_itemization))
print("Customer One Total: " + str(customer_one_total))