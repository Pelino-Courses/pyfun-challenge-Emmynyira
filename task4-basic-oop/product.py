class Product:
    """ 
Aclass to represent the product in an inventory system.

Attributes:
name(str): the name of the product.
price(float): the price of single unit of the product.
quantity(int): the quantity of the products in the stock.
Methods:
add_inventory(amaount): adds stock to the produuct.
remove_inventory(amount): Removes stock from the product.
toatal_value(): returns the total value of the product in stock(price*quantity).
display_product(): returns a string representation of the product.

"""
    def __init__(self,name,price,quantity):
        """
        Initializes the product with name, price and quantity.
        Args:
        name(str): the name of the product.
        price(float): the price of single unit of the product(must be non-negative).
        quantity(int): the quantity of the product in stock(must be non-negative). 
        Raises:
        ValueError: if the the price or quantity is negative
        """       
        self.name= name
        self.price= price
        self.quantity= quantity
        if price < 0:
            raise ValueError("Price must not be negative.")
        if quantity < 0:
            raise ValueError("Quantity must not be negative.")
    def add_inventory(self,amount):
       """
        Adds given amount to the product stock.

        Arguments:
        amaount(int): numbrer of units to add into the stock.
       Raises:
         ValueError: if the amount is negative.
        """        
       if amount < 0:
         raise ValueError("you can not remove negative inventory.")
         self.quantity += amount
    def remove_inventory(self,amount):
        if amount < 0:
            raise ValueError("you can not remove negative inventory.")
        if amount > self.quantity: 
         raise ValueError(f"can not remove {amount} units;only{self.quantity} units in stock.")
         self.quantity -= amount
    def total_value(self)->float:
          """
           culculates the total value of the current inventory.
         Returns:
        float: tatal value = price * quantity.
        """
          return self.price * self.quantity
    def display_info(self)->str:
        """
         displays the product information.
        """
        print(f"Product Name: {self.name}")
        print(f"Price: {self.price}") 
        print(f"Quantity: {self.quantity}")
        print(f"Total Value: $ {self.total_value()}")
    def get_name(self)->str:
        """
        Returns the name of the product.
        """
        return self.name
    def get_price(self)->float:
        """
        Returns the price of the product.
        """
        return self.price
    def get_quantity(self)->int:
        """
        Returns the quantity of the product.
        """
        return self.quantity