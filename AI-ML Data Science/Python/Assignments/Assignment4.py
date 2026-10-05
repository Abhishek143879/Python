# class product:
#     count = 0
#     def __init__(self, name, price):

#         self.name = name
#         self.price = price
#         product.count +=1

#     def get_info(self):
#         print(self.name, self.price)

#     @classmethod
#     def get_count(cls):
#         print(cls.count)

#     @staticmethod
#     def get_discountedPrice(price,discount):
#         final_amount = price - (price*discount)/100
#         print(final_amount)

# # Creating Objects
# p1 = product("Mobile",40_000)
# p2 = product("Fan", 6_000)
# p3 = product("shoes", 9_000)

# p1.get_info()
# p2.get_info()


# print(p1.name, p1.price)
# print(p2.name, p2.price)
# print(p3.name, p3.price)

# p1.get_count()

# p1.get_discountedPrice(p1.price,10)
# p2.get_discountedPrice(p2.price,10) # can pass the price by using product obj
# p2.get_discountedPrice(7000,10)  # can pass the price directly 



# class BankAccount:
#     def __init__(self, accnt_num, owner_name,Balance):
#         self.accnt_num = accnt_num
#         self.owner_name = owner_name
#         self.Balance = Balance

#     def deposit(self, amount):
#         if (amount<0):
#             print("Amount should be positive")
#         else:
#             self.Balance+=amount
#             print(f"Amount {amount} deposited in Your account Successfully...")

#     def withdraw(self, amount):
#         if (amount>self.Balance):
#             print("Insufficient Balance in your account")
#         else:
#             self.Balance-=amount
#             print(f"Amount {amount} withdrawl from Your account Successfully...")


#     def check_balance(self):
#         print(f"Your account balance is:{self.Balance}")


# p1 = BankAccount("01", "Abhishek", 1000000000000)

# print(p1.owner_name)
# p1.deposit(5000000)
# p1.withdraw(2342342)
# p1.check_balance()



# class Book:
    
#     def __init__(self, title, author):
#         self.title=title
#         self.author=author
#         self.reviews = []
#         self.count = 0

#     def Add_review(self, review):
#         self.reviews.append(review)
#         self.count += 1
#         print(f"Thanks for your review for: {self.title}")

#     def Count_rev(self):
#         print(f"Your book review for {self.title} book are: {self.count}")

#     def display_rev(self):
#         if(len(self.reviews)==0):
#             print("No reviews for this book")
#         else:
#             for review in self.reviews:
#                 print(review)

# b1 = Book("Rich dad poor dad", "charlie")
# b2 = Book("python", "guido")
# b3 = Book("english", "Abhishek")
# print(b1.title)
# b1.Add_review("this is amazing")
# b1.Add_review("this is good")
# b1.Add_review("this is fantastic")
# b2.Add_review("good")
# b2.Count_rev()
# b1.Count_rev()   

# b1.display_rev()
# b3.display_rev()


class Student:
    def __init__(self, name, roll_no, marks):
        self.__name=name
        self.__roll_no=roll_no
        self.__marks=marks

    # Name setter
    def name_setter(self, name):
        if(name == " "):
            print("Provide a name for this")
        else:
            self.__name = name

    # Name getter
    def name_getter(self):
        return self.__name

    # roll no setter
    def roll_setter(self, roll):
        if(int(roll)>=1 and int(roll)<=100):
            self.__roll_no = roll
        else:
            print("invalid Rollno")

    # roll no getter
    def roll_getter(self):
        return self.__roll_no 


s1 = Student("Abhishek", "04", "100")
s1.name_setter("Anurag")
print("Name is:",s1.name_getter())
s1.roll_setter("03")
print(f"Roll no is :{s1.roll_getter()}")
