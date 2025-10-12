print("welcome to pizza online ordering system")
print("please input 'y' if you want to order, otherwise input 'n' to exit")
price = 0

pizza = input("pizza? (price_359): ")
if pizza == "y":
    price += 359

chicken = input("chicken? (price_199): ")
if chicken == "y":
    price += 199    

pasta = input("pasta? (price_259): ")  
if pasta == "y":
    price += 259

total = price
print("Total price is %d." %total)