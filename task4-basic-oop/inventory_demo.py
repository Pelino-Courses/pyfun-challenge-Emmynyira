from product import Product
# creating a product object
product1= Product("water", 1000, 10)
# adding inventory
product1.add_inventory(5)
# removing inventory
product1.remove_inventory(3)
# displaying product information
print(product1.display_info())