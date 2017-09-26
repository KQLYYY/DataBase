import pickle
from Goods import Goods
from TypeOfGoods import TypeOfGoods
from ListOfGoods import ListOfGoods
from TypeOfGoodsList import TypeOfGoodsList

with open('TypeOfGoodsList.pickle', 'rb') as f:
    L_tp_goods = pickle.load(f)

with open('ListOfGoods.pickle', 'rb') as f:
    L_goods = pickle.load(f)

Type_of_product = TypeOfGoods(0, "", "")
Product = Goods(0, "", 0)

i = 100
while i != 0:
    i = 100
    i1 = 100
    a = 0
    print("1. Add\n2. Edit\n3. Filter\n4. Show\n5. Exit")
    a = input()
    if a == "1":
        a = "0"
        print("\n1.TypeOfGoods\n2.Goods")
        while i1 != 0:
            a = input()
            if a == "1":
                print("Enter ID of type")
                Type_of_product.id_of_type = int(input())
                print("Enter Name")
                Type_of_product.name = str(input())
                print("Enter description")
                Type_of_product.description = str(input())
                L_tp_goods.add(Type_of_product)
                i1 = 0
            elif a == "2":
                print("Enter ID of type")
                Product.id_of_type = int(input())
                print("Enter Name")
                Product.name = str(input())
                print("Enter price")
                Product.price = int(input())
                L_goods.add(Product)
                i1 = 0
    elif a == "2":
        print("1. TypeOfGoods\n2. Goods")
        while i1 != 0:
            a = input()
            if a == "1":
                print("Enter name of TypeOfGoods")
                a = str(input())
                i = 0
                for i in range(len(L_tp_goods.l_TypeOfGoodList)):
                    if a == L_tp_goods.l_TypeOfGoodList[i].name:
                        print("1. id_of_type\n2. name\n3. description")
                        b = str(input())
                        print("Ok, enter new info:",b)
                        if b == "1":
                            L_tp_goods.l_TypeOfGoodList[i].id_of_type = int(input())
                            break
                        elif b == "2":
                            L_tp_goods.l_TypeOfGoodList[i].name = str(input())
                            break
                        elif b == "3":
                            L_tp_goods.l_TypeOfGoodList[i].description = str(input())
                        i1 = 0
            elif a == "2":
                print("Enter name of Goods")
                a = str(input())
                i = 0
                for i in range(len(L_goods.l_goods)):
                    if a == L_goods.l_goods[i].name:
                        print("1. id_of_type\n2. name\n3. price")
                        b = str(input())
                        print("Ok, enter new info:",b)
                        if b == "1":
                            L_goods.l_goods[i].id_of_type = int(input())
                            break
                        elif b == "2":
                            L_goods.l_goods[i].name = str(input())
                            break
                        elif b == "3":
                            L_goods.l_goods[i].price = int(input())
                        i1 = 0
    elif a == "3":
        for i in range(len(L_goods.l_goods)):
           if L_goods.l_goods[i].price < int(100):
               print('-->', L_goods.l_goods[i])
    elif a == "4":
        print("1. List of TypeOfGoods\n2. List of Goods")
        while i1 != 0:
            a = input()
            if a == "1":
                print(L_tp_goods)
                i1 = 0
            elif a == "2":
                print(L_goods)
                i1 = 0
    elif a == "5":
        print("\tBYE!\n\t\tI`m looking forward to meeting you")
        i = 0
        break

with open('TypeOfGoodsList.pickle', 'wb') as f:
    pickle.dump(L_tp_goods, f)

with open('ListOfGoods.pickle', 'wb') as f:
    pickle.dump(L_goods, f)
