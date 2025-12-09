class Student:
    def __init__(self, name: str, year: int):
        self.name = name
        self.year = year

class infornation:
    def __init__(self):
        pass
    def add_student(self,name,year):
        self.name = name
        self.year = year
    def print_student(self):
        return f"Student, Year:{self.year} and name:{self.name}"

student = Student("Алена", 12)
student_info = infornation()
student_info.add_student("Алена",12)
print(student_info.print_student())
        




class bank_info:
    def __init__(self,number: str,amount=0):
        self.number = number
        self.amount = amount
    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
            return f"Ваш рахунок поповнено на {amount} грн"
        else:
            raise ValueError("Неможливо поповнити тому що введене число <= 0")
    def withdraw(self, amount):
        if amount > 0:
            if self.amount - amount >= 0:
                self.amount = self.amount - amount
                return f"Ви зняли {amount} грн"
            else:
                return f"Недостатньо коштів"
        else:
            raise ValueError("Неможливо поповнити тому що введене число <= 0")
    def show_balance(self):
        return f"Ваш рахунок {self.amount} грн"
    

Bank_info = bank_info("4446344678532768")
print(Bank_info.show_balance())
print(Bank_info.deposit(1000))
print(Bank_info.show_balance())
print(Bank_info.withdraw(566363))
print(Bank_info.show_balance())
print(Bank_info.withdraw(900))
print(Bank_info.show_balance())



class Product:
    def __init__(self, product: str, price: int, number: int):
        self.product = product
        self.price = price
        self.number = number

    def __str__(self):
        return f"Товар: {self.product}, кількість на складі: {self.number}, ціна: {self.price}"

class Store:

    def __init__(self, name):
        self.name = name
        self.product_list = [] 

    def add_product(self, product: str):
        if isinstance(product, Product):
            self.product_list.append(product)
            return f"Товар {product} додана до {self.name}"
        else:
            return "Такий товар вже є"

    def buy(self, product_name, amount: int):
        for item in shop.product_list:
            if item.product == product_name:
                if amount <= 0:
                    return "Неможливо придбати 0 або менше товару"
                elif item.number >= amount:
                    item.number -= amount
                    return f"Було придбано {amount} {item.product} по ціні {item.price}"
                else:
                    return "Недостатньо товару на складі"


    def show_products(self):
        print(f"Товари у {self.name}")
        if not self.product_list:
            raise ValueError("Нема нічого")
        else:
            for product_list in self.product_list:
                print(product_list)

p1 = Product("Телефон", 5000, 10) 
p2 = Product("Ноутбук", 25000, 5)

shop = Store("Мій магазин")
shop.add_product(p1)
shop.add_product(p2)
shop.show_products()
print(shop.buy("Телефон", 3))
shop.show_products()
print(shop.buy("Ноутбук", 2))
shop.show_products()
shop.add_product(Product("Банан", 5, 200))
shop.show_products()
print(shop.buy("Банан", 10))
shop.show_products()

