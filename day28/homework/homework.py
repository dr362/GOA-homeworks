# ```1)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა ორი რიცხვი შემდეგ კი გამოიტანეთ ამ რიცხვების ნამრავლი.

# 2)შექმენით ფუნქცია რომელსაც გადაეცემა არგუმენტად რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ლუწია ეს რიცხვი თუ კენტი.

# 3)შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სახელი და დაბეჭდავს მისთვის მიესალმებას (მაგალითად: "Hello Giorgi"). გამოძახეთ ეს ფუნქცია 2-ჯერ და გადაეცით სხვადასხვა სახელი.

# 4)შექმენით ფუნქცია, რომელიც იღებს ორ სტრინგს და მოახდინეთ კონკატენაცია.

# ```
#1)
def double(num1 , num2):
    print(num1 * num2)
double(2,10)
#2)
def check(num1):
    if num1 % 2 == 0:
        print("luwia")
    else:
        print("kentia")

check(2)
#3)
def hi(name1,name2):
    print("hello",name1)
    print("hello",name2)
hi("alexandre","gio")
#4)
def combine(str1,str2):
    print(str1 + str2)
combine("foot","ball")
