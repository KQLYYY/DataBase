class ListOfGoods(object):
    def __init__(self):
        self.l_goods = []

    def add(self, goods):
        self.l_goods.append(goods)

    def __str__(self):
        return '\n'.join(str(goods) for goods in self.l_goods)
