class Goods(object):
    def __init__(self, id_of_type, name, price):
        self.id_of_type = id_of_type
        self.name = name
        self.price = price

    def set_name(self, n):
        self.name = n

    def set_price(self, p):
        self.price = p

    def __str__(self):
        return "ID of type is: %d\nName is: %s\nPrice is: %d\n" % (self.id_of_type, self.name, self.price)
