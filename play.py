
import time as t
import random as r

class Customer():
    def __init__(self, max_prices, starting_money) -> None:
        self.inventory = {'cheesecake':0, 'cheese':0, 'milk':0}
        self.max_prices = max_prices
        self.money = starting_money
        self.priority = ['cheesecake', 'cheese', 'milk' ]
        pass

    def tryToBuy(self, vendor):
        for good in self.priority:
            price = vendor.prices[good]
            if price <= self.max_prices[good] and self.money >= price:
                if vendor.stock[good] > 0:
                    self.buy(vendor, good, price)
                    

    def buy(self, vendor, good, price):
        self.money -= price
        vendor.money += price
        self.inventory[good] +=1
        vendor.stock[good] -=1



class Vendor():
    def __init__(self, starting_stock, starting_prices) -> None:
        self.stock = starting_stock
        self.prices = starting_prices
        self.money = 0
        pass

class Player(Vendor):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    def changePrices(self):
        response = input('Change Prices? y/n')
        if response.lower() !='y':
            # print(response.lower())
            return
        print('Current Prices: ', self.prices)
        for good in list(self.prices.keys()):
            new_price = int(input(good + ' new price'))
            self.prices[good] = new_price
        print('New Prices: ', self.prices)


v1 = Vendor({'cheesecake':100, 'cheese':100, 'milk':100}, {'cheesecake':100, 'cheese':10, 'milk':1})
p1 = Player({'cheesecake':100, 'cheese':100, 'milk':100}, {'cheesecake':100, 'cheese':10, 'milk':1})
c1 = Customer({'cheesecake':50, 'cheese':40, 'milk':1}, 1000)
vendors = [v1,p1]
players = [p1]
customers = []
for n in range(10):
    customers.append(Customer({'cheesecake':r.randint(1,200), 'cheese':r.randint(1,100), 'milk':r.randint(1,10)}, r.randint(100,2000)))

for n in range(31):
    t.sleep(1)
    print('Day ', n)
    print('Vendors ________________________________________')
    for v in vendors:
        
        print(v.stock)
        print(v.money)

    print('Customers _______________________________________')
    for c in customers:
        
        print(c.inventory)
        print(c.money)

    if n %5 == 0:
        for p in players:
            print('You have £', p.money)
            other_vendors = vendors.copy()
            other_vendors.remove(p)
            other_vendors_money = []
            for v in other_vendors:
                other_vendors_money.append(v.money)
            other_vendors_money_max = max(other_vendors_money)
            print('Your richest competitor has £', other_vendors_money_max)
            p.changePrices()

    for c in customers:
        for v in vendors:
            c.tryToBuy(v)  

for v in vendors:
    print(v.money)  

    
