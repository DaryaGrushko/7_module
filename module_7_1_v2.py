#Режимы открытия файлов
#Задача "Учёт товаров"

from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name} , {self.weight} , {self.category}"

class Shop:
    __file_name = 'products.txt'
    def get_products(self):

        file = open(self.__file_name, 'r')
        text = file.read()
        file.close()
        return text
    def add(self, *products):

        for product in products:
            text = self.get_products()

            if  text=='' :

                file = open(self.__file_name, 'a')
                file.write(f"{product.name} , {product.weight} , {product.category}\n")
                file.close()
            else:
                find = str(product.name) + ' , ' + str(product.weight) + ' , ' + str(product.category)
                if find in text:
                    print ('Продукт' , product.name ,  'уже есть в магазине')
                else:
                    file = open(self.__file_name, 'a')
                    file.write(f"{product.name} , {product.weight} , {product.category}\n")
                    file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())

