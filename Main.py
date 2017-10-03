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

#L_goods = ListOfGoods()
#L_tp_goods = TypeOfGoodsList()
'''''
L_goods.add(Iphone)
L_goods.add(Airmax)
L_goods.add(Game)
L_tp_goods.add(El)
L_tp_goods.add(Sh)
L_tp_goods.add(Gm)
'''''

i = 100
while i != 0:
    i = 100
    i1 = 100
    a = 0
    print("1. Add\n2. Remove\n3. Filter\n4. Show\n5. Exit")
    a = input()
    if a == "1":
        a = "0"
        print("\n1.TypeOfGoods\n2.Goods")
        while i1 != 0:
            a = input()
            if a == "1":
                print("Enter ID of type")
                while f != 1:
                    Type_of_product.id_of_type = int(input())
                    f = 1
                    for i in range(len(L_tp_goods.l_TypeOfGoodList)):
                        if Type_of_product.id_of_type == L_tp_goods.l_TypeOfGoodList[i].id_of_type :
                            f = 0
                            print("error, ID already exists!")
                print("Enter Name")
                Type_of_product.name = str(input())
                print("Enter description")
                Type_of_product.description = str(input())
                L_tp_goods.add(Type_of_product)
                Type_of_product = TypeOfGoods(0, "", "")
                i1 = 0
            elif a == "2":
                print("Enter ID of type")
                f = 0
                while f != 1:
                    Product.id_of_type = int(input())
                    for i in range(len(L_tp_goods.l_TypeOfGoodList)):
                        if Product.id_of_type == L_tp_goods.l_TypeOfGoodList[i].id_of_type :
                            f = 1
                    if f == 0:
                        print("error, this ID doesn`t exist")
                print("Enter Name")
                Product.name = str(input())
                print("Enter price")
                Product.price = int(input())
                L_goods.add(Product)
                Product = Goods(0, "", 0)
                i1 = 0
    elif a == "2":
        print("1. TypeOfGoods\n2. Goods")
        while i1 != 0:
            a = input()
            if a == "1":
                print("Enter name of TypeOfGoods")
                i2 = 1
                while i2 !=0 :
                    a = str(input())
                    i = 0
                    for i in range(len(L_tp_goods.l_TypeOfGoodList)):
                        if a == L_tp_goods.l_TypeOfGoodList[i].name:
                            i2 = 0
                            j = 0
                            n = 0
                            m = len(L_goods.l_goods)
                            #print(m)
                            for j in range(m):
                                if L_tp_goods.l_TypeOfGoodList[i].id_of_type == L_goods.l_goods[j].id_of_type:
                                    n = 1
                            if n == 0:
                                L_tp_goods.l_TypeOfGoodList.pop(i)
                            else:
                                print("Error, you can`t delete a type without deleting items(goods)!")
                            i1 = 0
            elif a == "2":
                print("Enter name of Goods")
                a = str(input())
                i = 0
                f = 0
                m = len(L_goods.l_goods) - 1
                for i in range(m):
                    #print(a,L_goods.l_goods[i].name, i, m)
                    if a == L_goods.l_goods[i].name:
                        L_goods.l_goods.pop(i)
                        i = i - 1
                        f = 1
                        i1 = 0
                    else:
                        i1 = 0
                if f == 0:
                    if a == L_goods.l_goods[m].name:
                        L_goods.l_goods.pop(m)
                        m = len(L_goods.l_goods) - 1
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
        print("\tBYE!\n\t\tI`m looking forward to meeting you :)")
        i = 0
        break

with open('TypeOfGoodsList.pickle', 'wb') as f:
    pickle.dump(L_tp_goods, f)

with open('ListOfGoods.pickle', 'wb') as f:
    pickle.dump(L_goods, f)

