item = [101, 102, 103, 104, 105]
product = ['milk', 'cheese', 'ghee', 'Bread', 'curd']
price = [42, 50, 500, 40, 30]
stock = [10, 20, 15, 16, 30]
pinput = int(input(f'Enter the product number:- '))
quantity = int(input("Enter the number of quantity:- "))
if pinput in item:
    s = item.index(pinput)
    if quantity <= stock[s]:
        total = price[s] * quantity
        r = stock[s] - quantity
        stock[s] = r
        print(f"Total bill is {total}")
        print(f'available stock is {r}')
    else:
        print("Sorry item is out of stock")
else:
    print(f"please select the only this item no {item}")
