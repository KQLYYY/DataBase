class TypeOfGoodsList(object):
    def __init__(self):
        self.l_TypeOfGoodList = []

    def add(self, t_goods):
        self.l_TypeOfGoodList.append(t_goods)

    def __str__(self):
        return '\n'.join(str(t_goods) for t_goods in self.l_TypeOfGoodList)
