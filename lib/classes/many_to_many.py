import statistics
class Coffee:

    all =[]

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name (self, value):
        if isinstance(value, str) and not hasattr(self, "name") and 3 <= len(value):
            self._name = value
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        coffee_orders = [order.coffee for order in self.orders()]
        return coffee_orders.count(self)
        # OR...
        # return len(self.orders())
    
    def average_price(self):
        prices = [order.price for order in self.orders() if order.coffee == self]
        return statistics.mean(prices) if len(prices) else 0

class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter 
    def name (self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    # @classmethod
    # def most_aficionado(coffee):
    #     return [customer for customer in Customer.all if order.coffee == date]
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    @price.setter
    def price (self, value):
        if isinstance(value, float) and not hasattr(self, "price") and 1.0 <= value <= 10.0:
            self._price = value

    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value

    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value
