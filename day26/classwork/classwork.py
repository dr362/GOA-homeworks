# # დავალება:
# ```
# 1)კომენტარის სახით ახსენით append / insert / pop / len ფუნქციები.

# 2)შექმენით სია რომელიც შედგება 5 სახელისგან შემდეგ insert მეთოდის გამოყენებით დაამატეთ მე4 ინდექსზე კიდევ ერთი სახელი.

# 3)შექმენით სია რომელიც შედგება 5 ელემენტისგან და შემდეგ pop მეთოდის გამოყენებით ამოაკელით სიის პირველი და ბოლო ელემენტი.

# 4)შექმენით სია რომელშიც იქნება 10 ელემენტი, შემდეგ მომხმარებელს შემოატანინეთ რიცხვი და ამ რიცხვის ინდექსზე მდგომი ელემენტი ამოაგდეთ სიიდან.

# 5)მომხმარებელს შემოატანინეთ სახელი, თუ მისი სახელი შედგება 5ზე მეტი სიმბოლოსგან, მაშინ დაუბეჭდეთ "Hello" / სხვა შემთხვევაში "Bye"```
#1)
# len() - გვიბრუნებს სიის ან სტრინგის სიგრძეს
# .append() - სიის ბოლოში ამატებს გადაცემულ ელემენტს
# .insert() - სიის კონკრეტულ ინდექსზე ამატებს ახალ ელემენტს
# .pop() - კონკრეტულ ინდექსზე მდგომ ელემენტს ამოაგდებს სიიდან
#2)
names = ["nikolozi", "alexandre","deme","taso","gabriel"]
names.insert(3,"mariami")
print(names)
#3)
names = ["nikolozi", "alexandre","deme","taso","gabriel"]
names.pop(0)
names.pop(3)
print(names)
#4)
nums = [1,2,3,4,5,6,7,8,9,10]
nums.pop(2)
print(nums)
#5)
name = "alexandre"
if  > 5:
    print("Hello")
else:
    print("bye")