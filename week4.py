#Problem 1
# year=int(input("Enter your birth year:  ")
# age= 2019-year
# print(f"You are {age} years old!")

 #Problem2
# nameInput= input("Enter a name: ")
# names="Kenn","Kevin","Erin","Autumn"
# if nameInput=="kenn":
#     print("hello teacher")
# elif nameInput=="kevin":
#     print("hello teacher")
# elif nameInput=="erin":
#     print("hello teacher")
# elif nameInput=="autumn":
#     print("hello teacher")
# else:
#     print("Hello Student")

# #Problem 3
# numberInput= int(input("Enter a negative number:  "))
# for i in range(7,numberInput-1,-1):
#     print(i)
#
# # #Problem 4
# randomInput=int(input("Enter a random number between -10 and -5: "))
# x=0
# while x<1:
#     if randomInput<=-10 and randomInput>=-5:
#         print("Good Job")
#         break;
#     else:
#        print("try Again")
#     randomInput=int(input("Enter again"))

# # #Problem 5
squad = ["One", "Two", "Three", "Four", "Five"]


# #Problem 6
def nameFunc(firstName):
    lnameInput=input("Enter your last name: ")
    print(f" Hello, {firstName} {lnameInput}")
nameFunc("Jordon")

# #Problem 7
class Books:
    def __init__(self,name, rating, genre, author):
        self.name=name
        self.rating=rating
        self.genre=genre
        self.author=author
    def changeRating(self):
        ratingInput= int(input("Enter a new rating: "))
        self.rating= ratingInput

book1= Books("cat in the hat",5,"children","dr. suess")
book2= Books("4 agreements",5,"self help","don miguel")
book3= Books("Apple Sauce",3,"kids","Jordon")

booklist=[book1,book2,book3]
for e in booklist:
    print(e)
#
# #Problem 8
def numberFunc():
    newInput=int(input("Enter a number: "))
    if newInput<=-50 and newInput>=5:
        return f"Funds too low"
    elif newInput>=5 and newInput<=50:
        return f"You should add more funds"
    else:
        return f"Just enough"
print(numberFunc())

#Problem 9
input2= int(input("enter a positive number:" ))
newArray=[]
for i in range(0,len(newArray)):
        i+=1
        print(newArray.append(input2))
#
# #Problem 10

class Pet:
    def __init__(self,type,breed):
        self.type=type
        self.breed=breed
    def printAllAttributes(self):
        print(f"{self.breed}, {self.type}"

pet1= Pet("Dog", "Pitbull")
pet2= Pet("Cat","sphinx")
pet3= Pet("Frog","bullfrog")

pet_list=[pet1,pet2,pet3]
for x in pet_list:
    print(x)