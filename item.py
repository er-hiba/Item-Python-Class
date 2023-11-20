class Item:
    def __init__(self, price_excluding_tax, vat):
        # Initialize the 'price_excluding_tax' and 'vat' variables
        self.vat = vat
        self.price_excluding_tax = price_excluding_tax

    def total(self):
        # Calculate the total price including tax
        total_price = self.price_excluding_tax * (1 + self.vat / 100)
        
        # Display information about the item: price excluding tax, VAT rate, and total price
        print("The price excluding tax of the item is:", self.price_excluding_tax)
        print("The VAT rate is:", self.vat, "%")
        print("The total price of the item is:", total_price)

# Create an instance of the 'Item' class with price and VAT rate
item1 = Item(50, 3)

# Calculate and display the total price
item1.total()
